# Informe 01 de Laboratorio - Ploteo de señales en Arduino
## Tabla de contenidos
1. [Lista de participantes](#lista)
2. [Objetivos](#objetivos)
3. [Materiales y Equipos](#materiales)
4. [Entregables](#entregables)
5. [Metodología](#metodologia)
7. [Resultados y discusión](#resultados)
8. [Referencias bibliográficas](#referencias)

<a name="lista"></a>
## Lista de participantes
- Sofia Camila Céspedes Trece - 71738148
- Nicole Stefany Acuña Malpartida - 71400976
- Chris Margory Viviano Salvatierra - 75138288
- Harold Alonso Alemán Ramírez - 71386429
  
<a name="objetivos"></a>
## Objetivos
1. Adquirir señales conocidas como señal cuadrada, triangular, senoidal, rampa, etc.
2. Entender los criterios de selección de la frecuencia de muestreo.
3. Manipular y configurar adecuadamente una fuente de alimentación regulable; multímetro digital; Generador de señales y osciloscopio digital.
   
<a name="materiales"></a>
## Materiales y Equipos
| Modelo | Descripción | Cantidad | Imagen |
| ------------- | ------------- | ------------- | -------------- |
| AFG1022 | Generador de señales | 1 | <image src ="7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg"> |  

<a name="entregables"></a>
## Entregables
- Plotear al menos 3 señales en Arduino IDE provenientes del generador de señales.
- Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio.

<a name="metodologia"></a>
## Metodología
### Configuración inicial de los equipos
Antes de comenzar con la práctica de laboratorio, se configuró el generador de señales y el osciloscopio. El generador de señales fue configurado inicialmente para proporcionar una señal sinusoidal de 1 kHz de frecuencia, con 3V de amplitud y 0V de offset. Tras la configuración, se conectó el cable BNC entre los puertos del canal 1 tanto del generador de ondas como del osciloscopio, como se observa en la Figura 1.

A partir del uso de los cursores y controles de posición vertical, horizontal y disparo se ajustó la visualización de la señal sinusoidal, considerando la escala en la que se encontraba la sonda. Se mostró las medidas de amplitud y periodo de la señal con el uso de estos cursores, como se observa en la Figura 2.

### Conexión del arduino 33 IoT 
Se realizó la conexión del Arduino nano 33 IoT conectado al protoboard junto a un condensador formando un filtro RC con el cable BNC para evaluar la señal sinusoidal enviada desde el generador de señales, observado en la Figura 3. 

De manera paralela, se modificó el código en Arduino SAMD adjuntado por los docentes para que permita leer el puerto por el cual esta conectado al generador y la visualización de la gráfica generada. El código modificado se encuentra adjuntado en la carpeta “Código”.

<a name="resultados"></a>
## Resultados y discusión

<a name="referencias"></a>
## Referencias bibliográficas
