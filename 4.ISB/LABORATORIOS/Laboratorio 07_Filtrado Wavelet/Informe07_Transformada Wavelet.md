# Laboratorio N°7 - Filtrado con transformada wavelet
## **Tabla de contenidos**
1. [Introducción](#introduccion)\
   1.1 [Marco teórico](#marco)
2. [Objetivos](#objetivos)
3. [Metodología](#metodologia)\
   3.1 [Materiales y equipos](#materiales)\
   3.2 [Procedimiento](#adquisicion)
4. [Resultados](#resultados)\
   4.1 [Señal ECG](#ecg)\
   4.1 [Señal EMG](#emg)\
   4.1 [Señal EEG](#eeg)
5. [Archivos](#archivos)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Referencias bibliográficas](#referencias)

  
<a name="introduccion"></a>
## **Introducción**
### **Contexto**
Actualmente en el ámbito de la ingeniería biomédica, la obtención y correcta interpretación de señales médicas como ECG, EMG, y EEG, son de suma importancia el diagnóstico de distintas enfermedades y para la investigación. Una de las principales estrategias usadas para el procesamiento de estas señales es la transformada Wavelet.

La teoría de las wavelets, desarrollada por Morlet, Grossmann y Meyer, inicialmente estaba enfocada en aspectos teóricos más que en aplicaciones prácticas. Sin embargo, investigadores como Daubechies y Mallat establecieron la conexión entre las wavelets y el procesamiento digital de señales, ampliando su utilidad. Las wavelets han sido aplicadas en áreas como compresión de datos, procesamiento de imágenes y estimación espectral tiempo-frecuencia. Ofrecen una alternativa a la transformada de Fourier de tiempo corto en el análisis tiempo-frecuencia de señales discretas. Aunque la teoría subyacente es compleja, la implementación de la transformada de wavelet es más sencilla de lo esperado, lo que permite su aplicación práctica con un mínimo de conocimientos matemáticos. <sup>[1](https://doi.org/10.1049/ecej:19940401)</sup> 


<a name="marco"></a>
### **Marco teórico**
#### **a. Wavelet**

Las wavelets son funciones matemáticas con naturaleza oscilatoria similar a las ondas sinusoidales, pero con la particularidad de ser de "naturaleza oscilatoria finita". Básicamente, una forma de onda de longitud finita y en decadencia, cuando se escala y se traduce, resulta en lo que se llama una "wavelet hija" de la "wavelet madre" original. Por lo tanto, diferentes variables de escala y traducción producen una wavelet hija diferente a partir de una sola wavelet madre. <sup>[2](https://www.proquest.com/scholarly-journals/signal-filtering-using-discrete-wavelet-transform/docview/603852467/se-2)</sup> 

#### **b. Transformadas wavelet**

Las transformadas de wavelet se clasifican como Transformadas de Wavelet Continuas (CWT) y Transformadas de Wavelet Discretas (DWT). La naturaleza oscilatoria finita de las wavelets las hace extremadamente útiles en situaciones de la vida real en las que las señales no son estacionarias. Mientras que la transformada de Fourier de una señal solo ofrece resolución de frecuencia, las transformadas de wavelet ofrecen una resolución de "tiempo-frecuencia" variable, que es característica de estas transformadas.

Una transformada de wavelet descompone una señal en funciones de base conocidas como wavelets. La transformada de wavelet se calcula por separado para diferentes segmentos de la señal de dominio de tiempo en diferentes frecuencias, lo que resulta en un análisis de multi-resolución. Está diseñada de tal manera que el producto de la resolución temporal y la resolución de frecuencia es constante. Por lo tanto, ofrece buena resolución temporal y baja resolución de frecuencia en frecuencias altas, mientras que ofrece buena resolución de frecuencia y baja resolución temporal en frecuencias bajas. Esta característica de análisis de multi-resolución lo hace excelente para señales que tienen componentes de alta frecuencia durante cortos períodos y componentes de baja frecuencia durante períodos largos, como el ruido en señales, imágenes, fotogramas de video, etc. <sup>[2](https://www.proquest.com/scholarly-journals/signal-filtering-using-discrete-wavelet-transform/docview/603852467/se-2)</sup> 

</div>
<p align="center">
<image width="400" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c82a4845-0384-4094-9e30-9e511d2b923c">
<p align="center"><i>Figura 1. Esquema de la Transformada Wavelet </i></p>
</div>

#### **c. Transformada Wavelet Continua y discreta** <sup>[3]()</sup> 
Todas las wavelets son generadas a partir de la función  madre y tiene la misma forma. Lo que varía entre ellas es la escala s (siempre cumple condición de ser mayor a cero) y la ubicación u. Las Wavelets presentan un conportamiento continuo o discreto, dependiendo de la aplicación que le demos.
* **Transformada Wavelet Continua (CWT)**: La tranformada Wavelet continua identidicada como CWT, nos permite obtener un análisis de un señal en un segmento localizado de esta, obteniendo los coeficientes del producto interno entre la señal y la Wavelet madre y realizando una expansión de coeficientes de los mismo. En la _Figura 2_ se puede observar la ecuación de la CWT.
</div>
<p align="center">
<image width="250" height="50" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/fe547337-8e2f-466c-bda1-e42b3c277345">
<p align="center"><i>Figura 2. Ecuación de definición de la Transformada Wavelet Continua [3] </i></p>
</div>
	
* **Transformada Wavelet Discreta (DWT)**: Teniendo en cuenta la CWT, se hizo la observación de que los parámetros de escala y de traslación cambian contuamente, por lo que se presenta la necesidad de realizar un proceso de discretización para poder cambiar a un conjunto de valores finitos. Esto se logra por medio de la integral por sumatorias. En la _Figura 3_ se puede observar la ecuación de la DWT. La DWT es la transformada que estaremos usando a lo largo del laboratorio.
</div>
<p align="center">
<image width="250" height="50" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/3d5eb672-352f-4ea3-9128-042223bfc1ae">
<p align="center"><i>Figura 3. Ecuación de definición de la Transformada Wavelet Discreta [3] </i></p>
</div>


#### **d. Discrete Wavelet Transform (DWT)**
Técnica matemática que descompone una señal en una serie de funciones básicas llamadas wavelets. Estas wavelets son como pequeñas ondas que tienen diferentes tamaños y ubicaciones en el tiempo. La idea es que al combinar estas wavelets de diferentes maneras, podemos representar cualquier tipo de señal de manera eficiente. La descomposición de la señal se realiza calculando coeficientes que indican cuánto de cada wavelet está presente en la señal original. Estos coeficientes nos dan información sobre los diferentes componentes de la señal, como las frecuencias y los momentos en el tiempo.

La ventaja del DWT es que nos permite analizar señales en diferentes escalas de tiempo y frecuencia de manera simultánea, lo que puede ser útil para detectar patrones en datos complejos, como señales de audio o imágenes. <sup>[4](https://repository.rice.edu/bitstreams/33cd90c3-b6c6-4a7e-ab6f-dbc34e868d9b/download)</sup> 

#### **c.1. Tipos de Wavelets discretas**



<a name="objetivos"></a>
## Objetivos
1. Implementar y comparar el filtrado wavelet para reducir el ruido por artefactos producidos de las señales ECG, EMG y EEG para la aplicación en aspectos clínicos

<a name="metodologia"></a>
## Metodología 
La metodología del siguiente laboratorio consistió en el diseño de filtros wavelet para atenuar las frecuencias altas generadas por el ruido en la adquisición y procesamiento de señales ECG, EMG y EEG a partir del protocolo de de adquisición y posicionamiento de los electrodos de la guía del Kit BITalino**“"BITalino HOME-GUIDE"** <sup>[5](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>, realizado en laboratorios anteriores. Puesto que las señales adquirida no han atravesado ningún tipo de pre-procesamiento, contienen ruidos debido a los artefactos que surgieron durante la adquisición y, por lo tanto, resulta relevante la aplicación del filtrado para obtener una mayor claridad de la señal y así una interpretación mas acertada.

La aplicación del filtrado para las tres señales estuvo enfocado en el método de pre-procesamiento utilizando el método de transformada wavelet discreta (DWT) debido a que permite analizar señales en múltiples resoluciones lo que permite una mejor localización en tiempo y en frecuencia [1]. El método de DWT permite descomponer la señal en componentes de alta y baja frecuencia con filtros de pasa baja y alta, reduciendo los coeficientes wavelet a mitad de cada nivel. La señal se subsamplea, basado en la regal de Nyquist, descartando cada segunda muestra, lo que permite que los coeficientes DWT reconstruyan la señal original. A continuación, se detalla los pasos seguidos para la obtención del filtrado:

**1. Descomposición de la señal mediantre la DWT: La descomposición de la señal se utilizó**:
Las señales fueron descompuestas utilizando los tipos de filtros de DWT, como la familia Daubechies o Biorthogonal, según la literatura de referencia. Este proceso permite separar las componentes de frecuencia de la señal en diferentes niveles, aislando los detalles y las aproximaciones de frecuencia baja y alta.

**2. Cálculo del umbral**:
Se aplicó una técnica de umbralización suave a los coeficientes wavelet para atenuar o eliminar el ruido generado en la toma de las señales. El umbral utilizado se basó en la fórmula (ver Fórmula 1), optimizada para la reducción del ruido evitando eliminar las características fundamentales de las señales EEG, EMG y ECG para su posterior análisis:

**3. Reconstrucción de la señal**:
Utilizando los coeficientes wavelet modificados, se reconstruyeron las señales filtradas. Este paso permite asegurar que los elementos esenciales de cada señal, como las bandas de frecuencia alfa, beta, gamma o theta específicas en EEG, las contracciones musculares en EMG, y los picos R, Q y S del complejo QRS en ECG, se mantengan definidos, facilitando así su identificación y análisis.
   
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
#### Señal ECG
Para el filtrado con transformada Wavelet de ECG, se utilizaron las señales  ECG obtenidas en el Laboratorio 4 de ECG. Estos datos, fueron obtenidos en 3 diferentes estados: reposo, respiración controlada y depués de haber realizado actividad física. 

**a. Estado de reposo** :El sujeto de prueba se quedó en una posición estable y manteniendo la calma. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Estado de respiración prolongada**: El sujeto mantuvo la respiración por 30 segundos y se registró la señal durante la inspiración, mantención y expiración. El registro de la señal fue grabado por 30 segundos.

**c. Estado de ejercicio intensivo**: El sujeto de prueba realizó la actividad física de 10 burpees por 3 minutos y la señal fue registrada durante y después de la actividad realizada. El registro de la señal fue grabado por 30 segundos.

A continuación, se definen los parámetros obtenidos para el filtrado de las señales ECG a partir de la literatura de referencia. <sup>[]()</sup> 

|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** | **Coeficientes de detalle** | 
|:------------:|:---------------:|:------------:|:------------:|:------------:|:------------:|
|Daubechies wavelet (db4)|2|0.2|500 Hz|A2| |
<p align="center"><i>Tabla 2. Parámetros considerados para el diseño del filtro en la señal ECG </i></p>

#### Señal EMG

Para el estudio de la actividad muscular, se llevaron a cabo mediciones del músculo bíceps braquial y del abductor corto del pulgar en diferentes estados:

**a. b. Actividad muscular del bíceps braquial (brazo):** Durante esta prueba, se registró la actividad eléctrica del bíceps braquial en estados de reposo y ante la exposición de fuerzas con oposición o sin ella. Para ello, en el ensayo se empleó un electrodo de referencia en el codo para minimizar la interferencia eléctrica y el ruido.</p>

**Actividad muscular del abductor corto del pulgar:** En esta serie de mediciones, se evaluó la actividad eléctrica del abductor corto del pulgar en estados de reposo, fuerza con oposición y sin oposición. Al igual que en la prueba anterior, se utilizó un electrodo de referencia en el codo para reducir la interferencia eléctrica. Esta ubicación del electrodo permitió una colocación cómoda y no intrusiva durante las mediciones, lo que resulta beneficioso para evaluar la función muscular.

Para el análisis de la señal de actividad muscular de cada ensayo, se utilizará DWT. Este enfoque ofrece la capacidad de detectar y caracterizar cambios en la señal en distintas escalas temporales, siendo especialmente útil para identificar patrones complejos en señales no estacionarias como la actividad muscular. La transformada de wavelet proporciona información detallada sobre la localización temporal de eventos de interés, lo que nos permite identificar cambios en la actividad muscular en respuesta a diferentes condiciones o estímulos. A continuación, se definen los parámetros obtenidos para el filtrado de las señales EMG a partir de la literatura de referencia. <sup>[x](https://doi.org/10.1016/j.jelekin.2013.05.001)</sup> 

<div align="center">
	
|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** | **Coeficientes de detalle** | 
|:------------:|:---------------:|:------------:|:------------:|:------------:|:------------:|
|Bior1.5 (Biorthogonal 1.5)|7|16|500 Hz|A7| D1, D2, D3, D4, D5, D6, D7|
<p align="center"><i>Tabla 3. Parámetros considerados para el diseño del filtro en la señal EMG </i></p>

</div>

#### Señal EEG

Se consideró el uso de las señales de electroencefalograma (EEG) obtenidas en el Laboratorio 05 para el filtrado con la transformada wavelet, las cuales se obtuvieron en diferentes estados: reposo, durante el parpadeo, reposo tras el parpadeo y mientras se realizaba y respondía preguntas matemáticas (razonamiento).

**a. Estado de reposo**: El sujeto de prueba se quedó en una posición estable y manteniendo la calma para el registro de una línea base de señal con poco ruido y sin movimientos. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Estado de ojos cerrado-ojos abiertos**: El sujeto mantuvo los ojos cerrados y abiertos completando un ciclo (5 veces cada estado), manteniendo ambas fases durante 5 segundos. Para evitar artefactos, el sujeto se mantuvo calmado y mirando hacia un punto específico. El registro de la señal fue grabado por 50 segundos.

**c. Estado de segundo reposo**: Tras la primera actividad, el sujeto de prueba mantuvo nuevamente el estado de calma y sin movimiento como segunda fase de referencia. El registro de la señal fue grabado por 30 segundos.

**d. Estado de preguntas**: Se realizaron una serie de ejercicios matemáticos <sup> [14](https://doi.org/10.3758/s13415-019-00703-5)</sup> de menor a mayor complejidad al sujeto de prueba para que pueda resolverlo mentalmente enfocando su mirada en un punto específicos para evitar artefactos. La duración entre el lapso de registro de la respuesta y la siguiente pregunta fue de 12 segundos. Las preguntas realizadas se observan en la Tabla 4.

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

<p align="justify">El filtro utilizado para la eliminación de ruido en la señal es un filtro DWT tipo Biorthogonal 2.6, debido a que permite  y un nivel de 5. Los coeficientes de aproximación fueron A5 y de detalle D1, D2, D3, D4 y D5. El umbral fue calculado mediante umbralización suae y fue optimizado mediante pruebas. Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada con el DWT para observar la eficiencia del filtrado. A continuación, se definen los parámetros obtenidos para el filtrado de las señales EEG a partir de la literatura de referencia <sup>[X]()</sup>.</p>

<div align="center">
	
|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** | **Coeficientes de detalle** | 
|:------------:|:---------------:|:------------:|:------------:|:------------:|:------------:|
|bior2.6 (Biorthogonal 2.6)|5|16|1000 Hz|A5| D1, D2, D3, D4, D5|
<p align="center"><i>Tabla 5. Parámetros considerados para el diseño del filtro en la señal EEG </i></p>

</div>

<a name="resultados"></a>
## Resultados

<a name="ecg"></a>
### Señal ECG
<div align="center">

|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Reposo|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/a65245f0-9aea-467d-b7b5-d029ec1b11a0">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/92ec472d-1273-41d1-88f9-ca300708860f">|
|Respiración prolongada|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1bdb7cf7-de2d-4d1d-9800-20a37943cb9e">|<image width="300" height="100" src="">|
|Ejercicio Intensivo|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/a92ee20a-44d4-4d6f-b6e6-08ef77d57510">|<image width="300" height="100" src="">|
<p align="center"><i>Tabla 6. Resumen de la señal filtrada con DWT para la data ECG </i></p>
</div>
<a name="emg"></a>


### Señal EMG

En el análisis de las señales EMG obtenidas del bíceps braquial y del abductor corto del pulgar, el uso de la transformada wavelet discreta (DWT) con la wavelet biorthogonal 1.5 (Bior1.5) resultó particularmente efectivo. La elección de estos parámetros permitió una descomposición detallada de las señales en siete niveles, con un umbral de 16 y una frecuencia de 500 Hz. Observando los gráficos, se pudo apreciar que la señal filtrada del abductor corto del pulgar mostró una mayor claridad y menos ruido en comparación con la del bíceps braquial.

<div align="center">

|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Prueba Biceps|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Imágenes/SeñalBiceps_Original.png">|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/25907d77b4b0c32c31a8138006a56abc9dba9554/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/Se%C3%B1alBiceps_WT.png">|
|Prueba Pulgar|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/25907d77b4b0c32c31a8138006a56abc9dba9554/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/Se%C3%B1alPulgar_Original.png">|<image width="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/25907d77b4b0c32c31a8138006a56abc9dba9554/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/Se%C3%B1alPulgar_WT.png">|
<p align="center"><i>Tabla 7. Resumen de la señal filtrada con DWT para la data EMG </i></p>
</div>

<a name="eeg"></a>

### Señal EEG

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Reposo|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/084fb69b10b80046c5b4b9ef50b891431fa742b4/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/reposo.png">|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/084fb69b10b80046c5b4b9ef50b891431fa742b4/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/reposo_dwt.png">|
|Parpadeo|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/084fb69b10b80046c5b4b9ef50b891431fa742b4/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/parpadeo.png">|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/084fb69b10b80046c5b4b9ef50b891431fa742b4/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/parpadeo_dwt.png">|
|Razonamiento|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/084fb69b10b80046c5b4b9ef50b891431fa742b4/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/preguntas.png">|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/084fb69b10b80046c5b4b9ef50b891431fa742b4/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/Im%C3%A1genes/preguntas_dwt.png">|
<p align="center"><i>Tabla 8. Resumen de la señal filtrada con DWT para la data EEG </i></p>
</div>

<a name="archivos"></a>
## Archivo de las señales ploteadas en Python
* **Codigo**
  - [ECG]()
  - [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/d22284eac044bb34acde6b8b07a34325d813988b/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/C%C3%B3digos/emg_wavelet.py)
  - [EEG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/db4939c9ee53fb066a803574d1a96906d5e0938c/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/C%C3%B3digos/eeg_wavelet.py)

<a name="discusion"></a>
## Discusión


<a name="conclusiones"></a>
## Conclusiones

<a name="referencias"></a>
## Referencias bibliográficas

[1] P. M. Bentley and J. T. E. McDonnell, “Wavelet transforms: an introduction,” Electronics & Communication Engineering Journal, vol. 6, no. 4, pp. 175–186, Aug. 1994, doi: https://doi.org/10.1049/ecej:19940401.

[2] R. Madan, S. K. Singh and N. Jain, "Signal Filtering Using Discrete Wavelet Transform," International Journal of Recent Trends in Engineering, vol. 2, (3), pp. 96-98, 2009. Available: https://www.proquest.com/scholarly-journals/signal-filtering-using-discrete-wavelet-transform/docview/603852467/se-2.

[3]

[4] C. S. Burrus, R. Gopinath, and H. Guo, “Wavelets and Wavelet Transforms OpenStax-CNX,” 2015. Available: https://repository.rice.edu/bitstreams/33cd90c3-b6c6-4a7e-ab6f-dbc34e868d9b/download

[5] https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

[x] S. K. Chowdhury, A. D. Nimbarte, M. Jaridi, and R. C. Creese, “Discrete wavelet transform analysis of surface electromyography for the fatigue assessment of neck and shoulder muscles,” Journal of Electromyography and Kinesiology, vol. 23, no. 5, pp. 995–1003, Oct. 2013, doi: https://doi.org/10.1016/j.jelekin.2013.05.001.


