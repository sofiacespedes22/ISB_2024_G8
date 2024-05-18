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
<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c82a4845-0384-4094-9e30-9e511d2b923c">
<p align="center"><i>Figura 1. Esquema de la Transformada Wavelet </i></p>
</div>

#### **c. Transformada Wavelet Continua y discreta**
Todas las wavelets son generadas a partir de la función  madre (_Figura2_) y tiene la misma forma. Lo que varía entre ellas es la escala s (siempre cumple condición de ser mayor a cero) y la ubicación u. Las Wavelets presentan un conportamiento continuo o discreto, dependiendo de la aplicación que le demos.

</div>
<p align="center">
<image width="250" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2a3edcef-17a0-49ad-9795-5418fb8d3365">
<p align="center"><i>Figura 2. Función madre </i></p>
</div>

* **Transformada Wavelet Continua (CWT)**: La tranformada Wavelet continua identidicada como CWT, nos permite obtener un análisis de un señal en un segmento localizado de esta, obteniendo los coeficientes del producto interno entre la señal y la Wavelet madre y realizando una expansión de coeficientes de los mismo. En la _Figura 3_ se puede observar la ecuación de la CWT.
</div>
<p align="center">
<image width="250" height="80" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/deec86c7-9d3a-4057-82e9-6b47600dd568">
<p align="center"><i>Figura 3. Ecuación de definición de la Transformada Wavelet Continua </i></p>
</div>

* **Transformada Wavelet Discreta (DWT)**: Teniendo en cuenta la CWT, se hizo la observación de que los parámetros de escala y de traslación cambian contuamente, por lo que se presenta la necesidad de realizar un proceso de discretización para poder cambiar a un conjunto de valores finitos. Esto se logra por medio de la integral por sumatorias. En la _Figura 4_ se puede observar la ecuación de la DWT. La DWT es la transformada que estaremos usando a lo largo del laboratorio.
  
</div>
<p align="center">
<image width="250" height="50" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/7a0289e7-103f-4921-8535-8b43bcaa9148">
<p align="center"><i>Figura 4. Ecuación de definición de la Transformada Wavelet Discreta </i></p>
</div>


#### **d. Discrete Wavelet Transform (DWT)**
Técnica matemática que descompone una señal en una serie de funciones básicas llamadas wavelets. Estas wavelets son como pequeñas ondas que tienen diferentes tamaños y ubicaciones en el tiempo. La idea es que al combinar estas wavelets de diferentes maneras, podemos representar cualquier tipo de señal de manera eficiente. La descomposición de la señal se realiza calculando coeficientes que indican cuánto de cada wavelet está presente en la señal original. Estos coeficientes nos dan información sobre los diferentes componentes de la señal, como las frecuencias y los momentos en el tiempo.

