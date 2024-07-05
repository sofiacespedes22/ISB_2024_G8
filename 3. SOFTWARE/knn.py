import os
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

def calculate_features(ecg_signal, sampling_rate=1000):
    peaks, _ = find_peaks(ecg_signal, distance=sampling_rate/2.5)
    rr_intervals = np.diff(peaks) / sampling_rate
    
    minRR = np.min(rr_intervals) if len(rr_intervals) > 0 else np.nan
    maxRR = np.max(rr_intervals) if len(rr_intervals) > 0 else np.nan
    avgRR = np.mean(rr_intervals) if len(rr_intervals) > 0 else np.nan
    SDNN = np.std(rr_intervals, ddof=1) if len(rr_intervals) > 0 else np.nan
    rmsSD = np.sqrt(np.mean(np.square(np.diff(rr_intervals)))) if len(rr_intervals) > 0 else np.nan
    NN20 = np.sum(np.abs(np.diff(rr_intervals)) > 0.02) if len(rr_intervals) > 1 else np.nan
    pNN20 = NN20 / len(rr_intervals) if len(rr_intervals) > 1 else np.nan

    return [minRR, maxRR, avgRR, SDNN, rmsSD, NN20, pNN20]

def process_folder(folder_path, label):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            ecg_signal = df['ecg'].values
            features = calculate_features(ecg_signal)
            features.append(label)
            data.append(features)
    return data

# Paths to your folders
normal_folder = "normal"
arrhythmia_folder = "supraventricular"

# Process both folders
normal_data = process_folder(normal_folder, 0)  # Label 0 for normal
arrhythmia_data = process_folder(arrhythmia_folder, 1)  # Label 1 for arrhythmia

# Create DataFrame
columns = ['minRR', 'maxRR', 'avgRR', 'SDNN', 'rmsSD', 'NN20', 'pNN20', 'label']
df = pd.DataFrame(normal_data + arrhythmia_data, columns=columns)

# Drop rows with NaN values
df.dropna(inplace=True)

# Split the data
X = df.drop('label', axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Create and train the k-NN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = knn.predict(X_test)
print(classification_report(y_test, y_pred))
