import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, filtfilt

# Funciones para crear y aplicar filtros elípticos
def elliptic_lowpass(cutoff, fs, order=5, rp=1, rs=40):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = ellip(order, rp, rs, normal_cutoff, btype='low', analog=False)
    return b, a

def elliptic_highpass(cutoff, fs, order=5, rp=1, rs=40):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = ellip(order, rp, rs, normal_cutoff, btype='high', analog=False)
    return b, a

def elliptic_bandstop(lowcut, highcut, fs, order=4, rp=1, rs=40):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = ellip(order, rp, rs, [low, high], btype='bandstop')
    return b, a

def apply_filter(data, filter_func, *args):
    b, a = filter_func(*args)
    y = filtfilt(b, a, data)
    return y

# Función para cargar señal desde el archivo
def load_signal(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = [line.strip().split()[-1] for line in lines if not line.startswith('#')]
    signal = np.array(data, dtype=np.float64)
    return signal

# Función para calcular SNR
def calculate_snr(signal, filtered_signal):
    # Potencia de la señal original
    signal_power = np.sum(signal ** 2) / len(signal)
    
    # Potencia del ruido (diferencia entre señal original y filtrada)
    noise = signal - filtered_signal
    noise_power = np.sum(noise ** 2) / len(noise)
    
    # SNR en dB
    snr = 10 * np.log10(signal_power / noise_power)
    
    return snr

# Cargar señal desde el archivo
signal = load_signal('post salto.txt')

# Parámetros de los filtros
fs = 1000.0  # frecuencia de muestreo
lowcut = 0.5  # frecuencia de corte para el filtro paso alto
highcut = 45.0  # frecuencia de corte para el filtro paso bajo
notch_low = 49.0  # frecuencia de inicio del filtro notch
notch_high = 51.0  # frecuencia de fin del filtro notch

# Aplicar filtros elípticos
filtered_signal_low = apply_filter(signal, elliptic_lowpass, highcut, fs)
filtered_signal_high = apply_filter(filtered_signal_low, elliptic_highpass, lowcut, fs)
filtered_signal = apply_filter(filtered_signal_high, elliptic_bandstop, notch_low, notch_high, fs)

# Calcular SNR de la señal original y la filtrada
snr_original = calculate_snr(signal, filtered_signal)
snr_filtrada = calculate_snr(filtered_signal, signal)

# Graficar señales y mostrar SNR
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(signal, label='Señal original')
plt.title('Señal original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(filtered_signal, label='Señal filtrada')
plt.title('Señal filtrada')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()

plt.subplot(3, 1, 3)
plt.bar(['Original', 'Filtrada'], [snr_original, snr_filtrada], color=['blue', 'green'])
plt.title('SNR')
plt.ylabel('SNR (dB)')

plt.tight_layout()
plt.show()

print(f'SNR de la señal filtrada: {snr_original:.2f} dB')
print(f'SNR de la señal original: {snr_filtrada:.2f} dB')
