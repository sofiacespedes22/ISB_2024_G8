import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo excluyendo las líneas de encabezado y los comentarios
data = []
with open("parte_4.txt", "r") as file:
    for line in file:
        if not line.startswith('#'):
            data.append(list(map(int, line.strip().split())))

# Convertir los datos a un array de numpy
array = np.array(data)

# Obtener la longitud de la señal
n = len(array)

# Calcular el vector de tiempo conocida la longitud y el intervalo de muestreo (Ts)
Fs = 1000  # Frecuencia de muestreo (Hz)
Ts = 1 / Fs
t = np.arange(0, n*Ts, Ts)

# Extraer la columna de la señal
signal = array[:, -1]  # Última columna del array

# Calcular la Transformada de Fourier Discreta (DFT)
N = len(signal)  # Número de puntos de la señal
frequencies = np.fft.fftfreq(N, Ts)[:N // 2]  # Vector de frecuencias positivas
fft_values = np.fft.fft(signal - np.mean(signal)) / N  # Valores de la DFT normalizados

# Plotear la señal y la magnitud de la DFT
plt.figure(figsize=(10, 6))

# Plotear la señal
plt.subplot(2, 1, 1)
plt.plot(t, signal, label="Señal")
plt.ylim(0, 1200)

plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.legend(loc="upper right")
plt.title("Señal ECG")

# Plotear la magnitud de la DFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_values[:N // 2]))
plt.title('FFT')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0,100)
plt.grid(True)

# Añadir título principal
plt.suptitle('Prosim4 PARO CARDIACO STEP 2', fontsize=16)

plt.tight_layout()
plt.show()


