# Laboratorio N°8 - Procesamiento de señales ECG
## **Tabla de contenidos**
1. [Introducción](#introduccion)\
   1.1 [Marco teórico](#marco)
2. [Objetivos](#objetivos)
3. [Metodología](#metodologia)\
   3.1 [Materiales y equipos](#materiales)\
   3.2 [Procedimiento](#adquisicion)
4. [Resultados](#resultados)
5. [Archivos](#archivos)
6. [Discusión](#discusion)
7. [Referencias bibliográficas](#referencias)

<a name="introduccion"></a>
## **INTRODUCIÓN**
### **CONTEXTO**




<a name="marco"></a>
### **MARCO TEÓRICO**


<a name="objetivos"></a>
## OBJETIVOS
* Investigar literatura científica sobre técnica de procesamiento de señales electrocardiográficas (ECG).
* Identificar e implementar la mejor técnica filtrado para eliminar el ruido de las señales ECG.
* Implementar un proceso de segmentación de las señales ECG.
* Extraer características relevantes de las señales ECG en diferentes dominios.

<a name="metodologia"></a>
## METODOLOGÍA 
Para este laboratorio, se utilizarán datos de señales ECG adquiridas por el BITalino en la sesión de laboratorio 04. El proceso de adquisición se llevó a cabo siguiendo un protocolo estándar utilizando el dispositivo BITalino y el programa OpenSignal. Inicialmente, se estableció la conexión entre el BITalino y OpenSignal mediante Bluetooth para visualizar las señales en tiempo real. Luego, se conectó el sensor ECG de 3 electrodos al BITalino para comenzar la adquisición de señales.

<a name="materiales"></a>
### 1. MATERIALES Y EQUIPOS

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|-|**Laptop o PC**: Laptop equipada con el programa Python, para poder implementar ahí el código, para realizar los respectivos filtrados|1|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

<a name="adquisicion"></a>
### 2. PROCEDIMIENTO
Siguiendo las indicaciones de la guía BITalino (r)evolution Lab Guide 2021 proporcionada por PLUX-Wireless Biosignals <sup>[5](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>, se implementaron tres protocolos para medir la actividad eléctrica cardíaca en diferentes estados: estado de reposo, estado de respiración prolongada y estado de ejercicio intensivo. Los electrodos se colocaron de acuerdo con las especificaciones del protocolo, garantizando una captura precisa de las señales ECG para realizar la configuración bipolar de Einthoven de la siguiente manera:

* **IN+** (electrodo positivo/rojo) se coloca en la muñeca izquierda .
* **IN-** (electrodo negativo/negro) se coloca en la muñeca derecha.
* **REF** (electrodo de referencia/blanco) se coloca en la cresta ilíaca, debido a que representa una zona de baja interferencia electromagnética.
  
**a. Actividad eléctrica en estado de reposo**: Durante esta prueba, se registró la actividad eléctrica cardíaca del sujeto de prueba en una posición estable y manteniendo la calma. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Actividad eléctrica en estado de respiración prolongada**: El sujeto mantuvo la respiración por 30 segundos y se registró la señal durante la inspiración, mantención y expiración. El registro de la señal fue grabado por 30 segundos. Esta ubicación del electrodo permitió una colocación cómoda y no intrusiva durante las mediciones, lo que resulta beneficioso para evaluar la función cardíaca.

**a. Actividad eléctrica en estado de ejercicio intensivo**: Durante esta prueba, se registró la actividad eléctrica del sujeto de prueba al realizar la actividad física de 10 burpees por 3 minutos y la señal fue registrada durante y después de la actividad realizada. El registro de la señal fue grabado por 30 segundos..

#### DATOS ADQUIRIDOS EMG

En este laboratorio, nos enfocaremos en el análisis y la interpretación de las características de las señales ECG previamente adquiridos, como los picos de la onda R y la variabilidad de la frecuencia cardíaca (HRV). Las señales registradas durante los estado serán utilizadas para el análisis respectivo y así poder extraer conclusiones relevantes sobre la actividad cardíaca de diferentes estados del paciente en diferentes condiciones experimentales. Asimismo, para el cálculo del HRV y parte del procesamiento de la señal se utilizó un artículo de referencia que presentaba un enfoque en tiempo real del análisis del HRV <sup>[6]()</sup>.

#### Pre-procesamiento de la señal
- **Filtrado**

Se aplicó un filtro pasa banda con frecuencias de corte de 0.5Hz para frecuencia inferior y 40 Hz para superior. Estas fueron implementadas para eliminar la línea base, evitar el ruido de alta frecuencia generado por artefactos como la presencia de la actividad muscular no deseada. Este filtrado permitió mejorar la calidad de las señales ECG al eliminar el ruido no deseado y así facilitar la detección de pico. Asimismo, se aplicó filtro de segundo orden Butterworth con frecuencia de 5 a 15 Hz, así como la implementación de filtro Blackman y Wavelet como se ha estudiado en laboratorios pasados.

- **Segmentación**

Las señales de voltaje se segmentaron y anotaron en los puntos P, Q, R, S y T, que corresponden a diferentes intervalos de despolarización/repolarización atrial/ventricular, lo cual resulta relevante para el análisis de la señal al conocer sus características principales.

#### Detección de picos en onda R y cálculo del HRV

##### Análisis en tiempo real

Para la detección de los picos R, se utilizará un algoritmo de detección del complejo QRS (ref) y, una vez localizados, se construirá un algoritmo para la extracción de características. En el análisis en tiempo real, se utilizará un umbral calculado de manera iterativa con los primeros segundos de la señal ECG para el cálculo del umbral inicial. Cada segmento de cinco segundos se utilizará para actualizar los valores máximo y mínimos de la señal ECG y ajustar los umbrales de detección de picos R.

Asimismo, se utilizará el mecanismo de ventana deslizante para el cálculo de los índices HRV en tiempo real. Las ventanas se solaparon lo cual permite observar las características extraidas y brindar información de la variación de los índices. Cada ventana contiene 30 segundos de la señal ECG para el análisis temporal.

<div align="center">

|  **Nombre**  | **Descripción** | **Fórmula** |
|:------------:|:---------------:|:------------:|
|minRR|Mínimo intervalo RR|-|
|maxRR|Máximo intervalo RR|-|
|avgRR|Promedio de los intervalos RR|-|
|SDNN|Desviación estándar de los intervalos RR|$SDNN = \sqrt{\frac{1}{N-1} (\sum_{i=1})^{N} (RR_i - \overline{RR})^2}$, donde $\(RR_i\)$ es cada intervalo RR y $\(\overline{RR}\)$ es el promedio de todos los intervalos RR.|
|rmsSD|Raíz cuadrada media de las diferencias sucesivas|$\text{rmsSD} = \sqrt{\frac{(\sum_{i=1})^{N-1} (RR_{i+1} - RR_i)^2}{N-1}}$, donde $\(RR_{i+1} - RR_i\)$ representa la diferencia entre intervalos RR sucesivos|
|NN20|Número de intervalos RR donde la diferencia con el intervalo RR previo es mayor a 20 ms|$\text{NN20} = \sum_{i=1}^{N-1} \text{I}(RR_{i+1} - RR_i) > 20 \text{ms})$|
|avg IHR|Promedio de la frecuencia cardíaca instantánea (IHR)|$\text{avg IHR} = \frac{1}{\overline{RR}} \times 60$|
|pNN20|Promedio de la frecuencia cardíaca instantánea (IHR)|$\text{avg IHR} = \frac{1}{\overline{RR}} \times 60$|
|NN50|Promedio de la frecuencia cardíaca instantánea (IHR)|$\text{avg IHR} = \frac{1}{\overline{RR}} \times 60$|
|std IHR|Promedio de la frecuencia cardíaca instantánea (IHR)|$\text{avg IHR} = \frac{1}{\overline{RR}} \times 60$|
|SD1|Promedio de la frecuencia cardíaca instantánea (IHR)|$\text{avg IHR} = \frac{1}{\overline{RR}} \times 60$|
|SD2|Promedio de la frecuencia cardíaca instantánea (IHR)|$\text{avg IHR} = \frac{1}{\overline{RR}} \times 60$|

<p align="center"><i>Tabla 2. Parámetros del análisis estadístico y geométrico en tiempo real</i></p>
</div>

##### Análisis de frecuencias

El método de Lomb-Scargle se utilizó para convertir las señales HRV al dominio de frecuencia, dado que la serie temporal de los intervalos RR tiene un periodo de muestreo irregular. Este método generó un "estimador de espectro de potencia tipo Fourier" basado en el método de mínimos cuadrados, donde se determinó el sinusoide que mejor se ajusta a los datos para cada componente de frecuencia elemental. Se calcularon las potencias en las bandas de baja frecuencia (LF: 0.04-0.15 Hz) y alta frecuencia (HF: 0.15-0.40 Hz), las cuales proporcionan información sobre los componentes autónomos de la variabilidad de la frecuencia cardíaca. Asimismo, para el análisis en el dominio de frecuencia, se utilizó una ventana deslizante con una duración mínima de 2 minutos, garantizando una resolución suficiente para distinguir los componentes elementales del espectro en las diferentes bandas, ya que ventanas más cortas resultan en resoluciones frecuenciales insuficientes.

<a name="resultados"></a>
## RESULTADOS
### Estado de reposo
#### Detección de picos R

<div align="center">

|  **Señal Original vs Filtrada** | **Picos identificados** |
|:------------:|:---------------:|
|<image width="400" height="200" src="">|20|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

#### Resultados de HRV

<div align="center">

|  **Parámetro**  | **Resultado** |
|:------------:|:---------------:|
|minRR|[0.652, 0.656, 0.675, 0.69, 0.674]|
|maxRR|[0.686, 0.699, 0.766, 0.784, 0.719]|
|avgRR|[0.663, 0.6704000000000001, 0.7145, 0.73775, 0.6985999999999999]|
|SDNN|[0.012263767773404724, 0.01595744340425493, 0.033410327744576224, 0.038512173400108214, 0.015806327846783368]|
|rmsSD|[0.012509996003196817, 0.02100595153759995, 0.03970306453327414, 0.0565714886964568, 0.02808469333996719]|
|NN20|[1, 2, 3, 2, 3]|
|avg IHR|[90.52809798133592, 89.54854362370327, 84.15506002334973, 81.5510753403186, 85.93032476528307]|
|pNN20|[0.2, 0.4, 0.75, 0.5, 0.6]|
|NN50|[0, 0, 0, 1, 0]|
|pNN50|[0.0, 0.0, 0.0, 0.25, 0.0]|
|std IHR|[1.641457403170214, 2.0898853571466387, 3.8577380563454136, 4.2677565146159635, 1.9568682579356798]|
|SD1|[0.007079901129253154, 0.014468716252660383, 0.023211587144738213, 0.03784324392954592, 0.01979504357156101]|
|SD2|[0.007079901129253154, 0.014468716252660383, 0.023211587144738213, 0.03784324392954592, 0.01979504357156101]|


<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

#### Análisis de frecuencia

<div align="center">

|  **Ventana**  | **Resultado** |
|:------------:|:---------------:|
|Window_1|('LF": 0.15, "HF: 0.4)|
|Window_2|('LF": 0.15, 'HF': 0.4)|
|Window_3|('LF": 0.15, 'HF': 0.4)|
|Window_4|('LF": 0.15, 'HF': 0.4)|
|Window_5|('LF": 0.15, 'HF': 0.4)|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

### Estado de respiración prolongada

#### Detección de picos R

<div align="center">

| **Etapa** | **Señal Original vs Filtrada** | **Picos identificados** |
|:------------:|:---------------:|:---------------:|
|Inhalación|<image width="400" height="200" src="">|17|
|Exhalación|<image width="400" height="200" src="">|13|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

#### Resultados de HRV
##### Etapa de inhalación

<div align="center">
   
|  **Parámetro**  | **Resultado** |
|:------------:|:---------------:|
|minRR|[0.72, 0.632, 0.632, 0.664]|
|maxRR|[0.819, 0.778, 0.684, 0.71)|
|avgRR|[0.7825, 0.7022, 0.6572, 0.6898000000000001]|
|SDNN|[0.03761980861195336, 0.047641998278829575, 0.02114142852316278, 0.01802664694278996]|
|rmsSD|[0.04453463071962463, 0.04112784944535761, 0.03060637188560581, 0.0174785582929485]|
|NN20|(2, 3, 2, 1)|
|avg IHR|[76.86300038771995, £5.8386753670258, 91.39144576194663, 87.0417384426306]|
|pNN20|[0.5, 0.6, 0.4, 0.2]|
|NN50|[1, 2, 1, 0]|
|pNN50|[0.25, 0.4, 0.2, 0.01]|
|std IHR|([3.863839588497346, 5.807726151226807, 2.954753630489605, 2.2963211155921464]|
|SD1|[0.024861840461058195, O-013402425153680245, 0.021554436398235146, 0.010799305533227568]|
|SD2|[O.024861840461058195, 0.013402425153680245, 0.021554436898235146, 0.010799305533227568]|


<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

##### Etapa de exhalación

<div align="center">
   
|  **Parámetro**  | **Resultado** |
|:------------:|:---------------:|
|minRR|[0.781, 0.717, 0.65, 0.616]|
|maxRR|[0.821, 0.821, 0-73, 0.668]|
|avgRR|[0.0009999999099999, 0.7612, 0.6902, 0.6384000000000001]|
|SDNN|[0.019999999999999962, 0.03718279171815075, 0.029761720380381218, 0.019241621553289127]|
|rmsSD|[0.039999999999999925, 0.027721832551259208, 0.02108316864220799, 0.014212670403551907]|
|NN20|[1, 3, 1, 0]|
|avg IHR|[74.95309503110449, 79.00804372660010, 87.093079526112, 94.06974599740907]|
|pNN20|[0.5, 0.6, 0.2, 0.0]|
|NN50|[0, 0, 0, 0]|
|pNN50|[0.0, 0.0, 0.0, 0.0]|
|std IHR|[1.8714880357329449, 3.793042815738271, 3.1530155929914075, 2.8137066084617717]|
|SD1|[0.0, 0.006800735254367698, 0.004716990566028274, 0.004062019202317984]|
|SD2|[0.0, 0.006800735254367698, 0.004716990566028274, 0.004062019202317984]|


<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

#### Análisis de frecuencia
##### Etapa de inhalación

<div align="center">

|  **Ventana**  | **Resultado** |
|:------------:|:---------------:|
|Window_1|("LF": 0.15, "HP": 0.4)|
|Window_2|("LF": 0.15, "HP": 0.4)|
|Window_3|("LF": 0.15, "HE": 0.4)|
|Window_4|("LF": 0.15, "HF": 0.4)|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

##### Etapa de exhalación

<div align="center">

|  **Ventana**  | **Resultado** |
|:------------:|:---------------:|
|Window_1|("LF": 0.15, "HF": 0.4)|
|Window_2|("LF": 0.15, "HF": 0.4)|
|Window_3|("LF": 0.15, "HF": 0.4)|
|Window_4|("LF": 0.15, "HF": 0.4)|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

### Estado de ejercicio intensivo
#### Detección de picos R

<div align="center">

|  **Señal Original vs Filtrada** | **Picos identificados** |
|:------------:|:---------------:|
|<image width="400" height="200" src="">|12|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

#### Resultados de HRV

<div align="center">

|  **Parámetro**  | **Resultado** |
|:------------:|:---------------:|
|minRR|[0.525, 0.525, 0.469, 0.447]|
|maxRR|[1.745, 1.697, 0.923, 0.923]|
|avgRR|[1 1013333333322225, 1.OBS3323233333335, 0.623333332222234, 0.549]|
|SDNN|[0.5003334443704074, 0.4790410721010647, 0.21192010490129040, 0.18736160231524925]|
|rmsSD|[0.9347408731835792, 0.5910372238700368, 0.3147268657105714, 0.325443927582003]|
|NN20|[2, 2, 1, 2]|
|avg IHR|[68.89891591470571, 69.22310169341851, 106.15339979773631, 118.46309571014459]|
|pNN20|[0.66666666666666666, O.666666666666666666, 0.333333333333333, 0.4]|
|NN50|[2, 2, 1, 2]|
|pNN50|[0.66666666666666666, O.666666666666666666, 0.333333333333333, 0.4]|
|std IHR|[33.513384803489444, 33.180998090993666, 29.11263055479281, 26.927044643901976]|
|SD1|[0.6112938123357703, 0.05444722215136417, 0.15414927029066737, 0.2300583405770512]|
|SD2|[0.6112938123357103, 0.05444722215136417, 0.15414921829866737, 0.2300583485770512]|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

#### Análisis de frecuencia

<div align="center">

|  **Ventana**  | **Resultado** |
|:------------:|:---------------:|
|Window_1|("LF": 0.15, "HF": 0.4)|
|Window_2|("LF": 0.15, "HF": 0.4)|
|Window_3|("LF": 0.15, "HF": 0.4)|
|Window_4|("LF": 0.15, "HF": 0.4)|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>


<a name="archivos"></a>
## ARCHIVO DE LA SEÑAL PLOTEADA EN PYTHON
* **Codigo**
  - [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/tree/df24f30fb5e09ca55f7570ee885619f6fd250f00/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Codigos)

<a name="discusion"></a>
## Discusión


<a name="referencias"></a>
## REFERENCIAS BIBLIOGRÁFICAS
