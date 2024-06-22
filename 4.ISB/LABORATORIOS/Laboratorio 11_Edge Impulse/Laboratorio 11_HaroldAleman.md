<h1 style="text-align: center;">Laboratorio 11: Edge impulse (EI)</h1>
Integrante: Harold Aleman Ramirez

<a id = "Informe edge impulse" style></a>
<h2 style = "text-align: center;">Objetivos</h2>
- Crear un proyecto en EI por cada señal trabaja en clases; es decir, para EMG, ECG, EEG. <br />
- Subir cada señal mediante un código en python a EI.<br />

<h2 style = "text-align: center;">Código en python</h2>
1. Codigo de python: El código de Python convierte la señal de texto a un archivo CSV y luego segmenta la señal según la ventana propuesta para cada tipo de señal. El código es similar tanto para ECG como para EMG, y se muestra a continuación. Sin embargo, para EEG, se agregará en un segundo bloque ya que EEG tiene varios canales por cada señal. Además, se realiza un ventaneo utilizando un valor de ventana encontrado en la literatura.

```python
##ECG y EMG
import requests
import os
import csv

def txt_to_csv_first_window(txt_file_path, base_csv_file_path):
    with open(txt_file_path, 'r') as txt_file:
        # Saltar las líneas de encabezado
        for line in txt_file:
            if line.startswith('#'):
                continue
            break  # La primera línea después del encabezado ya está leída
        
        window_data = []
        timestamp = 0  # Inicializa el timestamp en 0
        window_count = 0  # Contador de ventanas
        
        for line in txt_file:
            columns = line.strip().split('\t')  # Asumiendo que los valores están separados por tabulaciones
            if len(columns) >= 6:
                window_data.append([timestamp, columns[5]])  # Añadir el timestamp y el valor de EMG
                timestamp += 1  # Incrementar el timestamp por 1 ms
                if len(window_data) == 250:
                    # Crear el archivo CSV para la ventana actual de datos
                    csv_file_path = f"{base_csv_file_path}_window_{window_count}.csv"
                    with open(csv_file_path, 'w', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(['timestamp', 'emg'])  # Escribir los encabezados
                        csv_writer.writerows(window_data)  # Escribir las filas de datos
                    window_count += 1
                    window_data = []  # Reiniciar los datos de la ventana

        # Si hay datos restantes en la última ventana incompleta, escribirlos también
        if window_data:
            csv_file_path = f"{base_csv_file_path}_window_{window_count}.csv"
            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['timestamp', 'emg'])  # Escribir los encabezados
                csv_writer.writerows(window_data)  # Escribir las filas de datos

# Ejemplo de uso
txt_file_path = 'Biceps.txt'
base_csv_file_path = 'Biceps'
txt_to_csv_first_window(txt_file_path, base_csv_file_path)

# Clave API de Edge Impulse
api_key = 'ei_705e952bd5423499302e8a8acc41ab5ff4d869473319209bda65ee0518a3eaa3'

# Agrega los archivos .csv que deseas subir a Edge Impulse
files = [f for f in os.listdir() if f.startswith(base_csv_file_path) and f.endswith('.csv')]

# Reemplaza la etiqueta con la tuya propia.
label = 'car'

# Prepara los archivos para la solicitud
prepared_files = []
for file in files:
    prepared_files.append(('data', (os.path.basename(file), open(file, 'rb'), 'text/csv')))

# Sube los archivos a Edge Impulse usando la API y imprime la respuesta.
try:
    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                        headers={
                            'x-label': label,
                            'x-api-key': api_key,
                        },
                        files=prepared_files)

    if res.status_code == 200:
        print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
    else:
        print('Failed to upload file(s) to Edge Impulse\n', res.status_code, res.content)
finally:
    # Asegúrate de cerrar los archivos después de la solicitud
    for _, (filename, fileobj, _) in prepared_files:
        fileobj.close()


```
```python
##EEG
import numpy as np
import os
import csv
import requests

# Función para extraer y procesar los datos de OpenBCI
def extract_file_OpenBCI(file):
    array = np.genfromtxt(file + ".txt", delimiter=",", skip_header=5)
    chs = np.transpose(array[:, 1:9])
    return chs

# Función para convertir los valores ADC a microvoltios
def touV_byOpenBCI(ad_values, scale_factor=0.02235):
    """
    Convert OpenBCI raw ADC values to microvolts.
    
    Parameters:
    ad_values: List of ADC values from OpenBCI.
    scale_factor: Scale factor for the specific OpenBCI board (Cyton: 0.02235, Ganglion: 0.0419453125)
    
    Returns:
    List of microvolt values.
    """
    uv_values = ad_values * scale_factor
    return uv_values

# Función para segmentar el archivo de señal EEG y convertirlo a CSV
def txt_to_csv_first_window(txt_file_path, base_csv_file_path, window_size=250):
    chs = extract_file_OpenBCI(txt_file_path)
    
    for ch_index in range(8):  # Procesar los 8 canales
        channel_data = touV_byOpenBCI(chs[ch_index])
        window_data = []
        timestamp = 0
        window_count = 0
        
        for i, value in enumerate(channel_data):
            window_data.append([timestamp, value])
            timestamp += 1  # Incrementar el timestamp por 1 ms
            if len(window_data) == window_size:
                # Crear el archivo CSV para la ventana actual de datos
                csv_file_path = f"{base_csv_file_path}_ch{ch_index}_window_{window_count}.csv"
                with open(csv_file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['timestamp', 'eeg'])  # Escribir los encabezados
                    csv_writer.writerows(window_data)  # Escribir las filas de datos
                window_count += 1
                window_data = []  # Reiniciar los datos de la ventana

        # Si hay datos restantes en la última ventana incompleta, escribirlos también
        if window_data:
            csv_file_path = f"{base_csv_file_path}_ch{ch_index}_window_{window_count}.csv"
            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['timestamp', 'eeg'])  # Escribir los encabezados
                csv_writer.writerows(window_data)  # Escribir las filas de datos

# Función para subir los archivos CSV a Edge Impulse
def upload_to_edge_impulse(base_csv_file_path, api_key, label):
    # Agrega los archivos .csv que deseas subir a Edge Impulse
    files = [f for f in os.listdir() if f.startswith(base_csv_file_path) and f.endswith('.csv')]

    # Prepara los archivos para la solicitud
    prepared_files = []
    for file in files:
        prepared_files.append(('data', (os.path.basename(file), open(file, 'rb'), 'text/csv')))

    # Sube los archivos a Edge Impulse usando la API y imprime la respuesta.
    try:
        res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                            headers={
                                'x-label': label,
                                'x-api-key': api_key,
                            },
                            files=prepared_files)

        if res.status_code == 200:
            print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
        else:
            print('Failed to upload file(s) to Edge Impulse\n', res.status_code, res.content)
    finally:
        # Asegúrate de cerrar los archivos después de la solicitud
        for _, (filename, fileobj, _) in prepared_files:
            fileobj.close()

# Ejemplo de uso
txt_file_path = 'OpenBCI-RAW-mate'  # Nombre base del archivo de entrada
base_csv_file_path = 'OpenBCI-RAW-mate'  # Nombre base para los archivos CSV
api_key = 'ei_2ca87b66205a63e70dc1e865b95cc2ed6936283d4c829648ccc1d8b9fd14ec15'  # Clave API de Edge Impulse
label = 'eegPreg'  # Etiqueta para los datos

# Procesar y segmentar la señal EEG
txt_to_csv_first_window(txt_file_path, base_csv_file_path, window_size=2000)

# Subir los archivos CSV generados a Edge Impulse
upload_to_edge_impulse(base_csv_file_path, api_key, label)

```
### ECG
 </p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20ale/asistolia.png">
