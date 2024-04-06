# Informe 01 de Laboratorio - Ploteo de señales en Arduino
## Tabla de contenidos
1. [Lista de participantes](#lista)
2. [Objetivos](#objetivos)
3. [Materiales y Equipos](#materiales)
4. [Entregables](#entregables)
5. [Metodología](#metodologia)
   - [Configuración inicial de los equipos](#conec1)
   - [Conexión del arduino nano 33 IoT](#conec2)
6. [Resultados y discusión](#resultados)
   - [Señal sinusoidal](#sinusoidal)
   - [Señal cuadrada](#cuadrada)
   - [Señal rampa](#rampa)
   - [Señal pulso](#pulso)
   - [Fuentes de error](#error)
7. [Referencias bibliográficas](#referencias)

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
   
|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
| AFG1022 | Generador de señales | 1 | <image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/f77e565c-b14c-4dd4-9bf5-9d63af9b054d"> | 
 | TBS 1000C Series | Osciloscopio digital | 1 | <image width="200" height="150" src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/d422cbc6-285c-483d-ab3b-eb10b246ac21"> 
| SAMD | Arduino 33 IoT | 1 | <image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/9bb89063-e51a-4ef1-9764-a4d6ffc2710a"> |
| - | Cable BNC M-M | 1 | <image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1030c4cf-863e-4986-9043-51f2ef09e90b"> |
| - | Punta de osciloscopio con conector BNC (Male) | 1 | <image width="200" height="150" src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/dd841cab-94c3-40ba-b2f6-3f165949aa44"> |
| - | Par de cables M-M | 1 | <image width="200" height="150" src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ba69efad-205a-4ae4-a563-0e8fd357f851"> |
| - | Condensador | 1 | <image width="200" height="150" src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2648872d-9dde-41ce-a7b8-81f828d5d3e6"> |
| - | Protoboard | 1 | <image width="200" height="150" src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8a071497-cdd1-4dbc-bbfc-a00e4cfc48b5">

</div>
<p align="center"><i>Tabla 1. Materiales y equipos utilizados para el ploteo de señales</i></p>

<a name="entregables"></a>
## Entregables
- Plotear al menos 3 señales en Arduino IDE provenientes del generador de señales.
- Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio.
- Graficar en Arduino cloud.

<a name="metodologia"></a>
## Metodología
<a name="conec1"></a>
### 1. Configuración inicial de los equipos
<div align="justify">

Antes de comenzar con la práctica de laboratorio, se configuró el generador de señales y el osciloscopio. El generador de señales fue configurado inicialmente para proporcionar una señal sinusoidal de 1 kHz de frecuencia, con 3V de amplitud y 0V de offset. Tras la configuración, se conectó el cable BNC entre los puertos del canal 1 tanto del generador de ondas como del osciloscopio, como se observa en la Figura 1.

<image width="200" height="150" src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/0561535c-8e5e-4988-8c1d-482a538f316a"> 
</div>
<image src ="|https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8a071497-cdd1-4dbc-bbfc-a00e4cfc48b5">
<p align="center"><i>Figura 1. Configuración del generador de ondas para el ploteo de señales</i></p>

<div align="justify">
  
A partir del uso de los cursores y controles de posición vertical, horizontal y disparo se ajustó la visualización de la señal sinusoidal, considerando la escala en la que se encontraba la sonda. Se mostró las medidas de amplitud y periodo de la señal con el uso de estos cursores, como se observa en la Figura 2.

</div>

<p align="center"><i>Figura 2. Señal sinusoidal visualizada en el osciloscopio para el ploteo de señales</i></p>
<a name="conec2"></a>
### 2. Conexión del arduino nano 33 IoT 
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
<p align="center"><i>Tabla 2. Parámetros considerados para el ploteo de señales</i></p>

<a name="resultados"></a>
## Resultados y discusión
<div align="justify">
En el presente informe, se generaron diferentes tipos de señales (sinusoidal, cuadrada, rampa y pulso) considerando los parámetros de frecuencia y voltaje observados en la Tabla 2 y fueron visualizadas en el ploteo de Arduino SAMD y en el osciloscopio. 

Primero, se realizó una prueba para determinar el efecto del ruido generado en la señal a partir de su visualización en el ploteo en Arduino. El primer resultado se evidencia en la Figura 4a, la cual muestra lo que se capturó cuando se apagó el generador de señales, en la que el Arduino solo pudo detectar el ruido ambiental presente. Posteriormente, al encender el generador de señales y utilizar un circuito que incluye un filtro RC, se logró modificar la señal de manera significativa, como se ilustra en la Figura 4b. Al remover el capacitor del circuito, como se muestra en la Figura 5, la señal adquirió una forma más cercana a una onda sinusoidal. Sin embargo, se observa una cantidad considerable de ruido en los bordes de la señal.
</div>
<p align="center"><i>Figura 4. Señal obtenida para la prueba preliminar</i></p>
<p align="center"><i>Figura 5. Señal obtenida de onda recortada (sin capacitor)</i></p>

<div align="justify">
Luego de dichas pruebas iniciales, se realizó la comparación de las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio para los cuatro tipos de señales: sinusoidales, cuadradas, rampas y pulsos. Asimismo, evaluó el comportamiento del filtro RC junto a la señal obtenida, por lo que se ploteo en el Arduino IDE las 4 señales provenientes del generador.
</div>
<a name="sinusoidal"></a>
### Señal sinusoidal
<p align="center"><i>Figura 6. Señal sinusoidal - Voltaje: 1.5V , Frecuencia: 3Hz</i></p>
<a name="cuadrada"></a>
### Señal cuadrada
<p align="center"><i>Figura 7. Señal cuadrada - Voltaje: 1.5V , Frecuencia: 3Hz</i></p>
<a name="rampa"></a>
### Señal rampa
<p align="center"><i>Figura 8. Señal rampa - Voltaje: 1.5V , Frecuencia: 3Hz</i></p>
<a name="pulso"></a>
### Señal pulso
<p align="center"><i>Figura 9. Señal pulso - Voltaje: 1.5V , Frecuencia: 3Hz</i></p>

<div align="justify">
Podemos observar a partir de la comparación que existen diferencias significativas entre las señales graficadas pues si bien las graficadas en el Arduino IDE presenta las formas deseadas, no llegan a ser las requeridas. A continuación, hemos considerado las siguientes fuentes de error como motivos de las diferencias evidenciadas: 
</div>

<a name="error"></a>
### Fuentes de error

<a name="referencias"></a>

## Referencias bibliográficas
