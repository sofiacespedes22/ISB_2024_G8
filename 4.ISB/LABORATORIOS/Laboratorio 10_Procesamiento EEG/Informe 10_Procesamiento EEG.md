# Laboratorio N°10 - Procesamiento de señales EEG
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


## OBJETIVOS
* Investigar literatura científica sobre técnica de procesamiento de señales electroencefalográficas (EEG).
* Identificar e implementar la mejor técnica filtrado para eliminar el ruido de las señales EEG.

<a name="metodologia"></a>
## METODOLOGÍA 
Para este laboratorio, se utilizarán las señales obtenidas del Ultracortex Mark IV, en el cuál se utilizó el sistema 10-20 para el posicionamiento de los electrodos, como se observa en la Figura A. Asimismo, la adquisición de las señales obtenidas fue registrada en OpenBCI para su posterior análisis. La conexión fue realizada a un sujeto de prueba (mujer, 22 años, condición sana) de un equipo de trabajo distinto al nuestro debido a complicaciones con el manejo del tiempo para el uso. 

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1572adee-70d4-4bde-9c4e-e38c0ed51ea3">
<p align="center"><i>Figura A. Posicionamiento de los electrodos según el sistema 10-20.</i></p>
</div>

   
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
Para el procedimiento del procesamiento de las señales EEG, se utilizó un artículo de referencia el cual presenta un análisis de las señales EEG para el diagnóstico de desórdenes neurológicos utilizando la transformada wavelet (DWT) y técnicas de filtrado y clasificación [x]. Las señales fueron previamente pre-procesadas mediante el uso de filtros, sus características fueron extraídas y se utilizaron técnicas de clasificación de vectores. Se combinaron técnicas dentro de la extracción de características como la banda de potencia logarítmica, desviación estándar, varianza, kurtosis y entropía de Shannon, utilizando clasificadores de diferentes tipos. Se presenta, a continuación, un diagrama de bloques que ejemplifica el procesamiento de las señales basadas en DWT.

</div>
<p align="center">
<image width="400" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164461832/94395227-58c9-49f7-ade4-45aa67303d9f"><p align="center"><i>Figura x. Diagrama de bloques del procedimiento a seguir basado en la literatura [x] </i></p>
</div>


#### Pre-procesamiento
Para el pre-procesamiento de la señal que presentaba artefactos, ruidos e interferencias de diversas fuentes, se aplicó la técnica ICA y filtros adaptativos para eliminar para eliminar los artefactos oculares de las señales registradas. Posteriormente, las señales fueron segmentadas en ventanas de tiempo de 50 s. Luego de la segmentación, se aplicó un filtrado pasa banda, que incluyo filtros FIR e IIR (Chebyshev, Butterworth).

#### Extracción de características
Para la extracción de características, se utilizó la DWT basado en LBP, desviación estándar, varianza, kurtosis y entropía para formar los vectores de características, que se observan en la Tabla 2. La DWT fue empleada debido a que proporciona una representación wavelet altamente eficiente. Se empleó la familia Daubechies 4 (db4) como la función wavelet madre de nivel 4 (ver Figura Y). En la descomposición de primer nivel, se utilizó filtros paso-bajo y paso-alto para obtener la representación de la señal digital como coeficientes de aproximación (A1) y detalle (D1). Los coeficientes de aproximación y detalle en cada nivel fueron seleccionados después de obtener todos los coeficientes de detalle en cada nivel (D1, D2, D3 y D4) y los coeficientes de aproximación en el último nivel (A4).

<div align="center">

|  **Nombre**  | **Descripción** | **Fórmula** |
|:------------:|:---------------:|:------------:|
|Varianza|La varianza mide la dispersión de las muestras de la señal alrededor de su media|$$V_s = \frac{1}{N} \sum_{n=1}^{N} (S(n) - \mu_s)^2$$|
|Desviación estándar|La desviación estándar es una medida de la cantidad de variación o dispersión de un conjunto de valores|$$\sigma_s = \sqrt{\frac{1}{N} \sum_{n=1}^{N} (S(n) - \mu_s)^2}$$|
|Kurtosis|La kurtosis de la señal mide la "agudeza" de la distribución de los valores de la señal. Una kurtosis alta indica una distribución con picos más afilados, mientras que una baja indica una distribución más plana|$$kurt = E \left[ \left( \frac{S(n) - \mu_s}{\sigma_s} \right)^4 \right]$$|
|Entropía|La entropía espectral no normalizada mide el grado de desorden o incertidumbre en la señal|$Ent = \sum_{n=1}^{N}(S(n))^2 \log(S(n))^2$|
|LBP|LBP de la señal mide la textura o estructura local de la señal|$$LBP = \log \left( \frac{1}{N} \sum_{n=1}^{N} (S(n))^2 \right)$$|

<p align="center"><i>Tabla 2. Parámetros de la extracción de características de la señal EEG</i></p>
</div>


</div>
<p align="center">
<image width="400" height="200" src=""> <p  align="center"><i>Figura y. Descomposición de la señal mediante el DWT 4 niveles [x] </i></p>
</div>


#### Clasificación
Por último, para la clasificación, se emplearon como clasificadores las técnicas de análisis discriminante lineal LDA, SVM, KNN y ANN. Durante el proceso de entrenamiento del algoritmo, los vectores de características se aplican a la red para ajustar sus parámetros variables, pesos y sesgos.

<a name="resultados"></a>
## RESULTADOS
### Estado de reposo


### Estado de respiración prolongada


### Estado de ejercicio intensivo


<a name="archivos"></a>
## ARCHIVO DE LA SEÑAL PLOTEADA EN PYTHON
* **Codigo**
  - []()

<a name="discusion"></a>
## Discusión

<a name="conclusion"></a>
## Conclusión


<a name="referencias"></a>
## REFERENCIAS BIBLIOGRÁFICAS
