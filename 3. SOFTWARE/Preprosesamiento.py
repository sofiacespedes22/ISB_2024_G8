import numpy as np
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

# Función para normalizar la señal
def normalize_signal(signal):
    normalized_signal = (signal - np.min(signal)) / (np.max(signal) - np.min(signal))
    return normalized_signal

# Función principal que filtra y normaliza la señal
def filter_and_normalize_signal(filename, fs):
    signal = load_signal(filename)

    # Parámetros de los filtros
    lowcut = 0.5  # Frecuencia de corte para el filtro paso alto
    highcut = 45.0  # Frecuencia de corte para el filtro paso bajo
    notch_low = 49.0  # Frecuencia de inicio del filtro notch
    notch_high = 51.0  # Frecuencia de fin del filtro notch

    # Aplicar filtros elípticos
    filtered_signal_low = apply_filter(signal, elliptic_lowpass, highcut, fs)
    filtered_signal_high = apply_filter(filtered_signal_low, elliptic_highpass, lowcut, fs)
    filtered_signal = apply_filter(filtered_signal_high, elliptic_bandstop, notch_low, notch_high, fs)

    # Normalizar la señal filtrada
    normalized_signal = normalize_signal(filtered_signal)

    return normalized_signal

# Ejemplo de uso de la función
if __name__ == "__main__":
    filename = 'post salto.txt'
    fs = 1000.0  # Frecuencia de muestreo

    # Obtener la señal filtrada y normalizada
    normalized_signal = filter_and_normalize_signal(filename, fs)

    # Imprimir la señal normalizada
    print(normalized_signal)
