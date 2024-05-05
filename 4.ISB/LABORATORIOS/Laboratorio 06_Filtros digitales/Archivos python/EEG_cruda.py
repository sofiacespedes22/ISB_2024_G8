import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import pywt
from scipy import signal
from scipy.signal import firwin, lfilter

"""## Obtenemos las señales sin filtrar

"""

arrayeeg = np.genfromtxt("EEG_Reposo1.txt", delimiter="\t",skip_header = 3, missing_values= 0)
#Extraemos la columna de la señal y creamos sus respectivos vectores tiempos
signaleeg = arrayeeg[:, 5]
signaleeg = signaleeg[0:30000]
Fs_eeg = 1000
Ts_eeg = 1/Fs_eeg
n_eeg= 30000
t_eeg = np.arange(0,n_eeg*Ts_eeg,Ts_eeg)
t_eeg

"""## Ploteamos las señales sin filtrar

## Ploteamos las señales sin filtrar
"""
plt.plot(t_eeg, signaleeg, label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EEG - Sin Filtrar")
plt.show()


"""## Aplicamos el filtrado con IIR
"""
# Crear un filtro de banda de paso Butterworth con las características indicadas en la bibliografía
FL_eeg = 0.5  # Frecuencia de corte inferior
FH_eeg = 50  # Frecuencia de corte superior
butterworth_bandpass_eeg = signal.butter(3, [FL_eeg, FH_eeg], btype='band', analog=False, fs=Fs_eeg, output='ba')
# Aplicamos el filtro a la señal
filtered_eeg_signal = lfilter(butterworth_bandpass_eeg[0], butterworth_bandpass_eeg[1], signaleeg)
plt.plot(t_eeg, filtered_eeg_signal, 'r', label='Señal de EEG  filtrada IIR')
plt.title('Señal de EEG - Filtrada IIR')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.show()

#Diseñamos el filtro FIR con las características indicadas en la literatura.
frecuencia_corte_1 = 0.5  # Frecuencia de corte 1 en Hz
frecuencia_corte_2 = 12  # Frecuencia de corte 2 en Hz
orden = 2  # Orden del filtro
numtaps = 2 * orden + 1
filtro_fir_eeg = firwin(numtaps, [frecuencia_corte_1, frecuencia_corte_2], pass_zero=False, fs=Fs_eeg, window='hamming')
eeg_filtered = lfilter(filtro_fir_eeg, 1, signaleeg)

plt.plot(t_eeg, eeg_filtered, 'r', label='Señal EEG filtrada')
plt.title('Señal EEG - Filtrada con FIR')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.show()
