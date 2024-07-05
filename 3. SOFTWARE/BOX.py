import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks

# Función para cargar señal desde el archivo CSV
def load_signal(filename):
    data = pd.read_csv(filename)
    signal = data['ecg'].values  # Ajusta el nombre de la columna aquí
    return signal

# Función para detectar picos R
def detect_r_peaks(ecg_signal, fs):
    peaks, _ = find_peaks(ecg_signal, height=None, distance=int(0.6 * fs))
    return peaks

# Función para extraer características de los segmentos de 4 segundos
def extract_hrv_features(signal, peaks, fs, window_size=4):
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

# Configuración inicial
fs = 250  # Frecuencia de muestreo en Hz

# Directorios con los archivos CSV
normal_dir = 'normal'
supraventricular_dir = 'supraventricular'

# Lista para almacenar características extraídas
hrv_features_list = []

# Procesar archivos en la carpeta 'normal'
for filename in os.listdir(normal_dir):
    if filename.endswith('.csv'):
        filepath = os.path.join(normal_dir, filename)
        signal = load_signal(filepath)
        peaks = detect_r_peaks(signal, fs)
        features = extract_hrv_features(signal, peaks, fs)
        features['label'] = 'normal'
        hrv_features_list.append(features)

# Procesar archivos en la carpeta 'supraventricular'
for filename in os.listdir(supraventricular_dir):
    if filename.endswith('.csv'):
        filepath = os.path.join(supraventricular_dir, filename)
        signal = load_signal(filepath)
        peaks = detect_r_peaks(signal, fs)
        features = extract_hrv_features(signal, peaks, fs)
        features['label'] = 'supraventricular'
        hrv_features_list.append(features)

# Crear un DataFrame con las características
df_hrv_features = pd.DataFrame(hrv_features_list)

# Generar boxplots para cada característica individualmente
feature_columns = df_hrv_features.columns.difference(['label'])

for feature in feature_columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='label', y=feature, data=df_hrv_features)
    plt.title(f'Boxplot de {feature}')
    plt.xticks(rotation=45)
    plt.show()
