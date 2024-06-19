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
## **INTRODUCCIÓN**
### **CONTEXTO**


<a name="marco"></a>
### **MARCO TEÓRICO**
#### EEG
El EEG mide la actividad eléctrica del cerebro, registrada en el cuero cabelludo, a partir de impulsos generados por las células nerviosas corticales. Estos impulsos producen señales con amplitudes de entre 10 y 100 µV y frecuencias de 1 a 100 Hz. Esta técnica no invasiva es crucial para diagnosticar diversas enfermedades neurológicas, como epilepsia, tumores y lesiones cerebrovasculares. Sin embargo, los resultados pueden verse afectados por artefactos debido a la naturaleza compleja y no lineal de las señales eléctricas cerebrales. <sup>[a](https://doi.org/10.1007/s10916-008-9231-z)</sup>

</div>
<p align="center">
<image width="260" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/70b9488a9578f60327302e3cf2d00b15a86e01dc/4.ISB/LABORATORIOS/Laboratorio%2010_Procesamiento%20EEG/Im%C3%A1genes/EEG.jpg">
<p align="center"><i>Figura 1: Señal EEG.</i></p>
</div>

#### Ondas Cerebrales
Las ondas cerebrales son fundamentales para diagnosticar trastornos neurológicos a través del EEG. En adultos sanos, las frecuencias y amplitudes de las ondas cerebrales varían según el estado de vigilia o sueño y con la edad. Los principales tipos de ondas cerebrales son: delta (0.5-4 Hz), asociadas con el sueño profundo; theta (4-7.5 Hz), relacionadas con la somnolencia y la meditación; alfa (8-13 Hz), vinculadas con la relajación y la atención pasiva; beta (14-26 Hz), asociadas con la atención activa y la resolución de problemas; y gamma (>30 Hz), relacionadas con la sincronización cerebral en eventos específicos. La identificación precisa de estos ritmos es crucial y puede mejorarse con herramientas avanzadas de procesamiento de señales. <sup>[b](http://dx.doi.org/10.1002/9780470511923)</sup>

</div>
<p align="center">
<image width="260" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/70b9488a9578f60327302e3cf2d00b15a86e01dc/4.ISB/LABORATORIOS/Laboratorio%2010_Procesamiento%20EEG/Im%C3%A1genes/OndasCerebrales.jpg">
<p align="center"><i>Figura 2: Ondas cerebrales típicas, ordenados de frecuencias altas a bajas.</i></p>
</div>

#### Adquisición
Adquirir señales del cuerpo humano, como el EEG, es esencial para el diagnóstico temprano de enfermedades. El EEG es preferido sobre fMRI y MEG por su alta resolución temporal y menor costo.
Los sistemas EEG actuales utilizan múltiples electrodos, amplificadores diferenciales y conversión digital, con frecuencias de muestreo de 200 a 2000 muestras/s y cuantización fina para asegurar precisión diagnóstica. El almacenamiento de datos requiere gran capacidad; una hora de grabación de 128 electrodos necesita aproximadamente 0.45 GB. <sup>[b](http://dx.doi.org/10.1002/9780470511923)</sup>

##### A. Posicionamiento Convencional de Electrodos
El sistema 10-20 es el estándar para colocar 21 electrodos de manera consistente basada en puntos anatómicos <sup>[c](https://doi.org/10.1016/0013-4694%2858%2990053-1)</sup>. Este sistema permite la expansión con más electrodos para estudios detallados. Se utilizan modos de grabación diferencial y referencial, con referencias comunes como Cz, orejas conectadas o la punta de la nariz .<sup>[d](https://scholar.google.com/scholar_lookup?title=Encyclopedia+of+Neuroscience&author=RD+Bickford&publication_year=1987&)</sup>  <sup>[b](http://dx.doi.org/10.1002/9780470511923)</sup>

</div>
<p align="center">
<image width="260" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/70b9488a9578f60327302e3cf2d00b15a86e01dc/4.ISB/LABORATORIOS/Laboratorio%2010_Procesamiento%20EEG/Im%C3%A1genes/posicionElectrodos.jpg">
<p align="center"><i>Figura 3 Posiciones convencionales de electrodos 10-20 para la colocación de 21 electrodos.</i></p>
</div>

##### B. Acondicionamiento de Señales
Las señales EEG crudas, con amplitudes en microvoltios y frecuencias de hasta 300 Hz, requieren amplificación y filtrado para eliminar ruido y retener información útil. Se usan filtros pasaaltos para remover componentes de baja frecuencia, filtros pasabajos para reducir ruido de alta frecuencia y filtros de muesca para eliminar interferencias de suministro eléctrico. Las frecuencias de muestreo comunes son 100, 250, 500, 1000 y 2000 muestras/s. <sup>[b](http://dx.doi.org/10.1002/9780470511923)</sup>

##### C. Ultracortex Mark IV
El Ultracortex Mark IV es un casco EEG desarrollado por OpenBCI que optimiza la adquisición de señales neuronales mediante una estructura modular y personalizable. Utiliza electrodos de gel, secos o semi-secos, lo que permite flexibilidad según las necesidades experimentales. Los electrodos de gel proporcionan una excelente conductividad, mientras que los secos permiten un montaje rápido y limpio. La colocación de los electrodos sigue el sistema internacional 10-20, asegurando una cobertura completa y precisa de la actividad cerebral.
La estabilidad del casco durante la adquisición de datos minimiza el ruido y los artefactos, garantizando la calidad de las señales EEG. Su compatibilidad con las placas de adquisición OpenBCI, como la Cyton y la Ganglion, facilita el procesamiento y análisis de los datos recogidos. El diseño ajustable del Ultracortex Mark IV asegura un contacto óptimo entre los electrodos y el cuero cabelludo, proporcionando datos fiables y de alta calidad. <sup>[e](https://docs.openbci.com/AddOns/Headwear/MarkIV/)</sup>


</div>
<p align="center">
<image width="260" height="250"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/70b9488a9578f60327302e3cf2d00b15a86e01dc/4.ISB/LABORATORIOS/Laboratorio%2010_Procesamiento%20EEG/Im%C3%A1genes/UltraCortex.jpg">
<p align="center"><i>Figura 4. Ultracortex Mark IV.</i></p>
</div>

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
Para el procedimiento del procesamiento de las señales EEG, se utilizó un artículo de referencia el cual presenta un análisis de las señales EEG para el diagnóstico de desórdenes neurológicos utilizando la transformada wavelet (DWT) y técnicas de filtrado y clasificación <sup>[x](https://doi.org/10.3390/s20092505)</sup>. Las señales fueron previamente pre-procesadas mediante el uso de filtros, sus características fueron extraídas y se utilizaron técnicas de clasificación de vectores. Se combinaron técnicas dentro de la extracción de características como la banda de potencia logarítmica, desviación estándar, varianza, kurtosis y entropía de Shannon, utilizando clasificadores de diferentes tipos. Se presenta, a continuación, un diagrama de bloques que ejemplifica el procesamiento de las señales basadas en DWT.

</div>
<p align="center">
<image width="600" height="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164461832/94395227-58c9-49f7-ade4-45aa67303d9f"><p align="center"><i>Figura x. Diagrama de bloques del procedimiento a seguir basado en la literatura [x] </i></p>
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
<image width="600" height="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/d542cf0f9bbc912fd5ee4e3baaeeb29211e277f1/4.ISB/LABORATORIOS/Laboratorio%2010_Procesamiento%20EEG/Im%C3%A1genes/feature%20extracion.jpg"> <p  align="center"><i>Figura y. Descomposición de la señal mediante el DWT 4 niveles [x] </i></p>
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
[x] F. A. Alturki, K. AlSharabi, A. M. Abdurraqeeb, y M. Aljalal, "EEG Signal Analysis for Diagnosing Neurological Disorders Using Discrete Wavelet Transform and Intelligent Techniques," Sensors (Basel, Switzerland), vol. 20, no. 9, p. 2505, 2020. [Online]. Disponible: https://doi.org/10.3390/s20092505.

[a] D. P. Subha, P. K. Joseph, R. Acharya U, and C. M. Lim, “EEG signal analysis: A survey,” J. Med. Syst., vol. 34, no. 2, pp. 195–212, 2010.
[b] S. Sanei and J. A. Chambers, EEG signal processing. Wiley, 2007.
[c]  Jasper, H., ‘Report of committee on methods of clinical exam in EEG’, Electroencephalogr. Clin. Neurophysiol., 10, 1958, 370–375.
[d] Bickford, R. D., ‘Electroencephalography’, in Encyclopedia of Neuroscience, Ed. G. Adelman,
Birkhauser, Cambridge (USA), 1987, 371–373.
[e] “Ultracortex Mark IV,” Openbci.com. [Online]. Available: https://docs.openbci.com/AddOns/Headwear/MarkIV/. [Accessed: 19-Jun-2024].

