import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo excluyendo las 2 primeras filas del archivo
array = np.genfromtxt("señal.txt", delimiter="\t", skip_header=3)



# Obtener la longitud de la señal
n = len(signal)

# Calcular el vector de tiempo conocida la longitud y el intervalo de muestreo (Ts)
Fs = 1000  # Asumiendo una frecuencia de muestreo de 100 Hz
Ts = 1 / Fs
t = np.arange(0, n * Ts, Ts)

ti=1000
tf=1200

# Extraer la columna de la señal
signal = array[ti*Fs:tf*Fs, 5]

# Ploteamos la señal
plt.plot(t, signal, label="Señal")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EMG")
plt.show()
