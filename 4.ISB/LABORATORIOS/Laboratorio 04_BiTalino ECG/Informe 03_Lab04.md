# LABORATORIO N°2 - Adquisición de señales de electrocardiograma (ECG) con BITalino
## Tabla de contenidos
1. [Lista de participantes](#lista)
2. [Introducción](#introduccion)\
   2.1 [Marco teórico](#marco)
3. [Objetivos](#objetivos)
4. [Metodología](#metodologia)\
   2.1 [Materiales y equipos](#materiales)\
   2.2 [Adquisición de datos](#adquisicion)\
   2.3 [Procesamiento de las señales](#procesamiento)
5. [Resultados](#resultados)\
   3.1 [Resultados obtenidos](#)\
   3.2 [Archivos](#)\
   3.2 [Ploteo de la señal en Python](#)\
   3.3 [Señal en Prosim4](#)
6. [Archivos de la señal ploteada en Python y de los datos de la señal](#phyton)
   - [Señales ploteadas en python](#r3)
   - [Datos de la señal ploteada](#r4)
7. [Discusión](#discusion)
8. [Conclusiones](#conclusiones)
9. [Referencias bibliográficas](#referencias)

<a name="lista"></a>
## Lista de participantes
- Sofia Camila Céspedes Trece - 71738148
- Nicole Stefany Acuña Malpartida - 71400976
- Chris Margory Viviano Salvatierra - 75138288
- Harold Alonso Alemán Ramírez - 71386429
  
<a name="introduccion"></a>
## Introducción
El electrocardiograma (ECG) representa la actividad eléctrica del corazón, siendo esencialmente una traducción gráfica de este fenómeno. Este proceso implica la detección de ondas P-QRS-T mediante electrodos ubicados en puntos estratégicos del cuerpo del paciente. Incluso pequeñas alteraciones en estas señales pueden ayudar a determinar o detectar una variedad de condiciones y aspectos relacionados con la salud del corazón <sup>[1](https://ieeexplore.ieee.org/document/8704365)</sup>.Este procedimiento no invasivo es útil para:

- Identificar ritmos cardíacos irregulares, como las arritmias.
- Evaluar si las arterias obstruidas o estrechas del corazón, como en la enfermedad de las arterias coronarias, están ocasionando dolor de pecho o un ataque cardíaco.
- Determinar antecedentes de ataques cardíacos previos.
- Evaluar la eficacia de ciertos tratamientos para enfermedades cardíacas, como el funcionamiento de un marcapasos. <sup>[2](https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983#:~:text=Electrocardiograma-)</sup>

Por eso mismo, el análisis temporal de la señal de ECG proporciona información valiosa para el diagnóstico cardiovascular. Partiendo de ese punto, en este laboratorio se explora el uso de la placa de desarrollo BITalino, destacada por su eficacia en la adquisición de señales de ECG gracias a su precisa capacidad para medir la actividad eléctrica del corazón. En este proceso, resulta crucial comprender la técnica adecuada de colocación de electrodos, así como identificar las ubicaciones exactas donde deben ser colocados, junto con los cables de medición (IN+/-) y el cable de referencia (REF). Esta configuración permite una transmisión precisa de la actividad eléctrica captada por los electrodos al dispositivo para su registro y análisis. La versatilidad y precisión del BITalino lo posicionan como una elección óptima tanto para investigaciones médicas como para aplicaciones de monitoreo de la salud cardiovascular. <sup>[3](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>
	
A través de esta experiencia práctica, se espera aprender sobre la obtención y análisis de señales ECG, así como familiarizarse con los procedimientos y protocolos de utilización de electrodos ECG, aprovechando la versatilidad y precisión del BITalino como una elección óptima tanto para investigaciones médicas como para aplicaciones de monitoreo de la salud cardiovascular.

<a name="marco"></a>
### Marco teórico
#### a. Señal ECG
La morfología de la señal de ECG se caracteriza por varios elementos clave: la onda P, el complejo QRS, la onda T y los intervalos entre ellos.

* La onda P indica la despolarización auricular.
* El complejo QRS señala la despolarización ventricular sincronizada.
* La onda T refleja la repolarización ventricular, mientras que la onda U se presenta posteriormente a la despolarización ventricular.
  
Estos elementos, junto con los intervalos como el intervalo PR, el período QRS y el intervalo QT, brindan información valiosa sobre la actividad cardíaca y pueden ser indicativos de diversas condiciones cardíacas. Además, los intervalos RR y PP están relacionados con la duración o frecuencia de los ciclos ventriculares y auriculares, respectivamente. <sup>[4](https://doi.org/10.1016/j.bea.2023.100089) </sup>

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c90c0996-9e1f-4b7f-887d-b750cb7197ab">
<p align="center"><i>Figura 1. Morfología del ECG: diferentes segmentos de señal de ECG para una persona normal <sup>[4](https://doi.org/10.1016/j.bea.2023.100089)</sup> </i></p>
</div>

#### b. Electrocardiograma
El electrocardiograma (ECG) es una herramienta diagnóstica esencial que registra la actividad eléctrica del corazón. A través de electrodos colocados estratégicamente en el cuerpo, se capturan las señales eléctricas generadas por cada contracción cardíaca. Estas señales se representan gráficamente como ondas en un papel o pantalla. El ECG proporciona una amplia gama de información, incluyendo la velocidad del ritmo cardíaco, la regularidad de los impulsos eléctricos y la fuerza de la actividad eléctrica en distintas regiones del corazón. Además, permite evaluar la morfología de las ondas cardíacas, lo que puede revelar detalles sobre la estructura y función cardíacas. <sup>[5](https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/)</sup>

#### c. Derivaciones Polares
Las derivaciones bipolares del ECG, denotadas como "I", "II" y "III", son fundamentales para visualizar la actividad eléctrica del corazón desde diferentes ángulos en el plano frontal del cuerpo, también conocido como plano coronal.<sup>[6](https://www.researchgate.net/publication/324690144_Electrocardiografia_de_Alta_Resolucion_Tecnicas_Aplicadas_de_Adquisicion_y_Procesamiento)</sup>

* **Derivación I**: Se caracteriza por colocar el electrodo positivo en el brazo izquierdo y el electrodo negativo en el brazo derecho. Esta disposición permite registrar la energía eléctrica que fluye diagonalmente desde la parte superior derecha del cuerpo hacia la parte inferior izquierda. Los complejos QRS tienden a tener una morfología ascendente debido al flujo del vector medio.

* **Derivación II**: Posiciona el electrodo positivo en el pie izquierdo y el electrodo negativo en el brazo derecho. Esta configuración ofrece una visualización directa del vector medio, resultando en complejos QRS más altos y ondas P más prominentes. Por su fiabilidad, la derivación II es preferida en muchas unidades de cuidados intensivos y de telemetría para monitorizar la actividad cardíaca.
 
* **Derivación III**: Ubica el electrodo positivo en el pie izquierdo y el electrodo negativo en el brazo izquierdo. Similar a la derivación I, el flujo del vector medio se aproxima desde la parte inferior derecha, generando complejos QRS con morfología ascendente. Sin embargo, los complejos QRS en la derivación III tienden a ser más altos debido a un ángulo de aproximación más estrecho.<sup>[7](https://www.researchgate.net/publication/324690144_Electrocardiografia_de_Alta_Resolucion_Tecnicas_Aplicadas_de_Adquisicion_y_Procesamiento)</sup>

</div>
<p align="center">
<image width="200" height="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/582f870a-c87d-4ad2-b525-a6340d19cb0b">
<p align="center"><i>Figura 2.  Derivaciones bipolares estándar del ECG en el plano Frontal <sup>[6](https://www.researchgate.net/publication/324690144_Electrocardiografia_de_Alta_Resolucion_Tecnicas_Aplicadas_de_Adquisicion_y_Procesamiento) </sup> </i></p>
</div>

	
Estas derivaciones bipolares son esenciales para comprender la actividad eléctrica del corazón en el plano frontal del cuerpo, lo que facilita el diagnóstico y monitoreo precisos de diversas condiciones cardíacas.

<a name="objetivos"></a>
## Objetivos
1. Adquirir señales biomédicas de ECG.
2. Hacer una correcta configuración de BiTalino.
3. Extraer la información de las señales ECG del software OpenSignals (r)evolution

<a name="metodologia"></a>
## Metodología 
La metodología seguida para la adquisición y procesamiento de las señales ECG utilizando el kit BITalino fue implementada siguiendo el protocolo de adquisición y posicionamiento de los electrodos de la guía **“"BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface"** <sup>[3](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>. 

<a name="materiales"></a>
### 1. Materiales y Equipos
<div align="center">
	
|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|(R)EVOLUTION|**Kit BITalino**:Kit electrónico formada por varios módulos individuales utilizados para la recolección de datos boiomédicos. Se pueden adquirir señales como EMG,ECG o EEG.|1|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c8d4e3ed-4054-4c4d-9820-0c1dbd5ddd6f">|
|-|**Laptop o PC**:Se descargará el software de análisis para procesar las señales|1|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|
|Fluke|**Prosim4**: Simulador de signos vitales diseñado para comprobar y verificar el funcionamiento básico de varios parámetros fisiológicos, como la respiració, presión arterial, entre otros.|1|<image width="200" height="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/376ac065-9d63-4bc6-b7d6-21d9b7afe0f4">|
|-|**Electrodos**: Registran la actividad eléctrica de los músculos durante la contracción y relajamiento muscular|1|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/21dab0fa-801d-4dd1-b0c9-3b29bf3be7fb">|
<p align="center"><i>Tabla 1. Materiales y equipos </i></p>
</div>


<a name="adquisicion"></a>
### 2. Procedimiento
Para la adquisición de datos, el sujeto de prueba fue un hombre de 22 años con las siguientes características:
<div align="center">
	
|  **Nombre**  | **Edad** | **Peso** | **Sexo** | **Frecuencia de actividad física** | **Condición** |
|:------------:|:--------:|:--------:|:--------:|:----------------------------------:|:-------------:|
|Harold Alemán|22|72 kg|Masculino|Regular|Sano|
<p align="center"><i>Tabla 2. Características del sujeto de prueba elegido </i></p>
</div>

#### Protocolo de conexión
En primer lugar, se realizó la conexión entre el BITalino con el programa OpenSignal para visualizar la señal generada a partir de Bluetooth. Luego, se realizó la conexion ECG en la placa del BITalino utilizando el sensor ECG de 3 electrodos. Posteriormente, se realizó el posicionamiento de los electrodos en el sujeto de prueba para realizar la configuración bipolar de Einthoven <sup>[3](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>. En esta configuración, se colocaron los electrodos de la siguiente manera, también observada en la Tabla 3:
* **IN+** (electrodo positivo/rojo) se coloca en la muñeca izquierda .
* **IN-** (electrodo negativo/negro) se coloca en la muñeca derecha.
* **REF** (electrodo de referencia/blanco) se coloca en la cresta ilíaca,debido a que representa una zona de baja interferencia electromagnética.

<div align="center">	
	
|  **Colocación de electrodos para la derivación I**  | **Colocación de electrodos en el sujeto de prueba** | 
|:------------:|:--------:|
|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/a393348e-5c2c-40d4-9d7a-012674926f9b">|<image width="200" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ea54888d-c6fb-41bc-b132-67bac1fd0285">|
<p align="center"><i>Tabla 3. Posicionamiento de los electrodos en el sujeto de prueba: IN+ (rojo) e IN-(negro) en las muñecas y REF (blanco) en la cresta ilíaca </i></p>
</div>


#### Protocolo de adquisición
Para la adquisición de datos, se realizó el protocolo de adquisición brindado por la guía en la cual se registraron las señales ECG para el análisis en tres diferentes estados:\
**a. Estado de reposo**:El sujeto de prueba se quedó en una posición estable y manteniendo la calma. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.\
**b. Estado de respiración prolongada**: El sujeto mantuvo la respiración por 30 segundos y se registró la señal durante la inspiración, mantención y expiración. El registro de la señal fue grabado por 30 segundos.\
**c. Estado de ejercicio intensivo**: El sujeto de prueba realizó la actividad física de 10 burpees por 3 minutos y la señal fue registrada durante y después de la actividad realizada. El registro de la señal fue grabado por 30 segundos.\

#### Señal ProSim4
Adicionalmente, se utilizó el Fluke ProSim4, para la adquisición de datos del estado de un paciente que llegaría a paro cardíaco utilizando el Prosim4 por cinco ciclos con los siguientes parámetros, como se observa en la Figura 2:
- **ECG 80lpm:** 45s
- **CVP(VI)**: 30s
- **Taq. vent. 160 lpm**: 30s
- **Fib. vent severa**: 30s
- **Asistolia**: 15s
- **Stop**
</div>
<p align="center">
<image width="200" height="400" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/7d2b5dac-75aa-47ce-9c79-9dfa98554684">
<p align="center"><i>Figura 2. Configuración del Prosim4 para la obtención de señales en cuatro etapas que conducen al paro cardíaco</i></p>
</div>

Y para la conexion del PromSim4 para la experiencia de laboratorio, se tomo en consideracion las siguientes entradas en cuanto a los terminales ECG: RL,LL,RA. En el que se utiliza LL como referencia, RA como el electrodo negativo, y LA como el electrodo positivo.
</div>
<p align="center">
<image width="200" height="400" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/57604da2-ce4a-4da0-ad2d-e6aad858acf6">
<p align="center"><i>Figura 3. Colocación de electrodos en el Prosim4</i></p>
</div>

<a name="procesamiento"></a>
### 3. Procesamiento de datos
Para el procesamiento de las señales adquiridas, se realizó el ploteo en Python para el análisis cuantitativo de segmentos específicos y determinar las características de cada señal ECG, así como los intervalos de duración de cada parámetro. Asimismo, se realizó la transformada rápida de Fourier (FFT) para determinar particularidades de una la señal en mucha mayor medida.

<a name="resultados"></a>
## Resultados
###  Visualización de señal eléctrica mediante video y OpenSignals
A continuación se pueden observar los videos correspondientes, tanto del sujeto de prueba como de la señal eléctrica en OpenSignals
<div align="center">	
	
| **Estados** | **Prueba** |
|:------------:|:---------------:|
| **a. Estado basal**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/58d0e028-2c7b-4772-898d-24b52509f798">|
| **b. Manteniendo la respiración 10 segundos**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/701703eb-04c7-4c8c-b24e-738c0388a65a">|
| **c. Reposo basal (exhalación)**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/b2b35cbd-60f7-488e-a7a0-45d3ad81e607">|
| **d. En actividad física**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/b604e160-5482-46f5-98a1-a97b4e9866e5">|
| **e. Después de actividad física**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/cc66813b-bcb5-48ef-9022-612dfcc94d1c">|
<p align="center"><i>Tabla 4. Videos obtenidos en los distintos estados </i></p>
</div>

#### Ploteo de la señales en Python
Se realizó el ploteo de las señales obtenidas en Python y se calculó los latidos por minuto (lpm) para comparar si los valores se encontraban dentro del rango estándar según cada estado evaluado. Para obtener el valor del lpm, se calculó el intervalo R-R en las señales, que representa la despolarización de los ventrículos, siguiendo la siguiente fórmula:
LPM = 60/RR, donde el intervalo RR es medido en segundos y se mide desde el pico de una onda “R” hasta la siguiente onda “R”.\
**a. En reposo**: En el estado de reposo, el usuario presentó un valor del intervalo R-R de 0.68s que equivaldría a 88 latido por minuto (lpm) , lo cual se encuentra dentro del rango de palpitaciones cardíacas estándar de un adulto joven en estado basal <sup>[8](https://www.scielo.br/j/rbfis/a/Jk9rTxSQbTQkVfrjnq3Zspj/)</sup>. Asimismo, se evidencia un pico máximo del complejo QRS de 700 mV en amplitud, y un pico mínimo de aproximadamente 420 de amplitud.
</div>
<p align="center">
<image width="550" height="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ea90f7b4-ee37-4f43-8d20-f7ed1ea9e5fe">
<p align="center"><i>Figura 5. Ploteo de la señal en estado de reposo y características ECG</i></p>
</div>
	
**b. Manteniendo la respiración**: En el segundo estado, el sujeto mantuvo la respiración por 10 segundos con lo que se obtuvo el valor del intervalo R-R de 0.75s, lo cual equivale a 80 lpm, que indica menores palpitaciones cardíacas que en estado de reposo. El pico máximo del complejo QRS es de 680 mV en amplitud, y el pico mínimo de aproximadamente 410 de amplitud.
</div>
<p align="center">
<image width="550" height="400" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/7bfc4f4a-89c2-4276-b7c4-0f77ab0f7a5f">
<p align="center"><i>Figura 6. Ploteo de la señal en estado de manteniendo la respiración y características ECG</i></p>
</div>


**c. Reposo basal (Exhalación)**: En el tercer estado, se registró la señal durante el proceso de exhalación del sujeto tras haber inhalado y mantenido por 10 segundos la respiración. El intervalo R-R obtenido fue de 0.82 s, lo cual equivale a 74 lpm. El pico máximo del complejo QRS es de 610 mV en amplitud, y el pico mínimo de aproximadamente 410 de amplitud.
</div>
<p align="center">
<image width="550" height="400" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/4b1d6814-fd6a-4b54-8f5b-30d31040d763">
<p align="center"><i>Figura 7. Ploteo de la señal en estado de exhalación tras la respiración y características ECG
</i></p>
</div>

**d. En actividad física**: En el cuarto estado, se registró la señal durante la actividad física. El intervalo R-R obtenido fue de 0.48s lo cual equivale a 125 lpm, que indicaría que el sujeto se encuentra en actividad física. Sin embargo, notamos que la señal se encuentra distorsionada debido al ruido ocasionado durante la actividad, por lo que la detección de las características ECG fue desafiante. El pico máximo del complejo QRS fue de 800 mV en amplitud, y el pico mínimo de aproximadamente 200 mV de amplitud.
</div>
<p align="center">
<image width="550" height="400" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/de4275cb-62e7-4f04-9cc1-4a8d64eafa41">
<p align="center"><i>Figura 8. Ploteo de la señal en estado de actividad física  y características ECG
</i></p>
</div>

**e. Después de la actividad física**: En el último estado, se registró la señal tras haber realizado la actividad física y se obtuvo que el intervalo R-R fue de 0.57s lo cual equivale a 105 lpm, demostrando estado de agitación y palpitaciones cardíacas elevadas pero retomando a los valores estándar. El pico máximo del complejo QRS es de 670 mV en amplitud, y el pico mínimo de aproximadamente 410 de amplitud.
</div>
<p align="center">
<image width="550" height="400" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/eedcbe8f-0d68-466e-9ab7-a14d02a5b679">
<p align="center"><i>Figura 9. Ploteo de la señal en estado después de actividad física y características ECG
</i></p>
</div>

### Señal del Prosim4 
A continuación se puede observar los resultados obtenido por el Prosim4 en el OpenSignals, simulando un paro cardiaco, desde el paso 2.
| **Fases** | **Prosim** |**Señaln en Python** |
|:---------:|:----------:|:-------------------:|
| **Fase 1**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/33d585dd-18db-4710-b01c-bb2d4f7b8f6f">|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/64b43f34-7159-4bea-9aa6-3a33dafea32d">|
| **Fase 2**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ad9b1adc-ddc1-4474-b16c-ddaecb371a29">|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/fa0956b8-13f3-4da8-a4cb-47df9f65e4bf">|
| **Fase 3**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e66f74e3-f8bb-42c3-a145-2ac599bd4fca">|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8e7806ea-e3f2-415b-9acf-186bd40f555c">|
| **Fase 4**|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/80e31a5e-f164-4081-be05-2544830dcd98">|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/d3a0737c-a18b-4120-8ec8-80c23ebc1c88">|

<a name="phyton"></a>
## Archivo de la señal ploteada en Python y de los datos de la señal
<a name="r3"></a>
  - [Señales ploteadas en python](y)
<a name="r4"></a>
  - [Datos de la señal ploteada]()

<a name="discusion"></a>
## Discusión
El análisis de las señales ECG obtenidas durante el estudio de los diferentes estados fisiológicos del sujeto evaluado permiten observar la variabilidad de la frecuencia cardíaca, características electrocardiográficas y realizar la comparación con valores estándar y anormales. En el estado de reposo, el sujeto presentó un intervalo RR de 0.68 segundos, lo que se traduce en una frecuencia cardíaca de 88 latidos por minuto (lpm). Este valor se sitúa dentro del rango normal para un adulto joven en estado basal y es una señal de una actividad cardíaca saludable <sup>[8](https://www.scielo.br/j/rbfis/a/Jk9rTxSQbTQkVfrjnq3Zspj/)</sup>.

En el estado de mantención de la respiración, intervalo RR fue de 0.75 segundos, resultando en 80 lpm, indicando una disminución en la frecuencia cardíaca en comparación con el estado de reposo. Al mantener la respiración, los latidos por minuto tienden a ser menores en comparación con el estado de reposo, como se observa según los valores obtenidos. Esto se debe a que el acto de contener la respiración activa el sistema nervioso parasimpático, específicamente el nervio vago, que tiende a reducir la frecuencia cardíaca y puede, en casos extremos, llevar a la bradicardia <sup>[9](https://www.sciencedirect.com/science/article/pii/S1050173820300669)</sup>. El tercer estado, el estado de exhalación, presentó un intervalo RR de 0.82 segundos y 74 lpm, significativamente menor que en el estado de mantención. Esto se debe a que el sistema nervioso parasimpático promueve la relajación al activarse y por ende, disminuye el ritmo cardíaco. Esta variabilidad en el ritmo cardíaco durante el ciclo respiratorio es un signo de buena salud cardíaca y flexibilidad del sistema nervioso autónomo <sup>[9](https://www.sciencedirect.com/science/article/pii/S1050173820300669)</sup>. 

En el cuarto estado, se observa que durante la realización de la actividad física,  el intervalo RR disminuyó a 0.48 segundos, equivalente a 125 lpm. Esta aceleración del ritmo cardíaco es esperada durante la actividad física pues se requiere mayor oxígeno y existe la liberación de adrenalina que incrementa el ritmo <sup>[10](https://www.ahajournals.org/doi/10.1161/circulationaha.107.760405)</sup>, aunque se observó una distorsión en la señal debido al ruido generado por el movimiento y la contracción muscular. Esto resalta la importancia de la correcta colocación de los electrodos para una mejor adquisición. Por último, en el quinto estado, se observa que el intervalo RR incremento a 0.57 segundos, lo que equivale a 105 lpm. Este nivel de frecuencia cardíaca, aunque elevado, indica que el sujeto estaba volviendo a su estado basal tras el ejercicio debido a la reducción del gasto energético y la activación de sistema parasimpático que reduce gradualmente la frecuencia <sup>[11](https://pubmed.ncbi.nlm.nih.gov/24286577/)</sup>. 

En ProSim 4, un simulador de paciente, se generó un array que simula la actividad eléctrica del corazón durante un paro cardíaco <sup>[12](https://www.flukebiomedical.com/sites/default/files/resources/prosim4_gsspa0300.pdf)</sup>. Su función principal es calibrar equipos de electrocardiograma (ECG), proporcionando una señal estándar para ajuste y calibración.

Al conectar el dispositivo Bitalino al ProSim, pudimos visualizar la señal con una notable ausencia de ruido. Esto se debió a la inserción directa de los electrodos en el paciente simulado, garantizando una captura limpia y precisa de la señal. Esta claridad facilitó la interpretación de los datos y la evaluación del rendimiento del equipo de ECG.

La señal simulada por ProSim 4 sigue un patrón de 4 tiempos. Inicialmente, se muestra un estado aparentemente normal, aunque con variaciones periódicas en el complejo QRS. Luego, se observa un ensanchamiento del complejo QRS y arritmias, seguido de arritmias más variadas. Finalmente, se muestra un pulso equipotencial, indicando la ausencia de actividad cardíaca (bpm). Este ciclo de señales proporciona una representación detallada de diversas condiciones cardíacas para propósitos de calibración y entrenamiento médico.

<a name="conclusiones"></a>
## Conclusiones
El ruido proveniente de la respiración y la actividad muscular puede afectar la calidad de las señales de ECG, lo que puede influir en la eficacia de los algoritmos utilizados. Aunque los filtros digitales pueden ayudar a reducir este ruido, es posible que no lo eliminen por completo.El dispositivo Bitalino demostró ser capaz de identificar claramente los diferentes patrones en las señales de ECG, incluyendo los picos del complejo QRS.

Ninguna de las señales mostró patrones gráficos asociados con enfermedades cardíacas, descartando esa posibilidad.El proceso de análisis de las señales en Python se realizó con éxito, permitiendo una evaluación detallada de los datos.

Se protegió la identidad de los participantes en el estudio de manera adecuada, garantizando su confidencialidad.La combinación de ProSim y Bitalino ofrece una plataforma efectiva para adquirir y analizar señales de ECG, con potencial aplicación en entornos clínicos e investigativos.


<a name="referencias"></a>
## Referencias bibliográficas
[1] V. Gupta and M. Mittal, “ECG Signal Analysis: Past, Present and Future,” IEEE Xplore, Dec. 01, 2018. https://ieeexplore.ieee.org/document/8704365

[2] Mayo Clinic, “Electrocardiogram (ECG or EKG)” www.mayoclinic.org, May 18, 2022. https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983#:~:text=Electrocardiograma-

[3] PLUX – Wireless Biosignals, “BITalino (r)evolution Lab Guide,” Feb. 2021. Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

[4] T. Anbalagan, M. K. Nath, D. Vijayalakshmi, and A. Anbalagan, “Analysis of various techniques for ECG signal in healthcare, past, present, and future,” Biomedical Engineering Advances, vol. 6, p. 100089, Nov. 2023, doi: https://doi.org/10.1016/j.bea.2023.100089.

[5] MedlinePlus, “Electrocardiograma” medlineplus.gov, Feb. 28, 2023. https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/

[6] N. Dugarte Jerez, E. Dugarte Dugarte, and N. Dugarte Dugarte, Electrocardiografía de Alta Resolución Técnicas Aplicadas de Adquisición y Procesamiento, 1st ed. Mendoza – Argentina: Universidad Tecnológica Nacional – Facultad Regional Mendoza, 2018.https://www.researchgate.net/publication/324690144_Electrocardiografia_de_Alta_Resolucion_Tecnicas_Aplicadas_de_Adquisicion_y_Procesamiento

[7] G. Goldich, “El electrocardiograma de 12 derivaciones: Parte I: reconocimiento de los hallazgos normales,” Nursing, vol. 32, no. 2, pp. 28–34, Mar. 2015, doi: https://doi.org/10.1016/j.nursi.2015.03.010

[8] Gianinis, H. H., Antunes, B. O., Passarelli, R. C., Souza, H. C., y Gastaldi, A. C., "Effects of dorsal and lateral decubitus on peak expiratory flow in healthy subjects", Brazilian Journal of Physical Therapy, vol. 17, no. 5, pp. 435–441, 2013. https://www.scielo.br/j/rbfis/a/Jk9rTxSQbTQkVfrjnq3Zspj/

[9] A. A. Manolis et al., "The role of the autonomic nervous system in cardiac arrhythmias: The neuro-cardiac axis, more foe than friend?," Trends in Cardiovascular Medicine, vol. 31, no. 5, pp. 290-302, 2021, doi: 10.1016/j.tcm.2020.04.011. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S1050173820300669

[10] B. Olshansky, H. N. Sabbah, P. J. Hauptman y W. S. Colucci, "Parasympathetic nervous system and heart failure: pathophysiology and potential implications for therapy," Circulation, vol. 118, no. 8, pp. 863–871, 2008, doi: 10.1161/CIRCULATIONAHA.107.760405.
https://www.ahajournals.org/doi/10.1161/circulationaha.107.760405

[11]D. Y. Zhang y A. S. Anderson, "The sympathetic nervous system and heart failure," Cardiol Clin., vol. 32, no. 1, pp. 33-45, 2014. doi: 10.1016/j.ccl.2013.09.010. [PMID: 24286577; PMCID: PMC5873965]. https://pubmed.ncbi.nlm.nih.gov/24286577/

[12] (s.f.). Biomedical Testing Equipment Solutions | Fluke Biomedical. https://www.flukebiomedical.com/sites/default/files/resources/prosim4_gsspa0300.pdf
