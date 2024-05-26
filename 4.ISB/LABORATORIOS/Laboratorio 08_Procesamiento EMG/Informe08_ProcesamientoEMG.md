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
7. [Referencias bibliográficas](#referencias)

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
#### PROCEDIMIENTO DE UTILIZACIÓN DE SEÑALES EMG
	
 - **Datos Adquiridos Previamente**

Para este laboratorio, se utilizarán datos de señales EMG adquiridos en sesiones de laboratorio anteriores. El proceso de adquisición se llevó a cabo siguiendo un protocolo estándar utilizando el dispositivo BITalino y el programa OpenSignal. Inicialmente, se estableció la conexión entre el BITalino y OpenSignal mediante Bluetooth para visualizar las señales en tiempo real. Luego, se conectó el sensor EMG de 3 electrodos al BITalino para comenzar la adquisición de señales.
 
 - **Procedimiento de Adquisición Anterior**

Siguiendo las indicaciones de la guía BITalino (r)evolution Lab Guide 2021 proporcionada por PLUX-Wireless Biosignals <sup>[5](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf)</sup>, se implementaron tres protocolos para medir la actividad muscular en diferentes músculos: el bíceps braquial y el abductor corto del pulgar. Los electrodos se colocaron de acuerdo con las especificaciones del protocolo, garantizando una captura precisa de las señales EMG en reposo, sin oposición y con oposición para ambos músculos.

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


<a name="resultados"></a>
## RESULTADOS

<div align="center">
	
|  **SNR para filtro Wavelet**  | **SNR para filtro Butterworth** | **SNR para filtro IIR** | **Filtro mas efectivo** |
|:------------:|:---------------:|:------------:|:----------:|
|12.29 dB|0.46 dB|3.18 dB|Wavelet con SNR de 12.29 dB|
<p align="center"><i>Tabla 2. Resultados de análisis SNR para el abductor del pulgar</i></p>
</div>

</div>
<p align="center">
<image width="600" height="350" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/74995d02-0110-402a-8d56-2ec0ccf56667">
<p align="center"><i>Figura 5. Ploteo de la señal de la prueba del pulgar con el uso de diferentes filtros (fuente : Elaboración propia) </i></p>
</div>

<div align="center">
	
|  **SNR para filtro Wavelet**  | **SNR para filtro Butterworth** | **SNR para filtro IIR** | **Filtro mas efectivo** |
|:------------:|:---------------:|:------------:|:----------:|
|19.41 dB|2.41 dB|6.03 dB|Wavelet con SNR de 19.41 dB|
<p align="center"><i>Tabla 3. Resultados de análisis SNR para el biceps </i></p>
</div>


</div>
<p align="center">
<image width="600" height="350" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/207d6443-b7e9-48c8-abe4-d358b7bd7b2b">
<p align="center"><i>Figura 6. Ploteo de la señal de la prueba del biceps con el uso de diferentes filtros (fuente : Elaboración propia) </i></p>
</div>


</div>
<p align="center">
<image width="600" height="350" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Im%C3%A1genes/abductor_wavelet.jfif">
<p align="center"><i>Figura 7. Ploteo de la señal del abductor del pulgar filtrada con transformada wavelet (fuente : Elaboración propia) </i></p>
</div>


</div>
<p align="center">
<image width="600" height="350" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Im%C3%A1genes/segmentacion_abductor.jfif">
<p align="center"><i>Figura 8. Segmentación utilizado el método de ventana deslizante para el abductor del pulgar</i></p>
</div>

</div>
<p align="center">
<image width="600" height="350" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Im%C3%A1genes/biceps_wavelet.jfif">
<p align="center"><i>Figura 9. Ploteo de la señal del bíceps braquial filtrada con transformada wavelet (fuente : Elaboración propia) </i></p>
</div>

</div>
<p align="center">
<image width="600" height="350" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Im%C3%A1genes/segmenetacion_biceps.jfif">
<p align="center"><i>Figura 10. Segmentación utilizado el método de ventana deslizante para el bíceps braquial</i></p>
</div>

Asimismo, se extrayeron las características correspondientes las cuales se observan en la siguientes carpeta:
 - [Feature extraction](https://github.com/sofiacespedes22/ISB_2024_G8/tree/7f4809ac39605ca591b058a35f0dea00cf118745/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Feature%20extraction)

<a name="archivos"></a>
## ARCHIVO DE LA SEÑAL PLOTEADA EN PYTHON
* **Codigo**
  - [EMG]()

<a name="discusion"></a>
## Discusión
La amplitud, tendencia central y variabilidad de las señales EMG evaluadas permite reconocer afecciones y variaciones del sistema neuromuscular, y es esencial para el diagnóstico de miopatías, neuropatías periféricas, ELA, y síndrome de túnel carpiano. En el presente laboratorio, se investigaron los datos tomados de la EMG para reconocer la actividad muscular según el movimiento o el tipo músculo evaluado, como fue el caso del abductor del pulgar o el músculo bíceps. Se observó que el filtro con mayor capacidad de atenuar el ruido por artefactos fue el filtro utilizando la transformada wavelet. El parámetro del SNR (Signal-to-noise ratio) fue evaluado pues permite identificar la relación entre la claridad de la señal frente al ruido que padece: a un mayor valor de SNR, la señal presenta mayor claridad y el ruido es relativamente mejor, lo cual nos da información de la calidad del filtrado. Se observa, a partir de los resultados obtenidos, que el filtro con transformada Wavelet que tuvo mayor efectividad fue en el bíceps braquial al presentar valores mas altos de SNR así como en la visualización de reducción de picos en la señal. Por último, concluimos que el análisis de señales EMG es relevante en el ámbito de la biomecánica, ya que se pronuncia en relación con la contracción, el rendimiento muscular y la coordinación involucrada. El procesamiento de señales de EMG, que abarca proceso y extracción de características y métodos de análisis y clasificación, es importante en las decisiones de diagnóstico y tratamiento de pacientes con desordenes neuromusculares. Asimismo, valores como la media y el valor RMS son ejes centrales para eliminar y normalizar señales <sup>[7](https://doi.org/10.1016/j.jelekin.2009.01.008)</sup>.


<a name="referencias"></a>
## REFERENCIAS BIBLIOGRÁFICAS
[1] V. Gohel and N. Mehendale, “Review on electromyography signal acquisition and processing,” Biophysical Reviews, vol. 12, no. 6, pp. 1361–1367, Nov. 2020, doi: 10.1007/s12551-020-00770-w. Disponible en: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/

[2] https://www.ijsrp.org/research-paper-0517/ijsrp-p6504.pdf

[3] A. Moreno Sanz, “Procesado Avanzado de señal EMG,” thesis, Universidad Carlos III de Madrid, Escuela politécnica superior, Madrid, 2017. Disponible en: https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content

[4] ] A. M. Moslhi, H. H. Aly, and M. ElMessiery, “The impact of feature extraction on classification accuracy examined by employing a signal transformer to classify hand gestures using surface electromyography signals,” Sensors, vol. 24, no. 4, p. 1259, Feb. 2024, doi: 10.3390/s24041259 Disponible en: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/

[5] “BITalino (r)evolution Lab Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS”. https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf

[6] Y. Sevim, “A new feature extraction method for EMG signals,” Trait. Du Signal, vol. 39, no. 5, pp. 1615–1620, 2022. https://doi.org/10.18280/ts.390518

[7] T. I. Arabadzhiev, V. G. Dimitrov, N. A. Dimitrova, and G. V. Dimitrov, “Interpretation of EMG integral or RMS and estimates of ‘neuromuscular efficiency’ can be misleading in fatiguing contraction,” Journal of Electromyography and Kinesiology, vol. 20, no. 2. Elsevier BV, pp. 223–232, Apr. 2010. doi: 10.1016/j.jelekin.2009.01.008.

