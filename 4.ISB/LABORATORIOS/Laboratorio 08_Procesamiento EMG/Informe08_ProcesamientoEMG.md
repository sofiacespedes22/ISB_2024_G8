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
## **Introducción**
### **Contexto**
Como sabemos la electromiografía (EMG), es el estudio que permite registrar señales eléctricas biomédicas que son obtenidas a través de actividades generadas por los músculos esqueléticos, estas señales mioeléctricas son generadas a partir de neuronas motoras, que forman parte del Sistema Nervioso Central (SNC) <sup>[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/)</sup>. En conclusión, una señal EMG es una señal biomédica que registra las corrientes eléctricas que son generadas por los músculos durante la contracción, representando actividades neuromusculares. 

Actualmente, la EMG es una herramienta de gran utilidad, ya que se pueden utilizar para diagnóstico y monitoreo de lesiones musculares, daños a los nervios y disfunciones musculares que se pueden producir a trastornos neurológicos y musculares, con fines de investigación, para el análisis de la biomecánica de diversos movimientos y el análisis de la marcha, entre otros. <sup>[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/)</sup>.

La electromiografía (EMG) al tener tanta relevancia en el ámbito biomédico, requiere de un procesamiento de la señal antes de ser estudiada, ya que al ser al ser una señal que registra la actividad muscular, la cual es controlada por el sistema nervioso, hace que la EMG se vuelve una señal complicada de analizar. La señal EMG puede adquirir ruido mientras viaja por los diferentes tejidos, además de que si la EMG es tomada en la superficie de la piel puede recoger señales de diferentes unidades motoras a la vez. Es por ello, que un adecuado procesamiento de la señal EMG es de suma importancia para un correcto análisis de la misma. 


