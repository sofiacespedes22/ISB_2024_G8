# Laboratorio N°8 - Procesamiento de señales ECG
## **Tabla de contenidos**
1. [Introducción](#introduccion)\
   1.1 [Marco teórico](#marco)
2. [Objetivos](#objetivos)
3. [Metodología](#metodologia)\
   3.1 [Materiales y equipos](#materiales)\
   3.2 [Procedimiento](#adquisicion)
4. [Resultados](#resultados)\
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
 - **Datos Adquiridos Previamente**

Para este laboratorio, se utilizarán datos de señales ECG adquiridas por el BITalino en la sesión de laboratorio 04. El proceso de adquisición se llevó a cabo siguiendo un protocolo estándar utilizando el dispositivo BITalino y el programa OpenSignal. Inicialmente, se estableció la conexión entre el BITalino y OpenSignal mediante Bluetooth para visualizar las señales en tiempo real. Luego, se conectó el sensor ECG de 3 electrodos al BITalino para comenzar la adquisición de señales.
 
 - **Procedimiento de Adquisición Anterior**

Siguiendo las indicaciones de la guía BITalino (r)evolution Lab Guide 2021 proporcionada por PLUX-Wireless Biosignals <sup>[5](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf)</sup>, se implementaron tres protocolos para medir la actividad eléctrica cardíaca en diferentes estados: estado de reposo, estado de respiración controlada, estado de descanso y estado post-ejercicio. Los electrodos se colocaron de acuerdo con las especificaciones del protocolo, garantizando una captura precisa de las señales ECG.

**a. Actividad muscular del bíceps braquial (brazo)**: Durante esta prueba, se registró la actividad eléctrica del bíceps braquial en estados de reposo y ante la exposición de fuerzas con oposición o sin ella. Para ello, en el ensayo se empleó un electrodo de referencia en el codo para minimizar la interferencia eléctrica y el ruido.

**b. Actividad muscular del abductor corto del pulgar**: En esta serie de mediciones, se evaluó la actividad eléctrica del abductor corto del pulgar en estados de reposo, fuerza con oposición y sin oposición. Al igual que en la prueba anterior, se utilizó un electrodo de referencia en el codo para reducir la interferencia eléctrica. Esta ubicación del electrodo permitió una colocación cómoda y no intrusiva durante las mediciones, lo que resulta beneficioso para evaluar la función muscular.

#### DATOS ADQUIRIDOS EMG

En este laboratorio, nos enfocaremos en el análisis y la interpretación de los datos de señales EMG previamente adquiridos. Las señales registradas durante las actividades musculares se utilizarán para llevar a cabo análisis específicos y extraer conclusiones relevantes sobre la actividad muscular en el bíceps braquial y el abductor corto del pulgar en diferentes condiciones experimentales.

#### Filtrado, Segmentación y Extracción de Características de Señal EMG

Para esta sección se seleccionó un articulo de referencia <sup>[6](https://doi.org/10.18280/ts.390518)</sup>, en este se optimiza el procesamiento de señales EMG mediante técnicas de filtrado, segmentación y extracción de características. El mejor enfoque encontrado se describe brevemente a continuación:

- **Filtrado**

Se aplicó un filtro de rechazo de banda de 45-55Hz para eliminar la interferencia de la línea de alimentación, lo que ayudó a mejorar la calidad de las señales EMG al eliminar el ruido no deseado.

- **Segmentación**

Se utilizó un método de ventana deslizante con una longitud de ventana de 250 ms y un incremento de 64 ms para segmentar los datos EMG. Esta técnica permitió dividir las señales en intervalos más pequeños para un análisis más detallado.

- **Extracción de características**

Se exploraron varias técnicas de extracción de características, incluidas las características en el dominio del tiempo (como la media y la varianza, así como características específicas de EMG), características en el dominio de la frecuencia (obtenidas mediante la transformada de Fourier), y métodos en el dominio tiempo-frecuencia (como la transformada de Fourier de tiempo corto y la transformada Wavelet). Además, se propuso un nuevo método de extracción de características basado en los coeficientes AR de las regiones positivas y negativas de la señal.


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



<a name="resultados"></a>
## RESULTADOS


<a name="archivos"></a>
## ARCHIVO DE LA SEÑAL PLOTEADA EN PYTHON
* **Codigo**
  - [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/tree/df24f30fb5e09ca55f7570ee885619f6fd250f00/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Codigos)

<a name="discusion"></a>
## Discusión


<a name="referencias"></a>
## REFERENCIAS BIBLIOGRÁFICAS
