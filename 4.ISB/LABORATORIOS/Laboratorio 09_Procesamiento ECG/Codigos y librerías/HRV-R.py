import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks, lfilter
import pywt

# Coeficientes del filtro de Blackman
b_blackman = np.array([
    -2.094552056898734e-18, 0.003034066721839687, 0.014580168473481207, 
    0.0390825116714423, 0.0772588321610623, 0.12172524448293782, 
    0.15816651137549176, 0.17230533022748998, 0.15816651137549176, 
    0.12172524448293782, 0.0772588321610623, 0.0390825116714423, 
    0.014580168473481207, 0.003034066721839687, -2.094552056898734e-18
])

# Función para filtrar la señal ECG con un filtro Butterworth pasa banda
def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

# Función para aplicar el filtro wavelet
def wavelet_filter(data, wavelet='sym3', level=8, threshold=10):
    coeffs = pywt.wavedec(data, wavelet, level=level)
    coeffs_thresh = [pywt.threshold(c, threshold, mode='soft') for c in coeffs]
    filtered_data = pywt.waverec(coeffs_thresh, wavelet)
    return filtered_data

# Función para detectar los picos R en la señal ECG
def detect_r_peaks(ecg_signal, fs):
    filtered_ecg = butter_bandpass_filter(ecg_signal, 5, 15, fs)
    diff_ecg = np.diff(filtered_ecg)
    squared_diff_ecg = diff_ecg**2
    integrated_ecg = np.convolve(squared_diff_ecg, np.ones(int(0.080 * fs)) / fs, mode='same')

    threshold = 0.5 * np.max(integrated_ecg)
    r_peaks, _ = find_peaks(integrated_ecg, height=threshold, distance=0.2 * fs)
    
    return r_peaks

# Función para calcular HRV en tiempo real con ventanas deslizantes
def real_time_hrv(ecg_signal, fs, window_size=4, overlap=0.5):
    step_size = int(window_size * (1 - overlap) * fs)
    window_length = int(window_size * fs)
    num_windows = (len(ecg_signal) - window_length) // step_size + 1

    hrv_features = {
        'minRR': [],
        'maxRR': [],
        'avgRR': [],
        'SDNN': [],
        'rmsSD': [],
        'NN20': [],
        'pNN20': [],
        'NN50': [],
        'pNN50': [],
        'avgIHR': [],
        'stdIHR': [],
        'SD1': [],
        'SD2': [],
        'frequency_analysis': {}  # Almacenar información de análisis de frecuencia
    }

    for i in range(num_windows):
        start = i * step_size
        end = start + window_length
        window_signal = ecg_signal[start:end]

        r_peaks = detect_r_peaks(window_signal, fs)
        rr_intervals = np.diff(r_peaks) / fs
        rr_intervals = rr_intervals[(rr_intervals > 0.4) & (rr_intervals < 2.0)]

        if len(rr_intervals) > 0:
            # Estadísticas básicas
            hrv_features['minRR'].append(np.min(rr_intervals))
            hrv_features['maxRR'].append(np.max(rr_intervals))
            hrv_features['avgRR'].append(np.mean(rr_intervals))
            hrv_features['SDNN'].append(np.std(rr_intervals))
            hrv_features['rmsSD'].append(np.sqrt(np.mean(np.diff(rr_intervals)**2)))

            # NN20 y pNN20
            nn20 = np.sum(np.abs(np.diff(rr_intervals)) > 0.02)
            hrv_features['NN20'].append(nn20)
            hrv_features['pNN20'].append(nn20 / len(rr_intervals))

            # NN50 y pNN50
            nn50 = np.sum(np.abs(np.diff(rr_intervals)) > 0.05)
            hrv_features['NN50'].append(nn50)
            hrv_features['pNN50'].append(nn50 / len(rr_intervals))

            # Frecuencia cardíaca instantánea
            ihr = 60 / rr_intervals
            hrv_features['avgIHR'].append(np.mean(ihr))
            hrv_features['stdIHR'].append(np.std(ihr))

            # Análisis de Poincaré
            sd1, sd2 = poincare_analysis(rr_intervals)
            hrv_features['SD1'].append(sd1)
            hrv_features['SD2'].append(sd2)

            # Análisis de frecuencia
            freq_analysis = frequency_domain_analysis(rr_intervals)
            hrv_features['frequency_analysis'][f'Window_{i+1}'] = freq_analysis

    return hrv_features

# Función para el análisis de Poincaré
def poincare_analysis(rr_intervals):
    sd1 = np.std(np.diff(rr_intervals)) / np.sqrt(2)
    sd2 = np.std(rr_intervals[:-1] - rr_intervals[1:]) / np.sqrt(2)
    return sd1, sd2

# Función para el análisis de dominio de frecuencia
def frequency_domain_analysis(rr_intervals):
    # Aquí puedes implementar el análisis de dominio de frecuencia
    # Puedes usar métodos como el método de Lomb-Scargle
    # y calcular la potencia en las bandas de frecuencia específicas
    freq_analysis = {
        'LF': 0.15,  # Ejemplo de potencia en la banda de frecuencia baja
        'HF': 0.4    # Ejemplo de potencia en la banda de frecuencia alta
        # Agrega más información según sea necesario
    }
    return freq_analysis

# Función principal para cargar la señal ECG y calcular HRV
def main():
    fs = 1000  # Frecuencia de muestreo
    data = []

    # Cargar la señal ECG desde un archivo
    with open("ECG_Salto.txt", "r") as file:
        for line in file:
            if not line.startswith('#'):
                data.append(list(map(int, line.strip().split())))

    array = np.array(data)
    n = len(array)
    ts = 1 / fs
    t = np.arange(0, n * ts, ts)
    signal = array[:, -1]

    # Aplicar el filtro Butterworth
    butter_filtered_signal = butter_bandpass_filter(signal, 5, 15, fs)

    # Aplicar el filtro de Blackman
    blackman_filtered_signal = lfilter(b_blackman, 1, butter_filtered_signal)

    # Aplicar el filtro Wavelet
    wavelet_filtered_signal = wavelet_filter(blackman_filtered_signal)
    ecg_signal = wavelet_filtered_signal

    # Calcular HRV
    hrv_results = real_time_hrv(ecg_signal, fs)

    # Plotear datos
    plt.plot(t, wavelet_filtered_signal, 'r', label="Señal Filtrada (Butterworth + Blackman + Wavelet)")
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Cantidad de picos
    # Identificar los picos R en la señal filtrada
    r_peaks = detect_r_peaks(ecg_signal, fs)
    num_r_peaks = len(r_peaks)
    print(f"Número de picos R identificados: {num_r_peaks}")

    # Mostrar resultados de HRV
    print("Resultados de HRV:")
    for key, value in hrv_results.items():
        if key == 'frequency_analysis':
            print("Análisis de Frecuencia:")
            for window, freq_info in value.items():
                print(f"Ventana {window}: {freq_info}")
        else:
            print(f"{key}: {value}")

    # Aquí puedes agregar visualizaciones si lo deseas

if __name__ == "__main__":
    main()