<h5 align="center">
  <i>Figura 1. Señal de ECG de un paciente con asistolia </i></div>
<br /> </p>
</h5>


</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20ale/ECG_REPOSO.png">
<h5 align="center">
  <i>Figura 3. Señal de ECG en un paciente en respoo</i></div>
<br /> </p>
</h5>

### EEG
</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20ale/ej%20mate.png">
<h5 align="center">
  <i>Figura 4. Señal de EEG tras realizar un ejercicio matemático </i></div>
<br /> </p>
</h5>

</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20ale/EEG_REPOSO.png">
<h5 align="center">
  <i>Figura 5. Señal de EEG en reposo </i></div>
<br /> </p>
</h5>
    
### EMG

</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20ale/oposicion.png">
<h5 align="center">
  <i>Figura 6. Señal EMG en haciendo oposición </i></div>
<br /> </p>
</h5>

</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20ale/EMG_REPOSO.png">
<h5 align="center">
  <i>Figura 7. Señal ENG en reposo </i></div>
<br /> </p>
</h5>
<h2 style = "text-align: center;">Links de proyecto</h2>

1. [IMMPULSE EDGE - EMG](https://studio.edgeimpulse.com/public/431202/live)</p>
2. [IMMPULSE EDGE - ECG](https://studio.edgeimpulse.com/public/431204/live)</p>
3. [IMMPULSE EDGE - EEG](https://studio.edgeimpulse.com/public/431206/live)</p>