<a name="marco"></a>
### **Marco teórico**
#### a. EMG
Proceso de registro de las actividades eléctricas musculares. Las actividades eléctricas musculares son realizadas bajo el control del cerebro, por lo tanto, están directamente relacionadas con el sistema nervioso. En el cerebro se produce un potencial de acción, el cual pasa a través de las fibras nerviosas, las cuales estimularán a las fibras musculares y las neuronas motoras trasmiten la señal logrando que el músculo se contraiga, generando una pequeña corriente eléctrica, la cual puede ser medida y registrada mediante EMG, y es mostrada en gráficos, sonidos y cuantificarla en valores numéricos <sup>[2](https://www.ijsrp.org/research-paper-0517/ijsrp-p6504.pdf)</sup> .Las señales EMG son señales no estacionarias, no lineales y complejas. <sup>[2](https://www.ijsrp.org/research-paper-0517/ijsrp-p6504.pdf)</sup>.

</div>
<p align="center">
<image width="500" height="250" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2b11a295-81ac-4f5b-9ae4-f85013bbe7a8">
<p align="center"><i>Figura 1. Señal EMG sin procesamiento [2] </i></p>
</div>

La amplitud de una señal EMG puede depender de varios factores, incluyendo la distancia que separa a los electrodos, el material de los electrodos y ruidos y “artefactos”.

#### b. Adquisición
Para la adquisición de las señales EMG, se utilizan principalmente 2 tipos de electrodos: el electrodo de aguja (método invasivo) y los electrodos de superficie (método no invasivo) (_Figura 2_). Los electrodos de aguja se clasifican además en tres subtipos: los electrodos individuales monopolares, electrodos EMG de fibra única y electrodos EMG concéntricos; tienen aproximadamente 1 mm2 de ancho. Los electrodos de superficie, son de dos tipos: electrodos EMG gelificados y electrodos EMG secos; tienen entre 0.5 y 2.5 mm de ancho y como son colocados en la superficie de la piel, son no invasivos, estos electrodos detectan el cambio entre la superficie del músculo y la piel a través de la conducción electrolítica <sup>[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/)</sup> .

</div>
<p align="center">
<image width="230" height="250" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e442da38-c5bb-479c-b12d-5dd2702dcc1b">
<p align="center"><i>Figura 2. Tipos de electrodos para la adquisición de señales EMG [1] </i></p>
</div>


|  **Electrodo de superficie**  | **Electrodo de aguja (Invasivo)** |
|:------------:|:---------------:|
|<p align="justify">Se colocan sobre la piel del músculo que se desea medir.</p>|<p align="justify">Son electrodos intramusculares, estos deben ser insertados directamente en el músculo que se desea analizar, requiere de un especialista que supervise diche inserción.</p>|
|<p align="justify">La señal que se registre es el promedio de la actividad eléctrica de varias unidades motoras en el músculo.</p>|<p align="justify">Es posible solo obtener mediciones de una sola unidad motora.</p>|
|<p align="justify">Al ser colocados los electrodos en la superficie de la piel, al viajar por lo diferentes tejidos, presenta un alto nivel de ruido.</p>|<p align="justify">La cantidad de ruido es menor.</p>|

En este laboratorio, nosotros estaremos analizando señales EMG adquiridas por electrodos de superficie, por lo tanto, es necesario que estas señales tengan un correcto procesamiento, para poder atenuar el ruido, producido por la propia adquisición y así poder luego realizar un mejor análisis.

#### c. Procesamiento
##### Pre-Procesamiento
Como mencionamos, para poder analizar correctamente las señales EMG obtenidas, se requiere de un procesamiento de estas señales, con el fin de eliminar el ruido. Las señales obtenidas por electrodos de superficie, son señales bastante débiles y ruidosas, como se mencionó anteriormente, por lo que requiere adecuación antes de ser tratada. Por lo que primero la señal debe pasar por una etapa de amplificación <sup>[3](https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content)</sup>. Después de esta amplificación, se siguen los siguientes pasos:

* **Filtrado**: Se debe empezar con una etapa de filtración, ya que es esencial para reducir los artefactos en las señales EMG. Generalmente se necesita un filtro paso alto para que se puedan reducir efectos de artefactos correspondientes a movimientos en inestabilidad entre los electrodos de superficie y la piel, también se necesitarán filtros pasa bajo para registrar los datos que corresponden a estimulación muscular y eliminar interferencias de alta frecuencia, e incluso se puede utilizar filtro pasa banda <sup>[3](https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content)</sup>.  En algunos estudios, para poder filtrar la señal utilizaron filtros Butterworth con parámetros específicos o filtros pasa banda <sup>[4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10893156/)</sup>. En este laboratorio utilizaremos el filtro que mejor nos haya dado resultado de los laboratorios anteriores de FIR e IRR. 






##### Extracción de características


##### Clasificación y evaluación



<a name="objetivos"></a>
## Objetivos

<a name="metodologia"></a>
## Metodología 
La metodología del siguiente laboratorio consistió en el diseño de filtros wavelet para atenuar las frecuencias altas generadas por el ruido en la adquisición y procesamiento de señales ECG, EMG y EEG a partir del protocolo de de adquisición y posicionamiento de los electrodos de la guía del **Kit BITalino BITalino HOME-GUIDE** <sup>[5](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>, realizado en laboratorios anteriores. Puesto que las señales adquirida no han atravesado ningún tipo de pre-procesamiento, contienen ruidos debido a los artefactos que surgieron durante la adquisición y, por lo tanto, resulta relevante la aplicación del filtrado para obtener una mayor claridad de la señal y así una interpretación mas acertada.

La aplicación del filtrado para las tres señales estuvo enfocado en el método de pre-procesamiento utilizando el método de transformada wavelet discreta (DWT) debido a que permite analizar señales en múltiples resoluciones lo que permite una mejor localización en tiempo y en frecuencia. El método de DWT permite descomponer la señal en componentes de alta y baja frecuencia con filtros de pasa baja y alta, reduciendo los coeficientes wavelet a mitad de cada nivel <sup>[6](http://dx.doi.org/10.13005/bpj/627)</sup> <sup>[7](https://doi.org/10.1109/CCAA.2016.7813897)</sup> [8] <sup>[9](http://www.ijecs.in/index.php/ijecs/article/download/1393/1279/2481)</sup> . La señal se subsamplea, basado en la regal de Nyquist, descartando cada segunda muestra, lo que permite que los coeficientes DWT reconstruyan la señal original <sup>[6]()</sup> . A continuación, se detalla los pasos seguidos para la obtención del filtrado:

 

<a name="materiales"></a>
### 1. Materiales y Equipos

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|-|**Laptop o PC**: Laptop equipada con el programa Python, para poder implementar ahí el código, para realizar los respectivos filtrados|1|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|

<p align="center"><i>Tabla 1. Materiales y equipos utilizados</i></p>
</div>

<a name="adquisicion"></a>
### 2. Procedimiento
#### Procedimiento de Utilización de Señales EMG
	
 - Datos Adquiridos Previamente

Para este laboratorio, se utilizarán datos de señales EMG adquiridos en sesiones de laboratorio anteriores. El proceso de adquisición se llevó a cabo siguiendo un protocolo estándar utilizando el dispositivo BITalino y el programa OpenSignal. Inicialmente, se estableció la conexión entre el BITalino y OpenSignal mediante Bluetooth para visualizar las señales en tiempo real. Luego, se conectó el sensor EMG de 3 electrodos al BITalino para comenzar la adquisición de señales.
 
 - Procedimiento de Adquisición Anterior

Siguiendo las indicaciones de la guía BITalino (r)evolution Lab Guide 2021 proporcionada por PLUX-Wireless Biosignals <sup>[x0](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf)</sup>, se implementaron tres protocolos para medir la actividad muscular en diferentes músculos: el bíceps braquial y el abductor corto del pulgar. Los electrodos se colocaron de acuerdo con las especificaciones del protocolo, garantizando una captura precisa de las señales EMG en reposo, sin oposición y con oposición para ambos músculos.
  

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

<div align="center">
	
|  **Categoría**  | **Pregunta** | 
|:------------:|:---------------:|
|**Simple**|<p align="justify"> Hay 3 pájaros en un árbol; Llegan 7 más. ¿Cuántos pájaros hay ahora?</p>|
|**Simple**|<p align="justify"> Jonás tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tienen en total?</p>|
|**Simple**|<p align="justify"> Hanna tiene 9 dólares pero gastó 4. ¿Cuántos dólares le quedan?</p>|
|**Compleja**|<p align="justify"> John anotó 45 puntos para su equipo; 10 más que José. Marie anotó 13 puntos más que John y Joseph juntos. ¿Cuántos puntos obtuvieron en total?</p>|
|**Compleja**|<p align="justify"> El grupo A tiene 24 estudiantes; 13 menos que el grupo B. El grupo C tiene 12 alumnos más que los grupos A y B juntos. ¿Cuál es el número total de estudiantes?</p>|
|**Compleja**|<p align="justify"> Una tienda vendió 21 refrescos por la mañana y 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y por la tarde juntas. ¿Cuántos refrescos se vendieron en total?</p>|
<p align="center"><i>Tabla 4. Preguntas realizadas al sujeto de prueba </i></p>
</div>



<a name="resultados"></a>
## Resultados

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
## Archivo de las señales ploteadas en Python
* **Codigo**
  - [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/d22284eac044bb34acde6b8b07a34325d813988b/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/C%C3%B3digos/emg_wavelet.py)

<a name="discusion"></a>
## Discusión
El filtrado de la señal EMG fue más efectivo en el abductor corto del pulgar que en el bíceps braquial debido a varias razones fisiológicas y técnicas. El abductor corto del pulgar, siendo un músculo más pequeño y localizado, experimenta menor interferencia de músculos adyacentes y presenta movimientos menos complejos, lo que reduce significativamente los artefactos y el ruido en la señal. Además, su ubicación superficial y menor profundidad permiten una captación más precisa de la señal por los electrodos. En contraste, el bíceps braquial, al estar rodeado de músculos grandes y estar involucrado en movimientos más amplios, genera señales con mayor ruido e interferencias, lo que dificulta una filtración tan eficaz.

<a name="conclusiones"></a>
## Conclusiones

<a name="referencias"></a>
## Referencias bibliográficas
[1] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755956/

[2] https://www.ijsrp.org/research-paper-0517/ijsrp-p6504.pdf
