import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.signal import find_peaks, filtfilt, iirfilter, butter
from scipy.stats import kurtosis
from sklearn.preprocessing import normalize

# Función para calcular la SNR
def calculate_snr(signal, noise):
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Función para el filtro IIR
def iir_filter_signal(signal, fs):
    cutoff_frequency_iir = 50 / (fs / 2)
    b, a = iirfilter(N=4, Wn=cutoff_frequency_iir, btype='low', ftype='butter')
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

# Función para el filtro Butterworth
def butter_lowpass_filter(data, cutoff_freq, sampling_freq, order=4):
    nyquist_freq = 0.5 * sampling_freq
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Leer y preparar la señal EMG
emg_signals = np.genfromtxt("Biceps.txt", delimiter="\t", skip_header=3, missing_values=0)
chn = 5
emg_signal = emg_signals[:, chn]
emg_signal = emg_signal - np.mean(emg_signal)
fs_emg = 500
t_emg = np.arange(0, len(emg_signal) / fs_emg, 1 / fs_emg)

# Agregar ruido a la señal para simular condiciones de prueba
noise = np.random.normal(0, 0.5, emg_signal.shape)
noisy_signal = emg_signal + noise

# Filtro Wavelet
n_level = 7
emg_coeffs = pywt.wavedec(noisy_signal, 'sym3', level=n_level)
threshold = 16
emg_coeffs_thresh = [pywt.threshold(c, threshold, mode='soft') for c in emg_coeffs]
filtered_signal_wavelet = pywt.waverec(emg_coeffs_thresh, 'sym3')

# Filtro Butterworth
filtered_signal_butter = butter_lowpass_filter(noisy_signal, 40, fs_emg)

# Filtro IIR
filtered_signal_iir = iir_filter_signal(noisy_signal, fs_emg)

# Calcular el ruido residual para cada filtro
residual_noise_wavelet = noisy_signal - filtered_signal_wavelet[:len(noisy_signal)]
residual_noise_butter = noisy_signal - filtered_signal_butter
residual_noise_iir = noisy_signal - filtered_signal_iir

# Calcular SNR para cada señal filtrada
snr_wavelet = calculate_snr(filtered_signal_wavelet[:len(noisy_signal)], residual_noise_wavelet)
snr_butter = calculate_snr(filtered_signal_butter, residual_noise_butter)
snr_iir = calculate_snr(filtered_signal_iir, residual_noise_iir)

print(f"SNR para filtro Wavelet: {snr_wavelet:.2f} dB")
print(f"SNR para filtro Butterworth: {snr_butter:.2f} dB")
print(f"SNR para filtro IIR: {snr_iir:.2f} dB")

# Determinar el filtro más efectivo
snr_values = {'Wavelet': snr_wavelet, 'Butterworth': snr_butter, 'IIR': snr_iir}
best_filter = max(snr_values, key=snr_values.get)

print(f"El filtro más efectivo es: {best_filter} con una SNR de {snr_values[best_filter]:.2f} dB")

# Graficar las señales originales y filtradas
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t_emg, noisy_signal, label="Señal con ruido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EMG con Ruido")

plt.subplot(4, 1, 2)
plt.plot(t_emg, filtered_signal_wavelet[:len(t_emg)], label="Filtrado Wavelet", color='red')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EMG Filtrada - Wavelet")

plt.subplot(4, 1, 3)
plt.plot(t_emg, filtered_signal_butter, label="Filtrado Butterworth", color='green')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EMG Filtrada - Butterworth")

plt.subplot(4, 1, 4)
plt.plot(t_emg, filtered_signal_iir, label="Filtrado IIR", color='blue')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EMG Filtrada - IIR")

plt.tight_layout()
plt.show()

