import numpy as np

# Iterar sobre los números del 1 al 81
for i in range(1, 82):
    # Construir los nombres de archivo para cada iteración
    base_filename = str(i)

    dat_file = base_filename + '.dat'

    txt_file = base_filename + '_signal.txt'  # Nombre del archivo de texto de salida

    try:
        # Leer datos desde el archivo .dat
        with open(dat_file, 'rb') as f:
            data = np.fromfile(f, dtype=np.int16)  # Suponiendo que los datos son int16, ajusta el dtype según sea necesario

        # Guardar los datos como texto en un archivo .txt
        np.savetxt(txt_file, data, fmt='%d')

        print(f"Datos guardados en {txt_file}")

    except FileNotFoundError:
        print(f"Error: Archivos no encontrados para {base_filename}")
    except Exception as e:
        print(f"Error al procesar {base_filename}: {str(e)}")
