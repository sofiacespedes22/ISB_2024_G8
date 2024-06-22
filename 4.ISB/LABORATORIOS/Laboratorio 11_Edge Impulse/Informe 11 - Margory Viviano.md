<h1 style="text-align: center;">Laboratorio 11: Edge impulse (EI)</h1>
Integrante: 
- Margory Viviano Salvatierra

<a id = "Informe edge impulse" style></a>
<h2 style = "text-align: center;">Objetivos</h2>
- Crear un proyecto en EI por cada señal trabaja en clases; es decir, para EMG, ECG, EEG. <br />
- Subir cada señal mediante un código en python a EI.<br />

<h2 style = "text-align: center;">Código en python</h2>
1. Codigo de python: 

```python
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
                window_data.append([timestamp, columns[5]])  # Añadir el timestamp y el valor de ECG
                timestamp += 1  # Incrementar el timestamp por 1 ms
                if len(window_data) == 750:
                    # Crear el archivo CSV para la ventana actual de datos
                    csv_file_path = f"{base_csv_file_path}window{window_count}.csv"
                    with open(csv_file_path, 'w', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(['timestamp', 'ecg'])  # Escribir los encabezados
                        csv_writer.writerows(window_data)  # Escribir las filas de datos
                    window_count += 1
                    window_data = []  # Reiniciar los datos de la ventana

        # Si hay datos restantes en la última ventana incompleta, escribirlos también
        if window_data:
            csv_file_path = f"{base_csv_file_path}window{window_count}.csv"
            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['timestamp', 'ecg'])  # Escribir los encabezados
                csv_writer.writerows(window_data)  # Escribir las filas de datos

# Ejemplo de uso
txt_file_path = 'reposo_prueba1.txt'
base_csv_file_path = 'ECG_REPOSO'
txt_to_csv_first_window(txt_file_path, base_csv_file_path)

api_key = 'ei_bee770b899359a30ce3068f78c7d5830fa14f61eff0ba9295ce35b727ebe4a32'

# Agrega los archivos .csv que deseas subir a Edge Impulse
files = [f for f in os.listdir() if f.startswith(base_csv_file_path) and f.endswith('.csv')]

# Reemplaza la etiqueta con la tuya propia.
label = 'ECG_REPOSO'

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
<h2 style = "text-align: center;">Links de proyecto</h2>

1. [IMMPULSE EDGE - EMG](https://studio.edgeimpulse.com/public/431212/live)</p>
2. [IMMPULSE EDGE - ECG](https://studio.edgeimpulse.com/public/431207/live)</p>
3. [IMMPULSE EDGE - EEG](https://studio.edgeimpulse.com/public/431213/live)</p>

<h2 style = "text-align: center;">Imagenes</h2>

### ECG
</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/db8a6aed-9f4c-40b8-a0c0-65852cdea8a3">
<p align="center"><i>Figura 1. Reposo </i></p>
</div>


</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/a10b2bdd-cbd5-4002-89ba-cd5b53c9c624">
<p align="center"><i>Figura 2. Aguantando la respiración </i></p>
</div>


</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/6e5df31b-8cba-492f-ae49-a66916712afc">
<p align="center"><i>Figura 3. Haciendo el ejercicio </i></p>
</div>


</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/5be3f095-d6b1-40b3-8d02-eda65195d029">
<p align="center"><i>Figura 4. Exhalación </i></p>
</div>

### EEG
</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/232a444b-094c-4694-acf3-ebd96d5635ba">
<p align="center"><i>Figura 5. Pulgar </i></p>
</div>


</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/08a23fd1-5960-4021-a19c-a4aee6b6ad83">
<p align="center"><i>Figura 6. Biceps </i></p>
</div>
    
### EMG
</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/cbf592b0-c528-4d5f-9f07-a1837d072349">
<p align="center"><i>Figura 7. Reposo 1 </i></p>
</div>


</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/5c8dc14c-3e7a-4896-becb-bd0ef46c50a4">
<p align="center"><i>Figura 8. Abriendo y cerrando los ojos </i></p>
</div>


</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/d0967a14-1ad5-42b9-8386-cd8dccd329f8">
<p align="center"><i>Figura 9. Reposo 2 </i></p>
</div>


</div>
<p align="center">
<image width="500" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/4cf7de3a-b665-4919-9bb6-75b270de5b2c">
<p align="center"><i>Figura 10. Ronda de preguntas </i></p>
</div>
