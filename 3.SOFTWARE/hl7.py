# Importar bibliotecas necesarias
import random

# Definir la función para generar datos ficticios de una señal ECG
def generar_datos_ecg(num_puntos):
    return [random.uniform(-1, 1) for _ in range(num_puntos)]

# Función para crear el mensaje HL7 modificado con datos de ECG
def crear_mensaje_hl7_modificado(datos_ecg):
    mensaje = (
        "MSH|^~\\&|SendingAPP|Sender Facility|Receiving APP|Receiving Facility|20220129041729^S|NO SECURITY|ORU^R01|2022012904172900001|T|2.3|00051||AL|\n"
        "PID|1|49120452|7337379446|234166342|Céspedes^Camila||19991101|F||Hispanic|244 Los Molles St^^Hermosa Beach^NY^916518712||(159) 052-1309|(214)555-1212X00019||||401585549515|644-11-8968|\n"
        "PV1|1|P|^^^00002|R||00019|8866423^Araujo^||^^^^^^^^||||||||||00111|\n"
        "DG1|1||I9|Arritmias ventriculares||W|||||||||01|6142326^Solomon^Bobby^L|\n"
        "OBX|1|NM|ECG^Electrocardiogram||{' '.join(map(str, datos_ecg))}"
    )
    return mensaje

# Función para guardar el mensaje HL7 en un archivo
def guardar_hl7_en_archivo(mensaje_hl7, nombre_archivo):
    with open(nombre_archivo, 'w') as file:
        file.write(mensaje_hl7)

# Generar datos ficticios de una señal ECG
num_puntos_ecg = 1000
datos_ecg = generar_datos_ecg(num_puntos_ecg)

# Crear el mensaje HL7 modificado con datos de ECG
mensaje_hl7_modificado = crear_mensaje_hl7_modificado(datos_ecg)

# Guardar el mensaje HL7 en un archivo
nombre_archivo = 'hl32_modificado_con_ecg.hl7'
guardar_hl7_en_archivo(mensaje_hl7_modificado, nombre_archivo)

print(f'Se ha generado el archivo {nombre_archivo} con el mensaje HL7 modificado que incluye datos de ECG.')