La ventaja del DWT es que nos permite analizar señales en diferentes escalas de tiempo y frecuencia de manera simultánea, lo que puede ser útil para detectar patrones en datos complejos, como señales de audio o imágenes. <sup>[3](https://repository.rice.edu/bitstreams/33cd90c3-b6c6-4a7e-ab6f-dbc34e868d9b/download)</sup> 

</div>
<p align="center">
<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/08dbb35a-84e5-4bfc-b0b2-f9de7f4ae043">
<p align="center"><i>Figura 5. Estructura del proceso de descomposición de la transformada wavelet discreta [3]</i></p>
</div>


##### **d.1. Tipos de Wavelets discretas** <sup>[4](https://disp.ee.ntu.edu.tw/tutorial/WaveletTutorial.pdf)</sup>
Entre los tipos de Wavelets, tenemos los siguientes:
* **Wavelet de Haar**: Fue la primera wavelet que se propuso y la más simple. Además, tiene un función madre discontinua, lo cual en ciertos contextos podría resultar un desventaja ya que no es muy suave, por lo que luego de usarla se necesitaria hacer una reconstrucción suave, sin embargo, a pesar de su simplicidad y la discontinuidad, esta wavelet es útil para el análisis señales y es la base de las Wavelets que veremos a continuación. 
* **Wavelets de Daubechies**: Está formada por un conjunto de wavelets ortogonales con soporte compacto y están diseñadas de forma que puedan maximizar la suavidad de acuerdo a la longitud que se le de, esto la hace útil para la comprensión de imágenes y el procesamiento de señales.
* **Wavelets de Meyer**: Estas Wavelets a pesar de no están compactamente soportadas, nos proporcionan una aproximación más suave. Tiene aplicaciones en el análisis de señales biomédicas y en procesamiento de señales específicas.
* **Wavelets Symlets**: Tienen mayor simetría que las Daubechies, lo que le permite tener una fase más lineal y capturar las características de señales con simetría par.
* **Wavelets Coiflets**: Nos proporcionan mejor representación de señales polinomiales. Son diseñadas con un número específico de momentos de desvanecimiento, lo que ocasiona que el tamaño del soporte sea mínimo. 


<a name="objetivos"></a>
## Objetivos
1. Implementar y comparar el filtrado wavelet para reducir el ruido por artefactos producidos de las señales ECG, EMG y EEG para la aplicación en aspectos clínicos

<a name="metodologia"></a>
## Metodología 
La metodología del siguiente laboratorio consistió en el diseño de filtros wavelet para atenuar las frecuencias altas generadas por el ruido en la adquisición y procesamiento de señales ECG, EMG y EEG a partir del protocolo de de adquisición y posicionamiento de los electrodos de la guía del **Kit BITalino BITalino HOME-GUIDE** <sup>[5](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>, realizado en laboratorios anteriores. Puesto que las señales adquirida no han atravesado ningún tipo de pre-procesamiento, contienen ruidos debido a los artefactos que surgieron durante la adquisición y, por lo tanto, resulta relevante la aplicación del filtrado para obtener una mayor claridad de la señal y así una interpretación mas acertada.

La aplicación del filtrado para las tres señales estuvo enfocado en el método de pre-procesamiento utilizando el método de transformada wavelet discreta (DWT) debido a que permite analizar señales en múltiples resoluciones lo que permite una mejor localización en tiempo y en frecuencia. El método de DWT permite descomponer la señal en componentes de alta y baja frecuencia con filtros de pasa baja y alta, reduciendo los coeficientes wavelet a mitad de cada nivel <sup>[6](http://dx.doi.org/10.13005/bpj/627)</sup> <sup>[7](https://doi.org/10.1109/CCAA.2016.7813897)</sup> [8] <sup>[9](http://www.ijecs.in/index.php/ijecs/article/download/1393/1279/2481)</sup> . La señal se subsamplea, basado en la regal de Nyquist, descartando cada segunda muestra, lo que permite que los coeficientes DWT reconstruyan la señal original <sup>[6]()</sup> . A continuación, se detalla los pasos seguidos para la obtención del filtrado:

**1. Descomposición de la señal mediantre la DWT: La descomposición de la señal se utilizó**:
Las señales fueron descompuestas utilizando los tipos de filtros de DWT, como la familia Daubechies o Biorthogonal, según la literatura de referencia. Este proceso permite separar las componentes de frecuencia de la señal en diferentes niveles, aislando los detalles y las aproximaciones de frecuencia baja y alta.

**2. Cálculo del umbral**:
Se aplicó una técnica de umbralización suave a los coeficientes wavelet para atenuar o eliminar el ruido generado en la toma de las señales. El umbral utilizado se basó en la fórmula (ver Fórmula 1)<sup>[10](https://doi.org/10.1093/biomet/81.3.425)</sup>, optimizada para la reducción del ruido evitando eliminar las características fundamentales de las señales EEG, EMG y ECG para su posterior análisis:

</div>
<p align="center">
<image width="250" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ec77e1c5-4ccd-47e0-8842-fb8600758275">
<p align="center"><i>Figura 6. Fórmula para el cálculo del umbral </i></p>
</div

**3. Reconstrucción de la señal**:
Utilizando los coeficientes wavelet modificados, se reconstruyeron las señales filtradas. Este paso permite asegurar que los elementos esenciales de cada señal, como las bandas de frecuencia alfa, beta, gamma o theta específicas en EEG, las contracciones musculares en EMG, y los picos R, Q y S del complejo QRS en ECG, se mantengan definidos, facilitando así su identificación y análisis.

</div>
<p align="center">
<image width="450" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/062087dc-fe29-4b71-b5d3-f1973986f0d3">
<p align="center"><i>Figura 7. Diagrama de flujo de eliminación de ruido con transformada wavelet </i></p>
</div>

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
#### SEÑAL ECG
Para el filtrado con transformada Wavelet de ECG, se utilizaron las señales  ECG obtenidas en el Laboratorio 4 de ECG. Estos datos, fueron obtenidos en 3 diferentes estados: reposo, respiración controlada y depués de haber realizado actividad física. 

**a. Estado de reposo** :El sujeto de prueba se quedó en una posición estable y manteniendo la calma. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Estado de respiración prolongada**: El sujeto mantuvo la respiración por 30 segundos y se registró la señal durante la inspiración, mantención y expiración. El registro de la señal fue grabado por 30 segundos.

**c. Estado de ejercicio intensivo**: El sujeto de prueba realizó la actividad física de 10 burpees por 3 minutos y la señal fue registrada durante y después de la actividad realizada. El registro de la señal fue grabado por 30 segundos.

El filtro utilizado para la eliminación de ruido en la señal ECG es un filtro Daubechies(db4) con un nivel 2. Los coeficientes de aproximación fue A2 y de detalle. En el caso del umbral, según el paper en el que nos basamos, indicaban un valor umbral de 0.2, ese valor lo tomamos como valor inicial, sin embargo, el filtrado era casi imperceptible, por lo que optamos después de algunas pruebas, el valor 1. A continuación, se definen los parámetros obtenidos para el filtrado de las señales ECG a partir de la literatura de referencia <sup>[11](https://ieeexplore.ieee.org/document/7569341)</sup>.</p>

<div align="center">
	
|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** |
|:------------:|:---------------:|:------------:|:------------:|:------------:|
|Daubechies wavelet (db4)|2|1| 360 Hz|A2|
<p align="center"><i>Tabla 2. Parámetros considerados para el diseño del filtro en la señal ECG </i></p>

</div>

#### SEÑAL EMG

Para el estudio de la actividad muscular, se llevaron a cabo mediciones del músculo bíceps braquial y del abductor corto del pulgar en diferentes estados:

**a. Actividad muscular del bíceps braquial (brazo):** Durante esta prueba, se registró la actividad eléctrica del bíceps braquial en estados de reposo y ante la exposición de fuerzas con oposición o sin ella. Para ello, en el ensayo se empleó un electrodo de referencia en el codo para minimizar la interferencia eléctrica y el ruido.</p>

**b. Actividad muscular del abductor corto del pulgar:** En esta serie de mediciones, se evaluó la actividad eléctrica del abductor corto del pulgar en estados de reposo, fuerza con oposición y sin oposición. Al igual que en la prueba anterior, se utilizó un electrodo de referencia en el codo para reducir la interferencia eléctrica. Esta ubicación del electrodo permitió una colocación cómoda y no intrusiva durante las mediciones, lo que resulta beneficioso para evaluar la función muscular.

Para el análisis de la señal de actividad muscular de cada ensayo, se utilizará DWT. Este enfoque ofrece la capacidad de detectar y caracterizar cambios en la señal en distintas escalas temporales, siendo especialmente útil para identificar patrones complejos en señales no estacionarias como la actividad muscular. La transformada de wavelet proporciona información detallada sobre la localización temporal de eventos de interés, lo que nos permite identificar cambios en la actividad muscular en respuesta a diferentes condiciones o estímulos. A continuación, se definen los parámetros obtenidos para el filtrado de las señales EMG a partir de la literatura de referencia. <sup>[12](https://doi.org/10.1016/j.jelekin.2013.05.001)</sup> 

<div align="center">
	
|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** | **Coeficientes de detalle** | 
|:------------:|:---------------:|:------------:|:------------:|:------------:|:------------:|
|Bior1.5 (Biorthogonal 1.5)|7|16|500 Hz|A7| D1, D2, D3, D4, D5, D6, D7|
<p align="center"><i>Tabla 3. Parámetros considerados para el diseño del filtro en la señal EMG </i></p>

</div>

#### SEÑAL EEG

Se consideró el uso de las señales de electroencefalograma (EEG) obtenidas en el Laboratorio 05 para el filtrado con la transformada wavelet, las cuales se obtuvieron en diferentes estados: reposo, durante el parpadeo, reposo tras el parpadeo y mientras se realizaba y respondía preguntas matemáticas (razonamiento).

**a. Estado de reposo**: El sujeto de prueba se quedó en una posición estable y manteniendo la calma para el registro de una línea base de señal con poco ruido y sin movimientos. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Estado de ojos cerrado-ojos abiertos**: El sujeto mantuvo los ojos cerrados y abiertos completando un ciclo (5 veces cada estado), manteniendo ambas fases durante 5 segundos. Para evitar artefactos, el sujeto se mantuvo calmado y mirando hacia un punto específico. El registro de la señal fue grabado por 50 segundos.

**c. Estado de segundo reposo**: Tras la primera actividad, el sujeto de prueba mantuvo nuevamente el estado de calma y sin movimiento como segunda fase de referencia. El registro de la señal fue grabado por 30 segundos.

**d. Estado de preguntas**: Se realizaron una serie de ejercicios matemáticos de menor a mayor complejidad al sujeto de prueba para que pueda resolverlo mentalmente enfocando su mirada en un punto específicos para evitar artefactos. La duración entre el lapso de registro de la respuesta y la siguiente pregunta fue de 12 segundos. Las preguntas realizadas se observan en la Tabla 4.

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

<p align="justify">El filtro utilizado para la eliminación de ruido en la señal es un filtro DWT tipo Biorthogonal 2.6, debido a su alta simetría, capacidad de separar eficazmente los componentes de frecuencia baja y alta y reconstrucción de la señal original y un nivel de 5. Los coeficientes de aproximación fueron A5 y de detalle D1, D2, D3, D4 y D5. El umbral fue calculado mediante umbralización suave y fue optimizado mediante pruebas. Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada con el DWT para observar la eficiencia del filtrado. A continuación, se definen los parámetros obtenidos para el filtrado de las señales EEG a partir de la literatura de referencia <sup>[13](http://dx.doi.org/10.1109/I2CT51068.2021.9417984)</sup>.

<div align="center">
	
|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** | **Coeficientes de detalle** | 
|:------------:|:---------------:|:------------:|:------------:|:------------:|:------------:|
|bior2.6 (Biorthogonal 2.6)|5|16|1000 Hz|A5| D1, D2, D3, D4, D5|
<p align="center"><i>Tabla 5. Parámetros considerados para el diseño del filtro en la señal EEG </i></p>

</div>

<a name="resultados"></a>
## Resultados

<a name="ecg"></a>
### SEÑAL ECG
Como vemos en las señales obtenidas luego del filtrado, podemos que el filtro si tuvo eficiencia en reducción del ruido, pero bastante leve. En el estado de reposo, podemos observar que la Wavelet logró atenuar levemente los picos observados, pero no se observó un resultado significativo. En el caso de la respiración prolongada, es donde se ve la mayor diferencia, entre la señal original y la Wavelet, en donde se observa notoriamente una disminución del ruido. Y finalmente, en el estado de reposo intensivo, también se puede observar un filtrado de ruido pero muy leve. En general, se observa disminución de ruido, pero no tan significativa, esto puede deberse a la presencia de artefactos durante la toma de muestras.
<div align="center">

|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Reposo|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/4c36a03d-cdab-4f23-8ba5-780565977bef">|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/abf43e2f-09c3-40f4-9c06-c6090826181f">|
|Respiración prolongada|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/b5eea10c-0274-46a4-8b2e-f815d54396a7">|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/fe0e464a-9261-4ed6-a115-ce2338d929d4">|
|Ejercicio Intensivo|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/3f382fb8-517b-4560-bf83-e0459176a7d6">|<image width="400" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/75068877-a29e-40e7-942e-039f3b79bf3b">|
<p align="center"><i>Tabla 6. Resumen de la señal filtrada con DWT para la data ECG </i></p>
</div>
<a name="emg"></a>


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
A partir de las señales filtradas obtenidas, se observa que el filtro diseñado tuvo una eficiencia significativa en la reducción del ruido generado. En el estado de reposo, observamos que el filtro aplicado logró suavizar los picos, los cuales fueron generados por artefactos durante el estado de ojos cerrados del sujeto de prueba, posiblemente debido a movimientos oculares rápidos o alteraciones en el pensamiento. Se elegió definir el tiempo entre los 10-13 segundos debido a que fue la sección con menores fluctuaciones de picos extremos registrada durante ese estado. En el estado de parpadeo, se observa el efecto del filtrado con DWT, sin embargo, no presentó un resultado significativo. Esto puede deberse posiblemente por la presencia de mayores artefactos durante la toma de este estado o que en los picos se presentó mayores niveles de excitación, por lo que el filtro diseñado no fue el ideal. Se elegió definir el tiempo entre los 3-6 segundos debido a que fue la sección que presentaba fracción del tiempo del estado de ojos cerrados y fracción del tiempo de estado de ojos abiertos (picos de mayor amplitud) registrada durante ese estado. Por último, durante el estado de razonamiento de preguntas matemáticas, se observa que sí hubo un filtrado apropiado específicamente en los picos extremos. Se elegió definir el tiempo entre los 36-42 segundos debido a que fue la sección que presentaba el estado de preguntas sencillas y fracción del tiempo de estado de preguntas que implicaban un mayor razonamiento matemático.

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
  - [ECG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/C%C3%B3digos/ECG.py)
  - [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/d22284eac044bb34acde6b8b07a34325d813988b/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/C%C3%B3digos/emg_wavelet.py)
  - [EEG](https://github.com/sofiacespedes22/ISB_2024_G8/blob/db4939c9ee53fb066a803574d1a96906d5e0938c/4.ISB/LABORATORIOS/Laboratorio%2007_Filtrado%20Wavelet/C%C3%B3digos/eeg_wavelet.py)

<a name="discusion"></a>
## Discusión
En el caso de la señal de ECG, el filtro empleado es un DDDTDWT, o Transformada Wavelet Discreta en Dos Dimensiones con Umbral Doble, el cual es una técnica de procesamiento de señales ampliamente utilizada en el análisis y la mejora de señales, como en el caso específico de señales de ECG. Esta técnica se basa en la descomposición de la señal en diferentes escalas y niveles de detalle, lo que permite una representación más eficiente de la información tanto en el dominio temporal como en el de frecuencia <sup> [14](http://dx.doi.org/10.1109/IIH-MSP.2009.148)</sup> <sup> [15](http://dx.doi.org/10.1109/TSP.2004.826174)</sup>. Nuestro filtro DDDTDWT cuenta con un nivel de descomposición de 8 y un umbral de 10 a la señal de ECG, porque lo que pudimo aprovechar varias de sus características distintivas. En primer lugar, este filtro demuestra una habilidad notable para preservar las características fundamentales de la señal mientras elimina eficazmente el ruido no deseado. Esto se traduce en una mejora evidente en la claridad y la interpretabilidad de la señal procesada, lo que facilita su análisis y diagnóstico. Asimismo, puede adaptarse a la estructura temporal de la señal. Esto significa que puede capturar tanto los detalles de alta frecuencia como las tendencias de baja frecuencia presentes en la señal de ECG, lo que resulta en una eliminación de ruido más selectiva y efectiva.

El filtrado de la señal EMG fue más efectivo en el abductor corto del pulgar que en el bíceps braquial debido a varias razones fisiológicas y técnicas. El abductor corto del pulgar, siendo un músculo más pequeño y localizado, experimenta menor interferencia de músculos adyacentes y presenta movimientos menos complejos, lo que reduce significativamente los artefactos y el ruido en la señal. Además, su ubicación superficial y menor profundidad permiten una captación más precisa de la señal por los electrodos. En contraste, el bíceps braquial, al estar rodeado de músculos grandes y estar involucrado en movimientos más amplios, genera señales con mayor ruido e interferencias, lo que dificulta una filtración tan eficaz.

La definición del umbral es un factor crítico en el diseño del filtro wavelet pues un umbral muy pequeño o uno muy grande podría influir en los estimadores de contracción de ondas, pues podría sobre/no ajustar la data <sup> [16](https://doi.org/10.1007/978-1-4612-2544-7_16)</sup>. El método utilizado para el cálculo del umbral, como se observa en la Fórmula 1 propuesto por Donoho y Johnstone <sup> [17](https://doi.org/10.1093/biomet/81.3.425)</sup> garantiza la reconstrucción de la señal filtrada del ruido, sin embargo, suele no ajustar los datos <sup> [18](https://www.academia.edu/109301514/Adaptation_to_high_spatial_inhomogeneity_using_wavelet_methods)</sup>. Esto podría explicar los resultados obtenidos previamente, pues si bien el umbral utilizado era relativamente elevado, no se realizaba un filtrado óptimo para las señales EEG. Como se observó en los resultados de ECG, EMG o EEG, la presencia de niveles de excitación en los picos y la presencia de ruido de mayores frecuencias debido a una mayor presencia de artefactos dificultó el filtrado apropiado ante el umbral calculado. Asimismo, al aplicar un valor de umbral menor a 1 para las señales EMG y EEG, se observaba un cambio nulo o no significativo en el filtrado de la señal por lo que se tuvo que realizar pruebas en el cálculo y en la programación para obtener una señal filtrada significativamente sin pérdida de información relevante. Esto indica que el proceso y protocolo de adquisición de las señales biomédicas es de suma relevancia pues nos permite un mejor entendimiento de la información provista y evitar complicaciones en el proceso de filtrado, pues elegir un umbral alto podría resultar en la pérdida de información relevante de la señal para su aplicación futura.

## Conclusiones
* El filtro utilizado en señales de ECG fue eficaz para preservar características fundamentales de la señal como el complejo QRS mientras elimina ruido no deseado, mejorando la interpretabilidad.
* En señales EMG, el filtrado es más efectivo en el abductor corto del pulgar debido a menor interferencia de músculos adyacentes y una ubicación superficial que facilita una captación más precisa en comparación al bíceps.
* La definición del umbral es crítica en el diseño del filtro DWT, ya que un umbral incorrecto puede sobreajustar o no ajustar adecuadamente los datos, afectando la calidad del filtrado y eliminando información importante.
* El protocolo de adquisición para señales biomédicas es esencial para asegurar una filtración óptima y evitar la pérdida de información relevante.

<a name="referencias"></a>
## Referencias bibliográficas

[1] P. M. Bentley and J. T. E. McDonnell, “Wavelet transforms: an introduction,” Electronics & Communication Engineering Journal, vol. 6, no. 4, pp. 175–186, Aug. 1994, doi: https://doi.org/10.1049/ecej:19940401.

[2] R. Madan, S. K. Singh and N. Jain, "Signal Filtering Using Discrete Wavelet Transform," International Journal of Recent Trends in Engineering, vol. 2, (3), pp. 96-98, 2009. Available: https://www.proquest.com/scholarly-journals/signal-filtering-using-discrete-wavelet-transform/docview/603852467/se-2.

[3] C. S. Burrus, R. Gopinath, and H. Guo, “Wavelets and Wavelet Transforms OpenStax-CNX,” 2015. Available: https://repository.rice.edu/bitstreams/33cd90c3-b6c6-4a7e-ab6f-dbc34e868d9b/download

[4] L. Chun-Lin, “A tutorial of the wavelet transform,” NTUEE Taiwan, vol. 21, no. 22, p. 2, 2010.

[5] PLUX – Wireless Biosignals, “BITalino (r)evolution Lab Guide,” Feb. 2021. Available: https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/

[6] M. Balamareeswaran and D. Ebenezer, "Denoising of EEG signals using discrete wavelet transform based scalar quantization," Biomed. Pharma. J., vol. 8, no. 1, pp. 399–406, 2015. DOI: http://dx.doi.org/10.13005/bpj/627

[7] M. S. Choudhry and R. Kapoor, "A survey on different discrete wavelet transforms and thresholding techniques for EEG denoising," in International Conference on Computing, Communication, and Automation, Greater Noida, India, pp. 29–30 April, 2016. DOI: https://doi.org/10.1109/CCAA.2016.7813897

[8] S. Jothimani and A. Suganya, "Denoising of EEG gesture using DWT," Int. J. Recent Tech. Eng., vol. 7, no. 6S4, pp. 522–527, 2019.

[9] S. Kaur and S. Malhotra, "Various techniques for denoising EEG signal: a review," Int. J. Eng. Comp. Scie., vol. 3, no. 8, pp. 7965–7973, 2014. Link: http://www.ijecs.in/index.php/ijecs/article/download/1393/1279/2481

[10] D. L. Donoho and I. M. Johnstone, "Ideal spatial adaptation by wavelet shrinkage," Biometrika, 1994. doi: https://doi.org/10.1093/biomet/81.3.425

[11] “Analysis of ECG signal denoising using discrete wavelet transform,” IEEE Conference Publication | IEEE Xplore. https://ieeexplore.ieee.org/document/7569341

[12] S. K. Chowdhury, A. D. Nimbarte, M. Jaridi, and R. C. Creese, “Discrete wavelet transform analysis of surface electromyography for the fatigue assessment of neck and shoulder muscles,” Journal of Electromyography and Kinesiology, vol. 23, no. 5, pp. 995–1003, Oct. 2013, doi: https://doi.org/10.1016/j.jelekin.2013.05.001.

[13] A. W. Pise and P. P. Rege, "Comparative Analysis of Various Filtering Techniques for Denoising EEG Signals," 2021 6th International Conference for Convergence in Technology (I2CT), Maharashtra, India, 2021, pp. 1-4, doi: http://dx.doi.org/10.1109/I2CT51068.2021.9417984

[14] Yu-Long Qiao., “Double-Density Dual-Tree Wavelet Transform Based Texture Classification”, Fifth International Conference on Intelligent Information Hiding and Multimedia Signal Processing, September 2009. DOI: http://dx.doi.org/10.1109/IIH-MSP.2009.148

[15] I. W. Selesnick, “The double-density dual-tree DWT”, IEEE Trans. on Signal Processing, 52(5): pp. 1304-1314, May 2004. DOI: http://dx.doi.org/10.1109/TSP.2004.826174

[16] G. P. Nason, "Choice of the Threshold Parameter in Wavelet Function Estimation," in Wavelets and Statistics, A. Antoniadis and G. Oppenheim, Eds., Lecture Notes in Statistics, vol. 103, New York, NY: Springer, 1995. doi: https://doi.org/10.1007/978-1-4612-2544-7_16

[17] D. L. Donoho and I. M. Johnstone, "Ideal spatial adaptation by wavelet shrinkage," Biometrika, 1994. doi: https://doi.org/10.1093/biomet/81.3.425

[18] J. Fan, P. Hall, M. Martin, and P. Patil, "Adaption to high spatial inhomogeneity based on wavelets and on local linear smoothing," Tech. Rep. CMA-SR18-93, Centre for Mathematics and Its Applications, Australian National University, Canberra, 1993. Link: https://www.academia.edu/109301514/Adaptation_to_high_spatial_inhomogeneity_using_wavelet_methods



