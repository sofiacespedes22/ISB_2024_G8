import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, iirfilter, butter, filtfilt

# Función para el filtro IIR
def iir_filter_signal(signal, Fs):
    cutoff_frequency_iir = 50 / (Fs / 2)
    iir_filter = iirfilter(N=4, Wn=cutoff_frequency_iir, btype='low', ftype='butter')
    ecg_filtered = lfilter(iir_filter[0], iir_filter[1], signal)
    return ecg_filtered

# Función para el filtro Butterworth
def butter_lowpass_filter(data, cutoff_freq, sampling_freq, order=4):
    nyquist_freq = 0.5 * sampling_freq
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Leer el archivo de señal ECG excluyendo las líneas de encabezado y los comentarios
data_ecg = []
with open("Prueba_Pulgar.txt", "r") as file:
    for line in file:
        if not line.startswith('#'):
            data_ecg.append(list(map(int, line.strip().split())))

# Convertir los datos a un array de numpy
array_ecg = np.array(data_ecg)
n_ecg = len(array_ecg)
Fs_ecg = 1000
t_ecg = np.arange(0, n_ecg * (1 / Fs_ecg), (1 / Fs_ecg))
signal_ecg = array_ecg[:, -1]

# Aplicar el filtro IIR a la señal ECG
ecg_filtered = iir_filter_signal(signal_ecg, Fs_ecg)

# Leer el archivo de señal EMG excluyendo las líneas de encabezado y los comentarios
data_emg = []
with open("EMG.txt", "r") as file:
    for line in file:
        if not line.startswith('#'):
            data_emg.append(list(map(int, line.strip().split())))

# Convertir los datos a un array de numpy
array_emg = np.array(data_emg)
n_emg = len(array_emg)
Fs_emg = 1000
t_emg = np.arange(0, n_emg * (1 / Fs_emg), (1 / Fs_emg))
signal_emg = array_emg[:, -1]

# Aplicar el filtro Butterworth a la señal EMG
filtered_signal_emg = butter_lowpass_filter(signal_emg, 40, Fs_emg)

# Graficar ambas señales originales y filtradas
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t_ecg, signal_ecg, label="Señal ECG Original")
plt.ylim(0, 1200)
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.legend(loc="upper right")
plt.title("Señal ECG")

plt.subplot(2, 2, 2)
plt.plot(t_emg, signal_emg, label="Señal EMG Original")
plt.ylim(0, 1200)
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.legend(loc="upper right")
plt.title("Señal EMG")

plt.subplot(2, 2, 3)
plt.plot(t_ecg, ecg_filtered, label="Señal ECG Filtrada", color='red')
plt.ylim(0, 1200)
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.legend(loc="upper right")
plt.title("Señal ECG Filtrada")

plt.subplot(2, 2, 4)
plt.plot(t_emg, filtered_signal_emg, label="Señal EMG Filtrada", color='red')
plt.ylim(0, 1200)
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.legend(loc="upper right")
plt.title("Señal EMG Filtrada")

plt.tight_layout()
plt.show()

