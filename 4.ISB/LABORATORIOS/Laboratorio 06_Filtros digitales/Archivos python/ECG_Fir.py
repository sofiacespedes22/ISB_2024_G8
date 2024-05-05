import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Cargar la señal del archivo
data = []
with open("ECG_Exhalación.txt", "r") as file:
    for line in file:
        if not line.startswith('#'):
            data.append(list(map(int, line.strip().split())))
array = np.array(data)
n = len(array)
Fs = 1000  # Frecuencia de muestreo (Hz)
Ts = 1 / Fs
t = np.arange(0, n*Ts, Ts)
signal = array[:, -1]

# Coeficientes del filtro de Blackman
b_blackman = np.array([-2.094552056898734e-18, 0.003034066721839687, 0.014580168473481207, 0.0390825116714423, 0.0772588321610623, 0.12172524448293782, 0.15816651137549176, 0.17230533022748998, 0.15816651137549176, 0.12172524448293782, 0.0772588321610623, 0.0390825116714423, 0.014580168473481207, 0.003034066721839687, -2.094552056898734e-18])

# Aplicar el filtro a la señal
y = lfilter(b_blackman, 1, signal)

# Recortar la señal filtrada a partir de los 400 mV
y_trimmed = y[y >= 400]

# Graficar la señal original y la señal filtrada recortada
plt.figure(figsize=(20, 10))

plt.plot(t, signal, 'b')
plt.title('Señal original: ECG')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.grid(True)

plt.tight_layout()
plt.show()

plt.plot(t[len(y)-len(y_trimmed):], y_trimmed, 'r')
plt.title('Señal filtrada FIR (Blackman)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.grid(True)

plt.tight_layout()
plt.show()
