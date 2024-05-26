# Laboratorio N°8 - Procesamiento de señales EMG
## **Tabla de contenidos**
1. [Introducción](#introduccion)\
   1.1 [Marco teórico](#marco)
2. [Objetivos](#objetivos)
3. [Metodología](#metodologia)\
   3.1 [Materiales y equipos](#materiales)\
   3.2 [Procedimiento](#adquisicion)
4. [Resultados](#resultados)\
   4.1 [Señal EEG](#eeg)
5. [Archivos](#archivos)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Referencias bibliográficas](#referencias)

  
<a name="introduccion"></a>
## **INTRODUCIÓN**
### **CONTEXTO**
Como sabemos la electromiografía (EMG), es el estudio que permite registrar señales eléctricas biomédicas que son obtenidas a través de actividades generadas por los músculos esqueléticos, estas señales mioeléctricas son generadas a partir de neuronas motoras, que forman parte del Sistema Nervioso Central (SNC) <sup>[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/)</sup>. En conclusión, una señal EMG es una señal biomédica que registra las corrientes eléctricas que son generadas por los músculos durante la contracción, representando actividades neuromusculares (_Figura 1_). 

</div>
<p align="center">
<image width="300" height="350" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/33febe45-7e95-4082-97aa-4bb7d851b23b">
<p align="center"><i>Figura 1. Relación entre el sistema nervioso central y el músculo [3] </i></p>
</div>


Actualmente, la EMG es una herramienta de gran utilidad, ya que se pueden utilizar para diagnóstico y monitoreo de lesiones musculares, daños a los nervios y disfunciones musculares que se pueden producir a trastornos neurológicos y musculares, con fines de investigación, para el análisis de la biomecánica de diversos movimientos y el análisis de la marcha, entre otros. <sup>[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/)</sup>.

La electromiografía (EMG) al tener tanta relevancia en el ámbito biomédico, requiere de un procesamiento de la señal antes de ser estudiada, ya que al ser al ser una señal que registra la actividad muscular, la cual es controlada por el sistema nervioso, hace que la EMG se vuelve una señal complicada de analizar. La señal EMG puede adquirir ruido mientras viaja por los diferentes tejidos, además de que si la EMG es tomada en la superficie de la piel puede recoger señales de diferentes unidades motoras a la vez. Es por ello, que un adecuado procesamiento de la señal EMG es de suma importancia para un correcto análisis de la misma. 


<a name="marco"></a>
### **MARCO TEÓRICO**
#### A. EMG
Proceso de registro de las actividades eléctricas musculares. Las actividades eléctricas musculares son realizadas bajo el control del cerebro, por lo tanto, están directamente relacionadas con el sistema nervioso. En el cerebro se produce un potencial de acción, el cual pasa a través de las fibras nerviosas, las cuales estimularán a las fibras musculares y las neuronas motoras trasmiten la señal logrando que el músculo se contraiga, generando una pequeña corriente eléctrica, la cual puede ser medida y registrada mediante EMG, y es mostrada en gráficos, sonidos y cuantificarla en valores numéricos <sup>[2](https://www.ijsrp.org/research-paper-0517/ijsrp-p6504.pdf)</sup> .Las señales EMG son señales no estacionarias, no lineales y complejas. <sup>[2](https://www.ijsrp.org/research-paper-0517/ijsrp-p6504.pdf)</sup>.

</div>
<p align="center">
<image width="500" height="180" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2b11a295-81ac-4f5b-9ae4-f85013bbe7a8">
<p align="center"><i>Figura 2. Señal EMG sin procesamiento [2] </i></p>
</div>

La amplitud de una señal EMG puede depender de varios factores, incluyendo la distancia que separa a los electrodos, el material de los electrodos y ruidos y “artefactos”.

#### B. ADQUISICIÓN
Para la adquisición de las señales EMG, se utilizan principalmente 2 tipos de electrodos: el electrodo de aguja (método invasivo) y los electrodos de superficie (método no invasivo) (_Figura 3_). Los electrodos de aguja se clasifican además en tres subtipos: los electrodos individuales monopolares, electrodos EMG de fibra única y electrodos EMG concéntricos; tienen aproximadamente 1 mm2 de ancho. Los electrodos de superficie, son de dos tipos: electrodos EMG gelificados y electrodos EMG secos; tienen entre 0.5 y 2.5 mm de ancho y como son colocados en la superficie de la piel, son no invasivos, estos electrodos detectan el cambio entre la superficie del músculo y la piel a través de la conducción electrolítica <sup>[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/)</sup> .

</div>
<p align="center">
<image width="230" height="250" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e442da38-c5bb-479c-b12d-5dd2702dcc1b">
<p align="center"><i>Figura 3. Tipos de electrodos para la adquisición de señales EMG [1] </i></p>
</div>


|  **Electrodo de superficie**  | **Electrodo de aguja (Invasivo)** |
|:------------:|:---------------:|
|<p align="justify">Se colocan sobre la piel del músculo que se desea medir.</p>|<p align="justify">Son electrodos intramusculares, estos deben ser insertados directamente en el músculo que se desea analizar, requiere de un especialista que supervise diche inserción.</p>|
|<p align="justify">La señal que se registre es el promedio de la actividad eléctrica de varias unidades motoras en el músculo.</p>|<p align="justify">Es posible solo obtener mediciones de una sola unidad motora.</p>|
|<p align="justify">Al ser colocados los electrodos en la superficie de la piel, al viajar por lo diferentes tejidos, presenta un alto nivel de ruido.</p>|<p align="justify">La cantidad de ruido es menor.</p>|

A continuación podemos observar (_Figura 4_) dos señales obtenidas, tanto en EMG intramuscular, es decir con aguja, y un EMG obtenido por electrodo de superficie. Aquí se puede observar que efectivamente las señales obtenidas con electrodos de superficie, presentan mayor ruido, por lo que se dificulta su análisis.
.

</div>
<p align="center">
<image width="450" height="250" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8f02ca47-3024-407c-8f02-5dee0b1d56a3">
<p align="center"><i>Figura 4. Señales obtenidas mediante EMG intramuscular y EMG superficial [3] </i></p>
</div>


En este laboratorio, nosotros estaremos analizando señales EMG adquiridas por electrodos de superficie, por lo tanto, es necesario que estas señales tengan un correcto procesamiento, para poder atenuar el ruido, producido por la propia adquisición y así poder luego realizar un mejor análisis


#### C. PROCESAMIENTO
Como mencionamos, para poder analizar correctamente las señales EMG obtenidas, se requiere de un procesamiento de estas señales, con el fin de eliminar el ruido. 

##### C.1. PRE-PROCESAMIENTO
Las señales obtenidas por electrodos de superficie, son señales bastante débiles y ruidosas, como se mencionó anteriormente, por lo que requiere adecuación antes de ser tratada. Por lo que primero la señal debe pasar por una etapa de amplificación <sup>[3](https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content)</sup>. Después de esta amplificación, se siguen los siguientes pasos:

* **Filtrado**: Se debe empezar con una etapa de filtración, ya que es esencial para reducir los artefactos en las señales EMG. Generalmente se necesita un filtro paso alto para que se puedan reducir efectos de artefactos correspondientes a movimientos en inestabilidad entre los electrodos de superficie y la piel, también se necesitarán filtros pasa bajo para registrar los datos que corresponden a estimulación muscular y eliminar interferencias de alta frecuencia, e incluso se puede utilizar filtro pasa banda <sup>[3](https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content)</sup>.  En algunos estudios, para poder filtrar la señal utilizaron filtros Butterworth con parámetros específicos o filtros pasa banda <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>. En este laboratorio utilizaremos el filtro que mejor nos haya dado resultado de los laboratorios anteriores de FIR e IRR. 
* **Rectificación**: Una de las técnicas más comunes para poder analizar la amplitud de una señal EMG es la rectificación. Las señales EMG adquieren valores positivos y negativos durante la contracción, lo que hace el proceso de rectificación es abordar la parte negativa de la señal. Para este proceso de rectificación, tenemos a los dos más comunes, que son la rectificación de onda completa y la de media onda <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>. En la rectificación de media onda, se excluyen los valores negativos y únicamente se consideran los valores positivos, mientras que en la rectificación de onda completa, se obtiene el valor absoluto de todos los valores, incluyendo los negativos <sup>[3](https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content)</sup>. 
* **Normalización**: La señales EMG varían de individuo en individuo, por lo que la normalización es un proceso que nos permite estandarizar la amplitud para poder comparar las señales entre diferentes sujetos. El proceso de normalización consiste en dividir las señales EMG obtenidas por un valore de señal EMG de referencia, ambas señales obtenida a las mismas condiciones, permitiendo una comparación más eficiente entre los individuos <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>.
* **Segmentación**: El proceso de segmentación consiste en dividir los datos muestreados, en segmentos para la posterior extracción de características. El tamaño de los segmentos debe ser lo suficientemente grande como para extraer adecuadamente las características de cada segmento y tener una mayor precisión de clasificación , pero la longitud de estos segmentos también debe ser pequeña para evitar cualquier retraso computacional en sistemas en tiempo real.

##### C.2. EXTRACCIÓN DE CARACTERÍSTICAS
En la extracción, lo que se busca es obtener información de la señal EMG, que sea relevante para su análisis, a través de una transformación de los datos originales, y de esta transformación se obtiene el vector de características. La extracción de características, no solo mejora el rendimiento del clasificador, sino que también es capaz de reducir la dimensionalidad, de forma que simplifique el procesamiento y la clasificación <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>. Entre las características que se pueden clasificar, están las siguientes tres:

* **Características en el dominio del tiempo**:
Las características del dominio del tiempo se evalúan en función de las variaciones de amplitud de la señal a lo largo del tiempo, eliminando la necesidad de más transformaciones y beneficiándose de su simplicidad y bajos requisitos de recursos computacionales <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>.

* **Características en el dominio de la frecuencia**:
Nos ayudan a identificar patrones específicos y poder identificar la activación para poder obtener información acerca de la modulación de la fuerza y de la velocidad de la contracción muscular. Las características del dominio de la frecuencia, a diferencia de las características del dominio del tiempo, no pueden derivarse directamente de datos sin procesar y se obtienen aplicando la transformada de Fourier a la señal. Estas características abarcan la densidad del espectro de potencia de la señal <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>.

* **Características en el dominio tiempo-frecuencia**:
Las herramientas de análisis en tiempo-frecuencia son capaces de darnos la información temporal de la cual se carece en el análisis espectral. Además, permite una mejor lectura e interpretación de las contracciones musculares <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>.

<a name="objetivos"></a>
## OBJETIVOS
* Investigar literatura científica sobre técnica de procesamiento de señales electromiográficas (EMG).
* Identificar e implementar la mejor técnica filtrado para eliminar el ruido de las señales electromiográficas (EMG).
* Implementar un proceso de segmentación de las señales electromiográficas (EMG).
* Extraer características relevantes de las señales electromiográficas (EMG) en diferentes dominios.

<a name="metodologia"></a>
## METODOLOGÍA 

En el proceso de procesamiento de señales EMG, el primer paso implica la búsqueda y revisión de al menos un artículo que aborde todos los aspectos relevantes para este propósito. En este reporte de laboratorio, se busca adquirir información esencial sobre técnicas de filtrado, métodos de segmentación y estrategias de extracción de características específicas para las señales EMG. Una vez seleccionado el recurso adecuado, se realizará la posterior aplicación de técnicas de filtrado para eliminar el ruido y las interferencias no deseadas de las señales EMG. Para luego continuar con el proceso de segmentación, dividiendo las señales en intervalos discretos para un análisis más detallado y llegar, finalmente, a la extracción de características relevantes de las señales segmentadas, identificando patrones y atributos útiles para su posterior análisis y aplicación en diversas aplicaciones biomédicas. 
 
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
#### Procedimiento de Utilización de Señales EMG
	
 - **Datos Adquiridos Previamente**

Para este laboratorio, se utilizarán datos de señales EMG adquiridos en sesiones de laboratorio anteriores. El proceso de adquisición se llevó a cabo siguiendo un protocolo estándar utilizando el dispositivo BITalino y el programa OpenSignal. Inicialmente, se estableció la conexión entre el BITalino y OpenSignal mediante Bluetooth para visualizar las señales en tiempo real. Luego, se conectó el sensor EMG de 3 electrodos al BITalino para comenzar la adquisición de señales.
 
 - **Procedimiento de Adquisición Anterior**

Siguiendo las indicaciones de la guía BITalino (r)evolution Lab Guide 2021 proporcionada por PLUX-Wireless Biosignals <sup>[x0](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf)</sup>, se implementaron tres protocolos para medir la actividad muscular en diferentes músculos: el bíceps braquial y el abductor corto del pulgar. Los electrodos se colocaron de acuerdo con las especificaciones del protocolo, garantizando una captura precisa de las señales EMG en reposo, sin oposición y con oposición para ambos músculos.

**a. Actividad muscular del bíceps braquial (brazo)**: Durante esta prueba, se registró la actividad eléctrica del bíceps braquial en estados de reposo y ante la exposición de fuerzas con oposición o sin ella. Para ello, en el ensayo se empleó un electrodo de referencia en el codo para minimizar la interferencia eléctrica y el ruido.

**b. Actividad muscular del abductor corto del pulgar**: En esta serie de mediciones, se evaluó la actividad eléctrica del abductor corto del pulgar en estados de reposo, fuerza con oposición y sin oposición. Al igual que en la prueba anterior, se utilizó un electrodo de referencia en el codo para reducir la interferencia eléctrica. Esta ubicación del electrodo permitió una colocación cómoda y no intrusiva durante las mediciones, lo que resulta beneficioso para evaluar la función muscular.

#### Datos adquiridos EMG

En este laboratorio, nos enfocaremos en el análisis y la interpretación de los datos de señales EMG previamente adquiridos. Las señales registradas durante las actividades musculares se utilizarán para llevar a cabo análisis específicos y extraer conclusiones relevantes sobre la actividad muscular en el bíceps braquial y el abductor corto del pulgar en diferentes condiciones experimentales.

#### Filtrado, Segmentación y Extracción de Características de Señal EMG

Para esta sección se seleccionó un articulo de referencia <sup>[x1](https://doi.org/10.18280/ts.390518)</sup>, en este se optimiza el procesamiento de señales EMG mediante técnicas de filtrado, segmentación y extracción de características. El mejor enfoque encontrado se describe brevemente a continuación:

- Filtrado

Se aplicó un filtro de rechazo de banda de 45-55Hz para eliminar la interferencia de la línea de alimentación, lo que ayudó a mejorar la calidad de las señales EMG al eliminar el ruido no deseado.

- Segmentación

Se utilizó un método de ventana deslizante con una longitud de ventana de 250 ms y un incremento de 64 ms para segmentar los datos EMG. Esta técnica permitió dividir las señales en intervalos más pequeños para un análisis más detallado.

- Extracción de características

Se exploraron varias técnicas de extracción de características, incluidas las características en el dominio del tiempo (como la media y la varianza, así como características específicas de EMG), características en el dominio de la frecuencia (obtenidas mediante la transformada de Fourier), y métodos en el dominio tiempo-frecuencia (como la transformada de Fourier de tiempo corto y la transformada Wavelet). Además, se propuso un nuevo método de extracción de características basado en los coeficientes AR de las regiones positivas y negativas de la señal.


#### SEÑAL EMG




|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** | **Coeficientes de detalle** | 
|:------------:|:---------------:|:------------:|:------------:|:------------:|:------------:|
|Bior1.5 (Biorthogonal 1.5)|7|16|500 Hz|A7| D1, D2, D3, D4, D5, D6, D7|
<p align="center"><i>Tabla 3. Parámetros considerados para el diseño del filtro en la señal EMG </i></p>

</div>


<a name="resultados"></a>
## RESULTADOS

### SEÑAL EMG

En el análisis de las señales EMG obtenidas del bíceps braquial y del abductor corto del pulgar, el uso de la transformada wavelet discreta (DWT) con la wavelet biorthogonal 1.5 (Bior1.5) resultó particularmente efectivo. La elección de estos parámetros permitió una descomposición detallada de las señales en siete niveles, con un umbral de 16 y una frecuencia de 500 Hz. Observando los gráficos, se pudo apreciar que la señal filtrada del abductor corto del pulgar mostró una mayor claridad y menos ruido en comparación con la del bíceps braquial.

<div align="center">

|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Prueba Biceps|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Imágenes/SeñalBiceps_Original.png">|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/25907d77b4b0c32c31a8138006a56abc9dba9554/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/Se%C3%B1alBiceps_WT.png">|
|Prueba Pulgar|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/25907d77b4b0c32c31a8138006a56abc9dba9554/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/Se%C3%B1alPulgar_Original.png">|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/25907d77b4b0c32c31a8138006a56abc9dba9554/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/Se%C3%B1alPulgar_WT.png">|
<p align="center"><i>Tabla 7. Resumen de la señal filtrada con DWT para la data EMG </i></p>
</div>

<a name="eeg"></a>

### SEÑAL EEG



<a name="archivos"></a>
## ARCHIVO DE LA SEÑAL PLOTEADA EN PYTHON
* **Codigo**
  - [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/d22284eac044bb34acde6b8b07a34325d813988b/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/C%C3%B3digos/emg_wavelet.py)

<a name="discusion"></a>
## DISCUSIÓN
El filtrado de la señal EMG fue más efectivo en el abductor corto del pulgar que en el bíceps braquial debido a varias razones fisiológicas y técnicas. El abductor corto del pulgar, siendo un músculo más pequeño y localizado, experimenta menor interferencia de músculos adyacentes y presenta movimientos menos complejos, lo que reduce significativamente los artefactos y el ruido en la señal. Además, su ubicación superficial y menor profundidad permiten una captación más precisa de la señal por los electrodos. En contraste, el bíceps braquial, al estar rodeado de músculos grandes y estar involucrado en movimientos más amplios, genera señales con mayor ruido e interferencias, lo que dificulta una filtración tan eficaz.

<a name="conclusiones"></a>
## CONCLUSIONES

<a name="referencias"></a>
## REFERENCIAS BIBLIOGRÁFICAS
[1] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/

[2] https://www.ijsrp.org/research-paper-0517/ijsrp-p6504.pdf

[3] https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content

[4] ] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/

[x0] “BITalino (r)evolution Lab Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS”. https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf

[x1] Y. Sevim, “A new feature extraction method for EMG signals,” Trait. Du Signal, vol. 39, no. 5, pp. 1615–1620, 2022. https://doi.org/10.18280/ts.390518

