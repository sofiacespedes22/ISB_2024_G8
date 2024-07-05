import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, hilbert, ellip, filtfilt

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

# Función para detectar picos R
def detect_r_peaks(ecg_signal, fs):
    peaks, _ = find_peaks(ecg_signal, height=None, distance=int(0.6 * fs))
    return peaks

# Función para extraer características de los segmentos de 4 segundos
def extract_hrv_features(signal, peaks, fs, window_size=4):
    window_samples = int(window_size * fs)
    rr_intervals = np.diff(peaks) / fs  # Calcular intervalos RR en segundos
    
    # Características de HRV
    minRR = np.min(rr_intervals)
    maxRR = np.max(rr_intervals)
    avgRR = np.mean(rr_intervals)
    SDNN = np.std(rr_intervals)
    rmsSD = np.sqrt(np.mean(np.diff(rr_intervals)**2))
    NN20 = np.sum(np.diff(rr_intervals) > 0.02)
    pNN20 = NN20 / len(rr_intervals)
    NN50 = np.sum(np.diff(rr_intervals) > 0.05)
    pNN50 = NN50 / len(rr_intervals)
    avg_IHR = 60 / avgRR
    std_IHR = np.std(60 / rr_intervals)
    
    # Calcular SD1 y SD2 (ejes sub-elípticos del diagrama de Poincaré)
    SD1 = np.sqrt(0.5 * np.std(np.diff(rr_intervals))**2)
    SD2 = np.sqrt(2 * SDNN**2 - SD1**2)
    
    return {
        'minRR': minRR,
        'maxRR': maxRR,
        'avgRR': avgRR,
        'SDNN': SDNN,
        'rmsSD': rmsSD,
        'NN20': NN20,
        'pNN20': pNN20,
        'NN50': NN50,
        'pNN50': pNN50,
        'avg_IHR': avg_IHR,
        'std_IHR': std_IHR,
        'SD1': SD1,
        'SD2': SD2
    }

# Cargar señal y aplicar filtros
filename = 'post salto.txt'
signal = load_signal(filename)
fs = 1000.0  # Frecuencia de muestreo

# Parámetros de los filtros
lowcut = 0.5  # Frecuencia de corte para el filtro paso alto
highcut = 45.0  # Frecuencia de corte para el filtro paso bajo
notch_low = 49.0  # Frecuencia de inicio del filtro notch
notch_high = 51.0  # Frecuencia de fin del filtro notch

# Aplicar filtros elípticos
filtered_signal_low = apply_filter(signal, elliptic_lowpass, highcut, fs)
filtered_signal_high = apply_filter(filtered_signal_low, elliptic_highpass, lowcut, fs)
filtered_signal = apply_filter(filtered_signal_high, elliptic_bandstop, notch_low, notch_high, fs)

# Detectar picos R en la señal filtrada
r_peaks = detect_r_peaks(filtered_signal, fs)

# Extraer características de HRV para segmentos de 4 segundos alrededor de cada pico R
window_size_seconds = 4
hrv_features = extract_hrv_features(filtered_signal, r_peaks, fs, window_size_seconds)

# Imprimir características de HRV
print("Características de HRV:")
for key, value in hrv_features.items():
    print(f"{key}: {value}")

# Graficar la señal filtrada y los picos R detectados
plt.figure(figsize=(14, 6))
time = np.arange(len(filtered_signal)) / fs
plt.plot(time, filtered_signal, label='Señal filtrada')
plt.plot(r_peaks / fs, filtered_signal[r_peaks], 'ro', label='Picos R detectados')
plt.title('Señal de ECG Filtrada con Picos R Detectados')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
