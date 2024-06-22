<h1 style="text-align: center;">Laboratorio 11: Edge impulse (EI)</h1>
Integrante: 

- Sofía Camila Céspedes Trece
  
<a id = "Informe edge impulse" style></a>
<h2 style = "text-align: center;">Objetivos</h2>
- Crear un proyecto en EI por cada señal trabaja en clases; es decir, para EMG, ECG, EEG. <br />
- Subir cada señal mediante un código en python a EI.<br />

<h2 style = "text-align: center;">Código en python</h2>
1. Codigo de python: 


a. [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/a831ccc509dd4bf71fdfe4905482f315d5469a03/4.ISB/LABORATORIOS/Laboratorio%2011_Edge%2IImpulse/Codigos/emg.py)</p>
b. [ECG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/a831ccc509dd4bf71fdfe4905482f315d5469a03/4.ISB/LABORATORIOS/Laboratorio%2011_Edge%20Impulse/Codigos/ecg.py)</p>
c. [EEG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/a831ccc509dd4bf71fdfe4905482f315d5469a03/4.ISB/LABORATORIOS/Laboratorio%2011_Edge%20Impulse/Codigos/eeg.py)</p>

``` python
import requests
import os
import csv

def txt_to_csv(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r') as txt_file, open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Escribir los encabezados
        csv_writer.writerow(['timestamp', 'ecg'])
        
        # Saltar las líneas de encabezado
        for line in txt_file:
            if line.startswith('#'):
                continue
            break  # La primera línea después del encabezado ya está leída
        
        timestamp = 0  # Inicializa el timestamp en 0
        
        # Escribir el resto de las líneas procesadas
        for line in txt_file:
            columns = line.strip().split('\t')  # Asumiendo que los valores están separados por tabulaciones
            if len(columns) >= 6:
                # Escribir el timestamp y la sexta columna (ECG)
                csv_writer.writerow([timestamp, columns[5]])
                timestamp += 1  # Incrementar el timestamp por 1 ms

# Ejemplo de uso
txt_file_path = 'ECG_Reposo1.txt'
csv_file_path = 'ECG_Reposo1.csv'
txt_to_csv(txt_file_path, csv_file_path)

api_key = 'ei_9fd00242dc38a411c3e476920d7355b834d92106ed48ffacbd46ed10769bd1e0'

# Agrega los archivos .csv que deseas subir a Edge Impulse
files = [
    'ECG_Reposo1.csv',
]

# Reemplaza la etiqueta con la tuya propia.
label = 'car'

# Prepara los archivos para la solicitud
prepared_files = []
for file in files:
    prepared_files.append(('data', (os.path.basename(file), open(file, 'rb'), 'text/csv')))

# Sube el archivo a Edge Impulse usando la API y imprime la respuesta.
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
<h2 style = "text-align: center;">Links de proyecto</h2>

1. [IMMPULSE EDGE - EMG](https://studio.edgeimpulse.com/public/431209/live)</p>
2. [IMMPULSE EDGE - ECG](https://studio.edgeimpulse.com/public/431174/live)</p>
3. [IMMPULSE EDGE - EEG](https://studio.edgeimpulse.com/public/431211/live)</p>

<h2 style = "text-align: center;">Imagenes</h2>

### ECG

</div>
<p align="center">
<image width="500" height="250"src="">
<p align="center"><i>Figura 1. Reposo </i></p>
</div>

</div>
<p align="center">
<image width="500" height="250"src="">
<p align="center"><i>Figura 2. Salto </i></p>
</div>

### EEG

</div>
<p align="center">
<image width="500" height="250"src="">
<p align="center"><i>Figura 3. Pulgar </i></p>
</div>

</div>
<p align="center">
<image width="500" height="250"src="">
<p align="center"><i>Figura 4. Bíceps </i></p>
</div>

### EMG

</div>
<p align="center">
<image width="500" height="250"src="">
<p align="center"><i>Figura 5. Ojos cerrados </i></p>
</div>

</div>
<p align="center">
<image width="500" height="250"src="">
<p align="center"><i>Figura 6. Preguntas </i></p>
</div>
