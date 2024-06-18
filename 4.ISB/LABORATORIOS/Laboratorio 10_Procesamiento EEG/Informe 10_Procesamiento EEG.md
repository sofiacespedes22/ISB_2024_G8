# Laboratorio N°9 - Procesamiento de señales ECG
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
* Investigar literatura científica sobre técnica de procesamiento de señales electrocardiográficas (ECG).
* Identificar e implementar la mejor técnica filtrado para eliminar el ruido de las señales ECG.
* Extraer picos de las ondas R y calcular el HRV de las señales ECG en diferentes dominios.

<a name="metodologia"></a>
## METODOLOGÍA 
Para este laboratorio, se utilizarán datos de señales ECG adquiridas por el BITalino en la sesión de laboratorio 05. El proceso de adquisición se llevó a cabo siguiendo un protocolo estándar utilizando el dispositivo BITalino y el programa OpenSignal. Inicialmente, se estableció la conexión entre el BITalino y OpenSignal mediante Bluetooth para visualizar las señales en tiempo real. Luego, se conectó el sensor ECG de 3 electrodos al BITalino para comenzar la adquisición de señales.

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

#### Pre-procesamiento
En esta sección, se describen las técnicas propuestas de extracción de características y clasificación, así como su validación utilizando herramientas de software MATLAB (MathWorks, Natick, MA, EE. UU.). El diagrama de bloques del método propuesto se muestra en la Figura 1, que resalta los métodos propuestos basados en DWT. En este diagrama, los datos de EEG se leen primero y luego se eliminan los artefactos oculares de las señales registradas mediante la técnica ICA. Después del proceso de eliminación de artefactos, las señales de EEG se segmentarán en ventanas de tiempo fijas de 50 s. A continuación, se alimenta la salida del proceso de segmentación a un filtro paso-banda para eliminar los ruidos. En esta etapa de preprocesamiento, se utilizan tanto técnicas de filtro adaptativo como ICA para eliminar artefactos oculares, con señales de referencia registradas desde cuatro electrodos alrededor de los ojos para eliminar los parpadeos oculares. Posteriormente, el conjunto de datos de EEG se divide en segmentos iguales para asegurar que la cantidad de información sea igual en cada segmento. En este estudio, se selecciona una longitud de segmento de 50 s porque produce mejores resultados experimentales. Después de segmentar las señales de EEG, los segmentos de EEG se filtran para eliminar los ruidos e interferencias generados durante la grabación de las señales de EEG. La técnica de filtrado tiene como objetivo eliminar todo el ruido e interferencia, mejorando la relación señal-ruido para mejorar y aumentar los resultados de precisión de la clasificación. Se utilizaron diferentes métodos de filtrado, como filtros de respuesta finita al impulso (FIR) (Equiripple, Kaiserwin, etc.) y filtros de respuesta infinita al impulso (IIR) (Chebyshev I, Chebyshev II, Butterworth, Elíptico, etc.). Sin embargo, el filtro paso-banda elíptico (0.1–60 Hz) proporciona mejores resultados experimentales en comparación con los otros tipos de filtros, ya que la implementación del filtro elíptico requiere menos memoria, menos cálculos y proporciona un tiempo de retraso reducido.

#### Extracción de características
El método de extracción de características es importante para el procesamiento de señales de EEG para lograr el mejor rendimiento posible. Las señales de EEG se registran y segmentan en series de tiempo largas, lo cual es necesario para trabajar con un número muy pequeño de valores que describen las características de la señal de EEG. Estos valores se llaman características y se agrupan en un vector llamado vector de características. Así, los métodos de extracción de características se definen como las técnicas que transforman señales en un vector de características. Hay varios tipos de técnicas de extracción de características utilizadas para extraer características. En el presente trabajo, se ha utilizado la tecnología más popular y extendida, es decir, DWT. En este estudio, se propone el uso de DWT basado en LBP, SD, varianza, curtosis y entropía para formar los vectores de características. La STFT no es adecuada para analizar señales no estacionarias, como las EEG, ya que ofrece una resolución constante en todas las frecuencias. Para analizar diferentes frecuencias con diferentes resoluciones, se emplea la técnica de transformada wavelet, que utiliza multi-resolución. Además, la transformada wavelet puede ofrecer un menor número de características para la señal a procesar, lo que implica que puede ser adecuada para evitar el problema asociado a la dimensionalidad. Así, las transformadas wavelet analizan las características de la señal en los dominios del tiempo y la frecuencia descomponiendo dichas señales en varias funciones utilizando una función única llamada función madre.

En este trabajo, se empleó DWT porque proporciona una representación wavelet altamente eficiente. En la descomposición de primer nivel, se utilizan con frecuencia filtros paso-bajo y paso-alto para obtener la representación de la señal digital como coeficientes de aproximación (A1) y detalle (D1). En el primer nivel, los coeficientes de aproximación se descomponen en coeficientes de aproximación (A2) y detalle (D2) en el segundo nivel. En el tercer nivel, los coeficientes de aproximación en el segundo nivel se descomponen en coeficientes de aproximación (A3) y detalle (D3). Finalmente, los coeficientes de aproximación en el tercer nivel se descomponen en coeficientes de aproximación (A4) y detalle (D4) en el cuarto nivel. Después de obtener todos los coeficientes de detalle en cada nivel (D1, D2, D3 y D4) y los coeficientes de aproximación en el último nivel (A4), se probaron diferentes combinaciones de estos coeficientes para obtener el mejor resultado. Sin embargo, la mayor precisión general de clasificación se logró utilizando todos ellos.

#### Clasificación
In the proposed system, linear discriminant analysis LDA, SVM, KNN, and ANN techniques were applied as classifiers. We implemented and verified all possible combinations of the proposed methods. Both LDA and SVM classification techniques use hyperplane separation to classify their inputs. In the present study, we used a linear SVM because a non-linear SVM is expected to have higher computational costs and longer computation time. The KNN classifier is the simplest machine-learning algorithm and distinguishes objects by a majority vote of its k-nearest neighbors. In the current work, k is selected to equal five for all experiments. We have also used ANN as a classifier, which is an information-processing system that simulates the process of human cognition. During the training process, the feature vectors are applied to the network to adjust its variable parameters, weights, and biases.


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
