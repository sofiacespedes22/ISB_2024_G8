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
<div align="center">
  
| Modelo | Descripción | Cantidad | Imagen |
| ------------- | ------------- | ------------- | -------------- |
| AFG1022 | Generador de señales | 1 | <image src =![Texto alternativo](7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg)> |
| TBS 1000C Series | Osciloscopio digital | 1 | <image src ="https://postimg.cc/qhSt0qq1"> |
| SAMD | Arduino 33 IoT | 1 | <image src="7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg"> |
| - | Cable BNC M-M | 1 | <image src="7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg"> |
| - | Punta de osciloscopio con conector BNC (Male) | 1 | <image src ="7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg"> | 
| - | Par de cables M-M | 1 | <image src ="7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg"> |
| - | Condensador | 1 | <image src ="7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg"> |
| - | Protoboard | 1 | <image src ="7. LABORATORIOS/Laboratorio 02_Ploteo de señales/Imagenes/Osciloscopio.jpeg"> |

</div>

<a name="entregables"></a>
## Entregables
- Plotear al menos 3 señales en Arduino IDE provenientes del generador de señales.
- Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio.
- Graficar en Arduino cloud.

<a name="metodologia"></a>
## Metodología
### Configuración inicial de los equipos
<div align="justify">

Antes de comenzar con la práctica de laboratorio, se configuró el generador de señales y el osciloscopio. El generador de señales fue configurado inicialmente para proporcionar una señal sinusoidal de 1 kHz de frecuencia, con 3V de amplitud y 0V de offset. Tras la configuración, se conectó el cable BNC entre los puertos del canal 1 tanto del generador de ondas como del osciloscopio, como se observa en la Figura 1.

</div>

<p align="center"><i>Figura 1. Configuración del generador de ondas para el ploteo de señales</i></p>

<div align="justify">
  
A partir del uso de los cursores y controles de posición vertical, horizontal y disparo se ajustó la visualización de la señal sinusoidal, considerando la escala en la que se encontraba la sonda. Se mostró las medidas de amplitud y periodo de la señal con el uso de estos cursores, como se observa en la Figura 2.

</div>

<p align="center"><i>Figura 2. Señal sinusoidal visualizada en el osciloscopio para el ploteo de señales</i></p>

### Conexión del arduino 33 IoT 
<div align="justify">
Se realizó la conexión del Arduino nano 33 IoT conectado al protoboard junto a un condensador formando un filtro RC con el cable BNC para evaluar la señal sinusoidal enviada desde el generador de señales, observado en la Figura 3. 
</div>
<p align="center"><i>Figura 3. Conexión Arduino nano 33 IoT y cable BNC para el ploteo de señales</i></p>
<div align="justify">
De manera paralela, se modificó el código en Arduino SAMD adjuntado por los docentes para que permita leer el puerto por el cual esta conectado al generador y la visualización de la gráfica generada. El código modificado se encuentra adjuntado en la carpeta “Código”. A continuación, se visualiza los parámetros considerados para el ploteo de las señales que se compararán en la siguiente sección (ver Tabla 1).
</div>
<div align="center">

| Parámetros | Valor | 
| ------------ | ------------ | 
| Frecuencia        | 3 hz    | 
| Voltaje    | 1.5 V    | 
| Offset    | 0 V   | 
| Capacitor    | 100 µF  | 

</div>
<p align="center"><i>Tabla 1. Parámetros considerados para el ploteo de señales</i></p>

<a name="resultados"></a>
## Resultados y discusión
<div align="justify">
Para esta primera parte de los resultados, se presenta en la Figura 1. la cual se obtuvo a que se apagó el generador de señales por lo que lo único que se podía leer en el arduino era el ruido generado. Sin embargo, luego al prender el generador de señales y mediante el circuito empleado, que consiste de un filtro RC, se pudo obtener un comportamiento en la señal como lo mostrado en la Figura 2. Y en el caso de la Figura 3. se extrajo el capacitor y esto ocasionó que la señal muestre un comportamiento de la onda sinusoidal; sin embargo los bordes como se puede ver señalan una presencia alta de ruido.
</div>
<a name="referencias"></a>

## Fuentes de error
## Referencias bibliográficas
