# Laboratorio N°5 - Procedimiento de registro de señales de electroencefalograma (EEG)
## **Tabla de contenidos**
1. [Lista de participantes](#lista)
2. [Introducción](#introduccion)\
   2.1 [Contexto](#contexto)\
   2.2 [Marco teórico](#marco)
3. [Objetivos](#objetivos)
4. [Metodología](#metodologia)\
   4.1 [Materiales y equipos](#materiales)\
   4.2 [Procedimiento](#adquisicion)\
   4.3 [Procesamiento de datos](#procesamiento)
5. [Resultados](#resultados)\
   5.1 [Prueba con Bitalino](#bitalino)\
   5.2 [Prueba con Ultracortex Mark IV](#ultracortex)
6. [Archivos](#archivos)
7. [Discusión](#discusion)
8. [Conclusiones](#conclusiones)
9. [Referencias bibliográficas](#referencias)


<a name="lista"></a>
## **Lista de participantes**
- Sofia Camila Céspedes Trece - 71738148
- Nicole Stefany Acuña Malpartida - 71400976
- Chris Margory Viviano Salvatierra - 75138288
- Harold Alonso Alemán Ramírez - 71386429
  
<a name="introduccion"></a>
## **Introducción**
<a name="contexto"></a>
### **Contexto**
#### **a. Encefalografía**
Un electroencefalograma (EEG) es una téncica no invasiva usada en el ámbito de la neurología, el cual sirve para medir las diferentes señales eléctricas creadas por la actividad de grandes grupos de neuronas, durante un determinado periodo de tiempo, a través de electrodos <sup>[1](https://www.mdpi.com/2076-3417/10/21/7453)</sup>. La neuronas cerebrales establecen comunicación a través de impulsos eléctricos, incluso cuando estamos dormidos. Y esta actividad es la que el electroencefalográgico registra como líneas onduladas <sup>[2](https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875)</sup> .El electroencefalograma funciona midiendo las fluctuaciones de la corriente eléctrica entre la piel y el sensor, en este caso de los electrodos, amplicando la corriente eléctrica y realizando filtrado de ser necesario <sup>[1](https://www.mdpi.com/2076-3417/10/21/7453)</sup>.

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/b74e6a58-fd60-4514-96f0-81cc09cd571d">
<p align="center"><i>Figura 1. Actividad cerebral registrada por encefalograma [2] </i></p>
</div>


#### **b. Patologías que pueden ser detectadas con EEG**<sup> [1](https://www.mdpi.com/2076-3417/10/21/7453)</sup>
Este procedimiento no invasivo es útil, ya que los resultados que arrojan nos permiten visualizar cambios en la actividad cerebral, los cuales luego de ser interpretados nos proporcionan información, que nos ayuda a diagnosticar y predecir muchas enfermedades cerebrales anormales y deterioros cognitivos. A continuación se mencionarán solo algunas de las enfermedades que pueden ser diagnosticadas:
1. Epilepsia
2. Enfermedad de Parkinson
3. Problemas de memoria como el Alzheimer
4. Deficiencias del lenguaje como dislexia
5. Trastorno por déficit de atención e hiperactividad (TDHA)
6. Convulsiones
7. Esquizofrenia
8. Autismo en adultos y niños 
9. Trastornos del sueño e insomnio, ansiedad , estrés
10. Tumores cerebrales
11. Encefalitis herpética
12. Accidente cerebrovascular

#### **c. Aplicaciones** <sup> [1](https://www.mdpi.com/2076-3417/10/21/7453)</sup>
Los dispositivos EEG pueden proporcionar información valiosa sobre el estado de salud mental de las personas, y contribuir también a la investigación. Entre algunas de las aplicaciones del EEG podemos encontrar: 
* **Interfaces cerebro-computadora (BCI)** : El BCI es una de las aplicaciones comunes del EEG, en donde utilizan los datos obtenidos del EEG en tiempo real, para controlar dispositivos mecánicos y electrónicos. El BCI principlamente se puede usar en 3 ámbitos:
1. Navegación autónoma de dispoditivos digitales, con orientación a la teleoperación en tiempo real de cuerpos robóticos y monitoreo de sensores.
2. Como ayuda para personas con discapacidades motoras leves, con el fin de facilitarles sus actividades,  
Entre otro de lcomo en el control de aplicaciones móviles, dirigir movimientos de sillas de ruedas eléctricas, sistemas de reconocimiento de voz para personas con discapacidad de habla, etc.
3. Neurojuegos y entretenimiento.   

* **Investigación en neurociencia** :
Para comprender la funcionalidad del sistema nervioso, el EEG es usado como herramienta para aprender sobre el funcionamiento del cerebro cuando experimenta diferentes estados emocionales y como funciona el cerebro en diversos estados mentales. Algunos de los campos en los que se realiza comunmente investigacionesson en:
1. Neurociencia cognitiva
2. Neurociencia conductual
3. Neurofisiología


<a name="marco"></a>
### Marco teórico

#### **a. ¿Qué es una señal EEG?**
El electroencefalograma (EEG) es una técnica de neuroimagen no invasiva que permite el registro de la actividad eléctrica del cerebro mediante la colocación de electrodos en el cuero cabelludo que detectan la señal <sup>[3](https://www.frontiersin.org/articles/10.3389/fncom.2023.1151852/full)</sup> . Estas señales brindan información en cuanto a los diferentes mecanismos operativos que presenta el cerebro, permitiendo la identificación de patrones, trastornos neurológicos y explorar diversos procesos cognitivos <sup>[4](https://www.sciencedirect.com/science/article/pii/S092549272300001X)</sup> . Asimismo, el EEG representa un patrón de señal que es obtenida amplificando y registrando el potencial biológico del cerebro en el cuero cabelludo. Este potencial refleja la actividad macroscópica de la superficie cerebral y permite que los electrodos capturen los impulsos eléctricos inherentes y periódicos generados por grupos de células cerebrales <sup>[5](https://doi.org/10.3390/s140712847)</sup>. Las oscilaciones de voltaje que presentan estas señales revelan cierta actividad cerebral significativa, lo cual se refleja en estados de sueño profundo o en coma, donde las oscilaciones son lentas y las amplitudes elevadas <sup>[6](http://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272009000600004&lng=es&tlng=es.)</sup>. 


</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164461832/1971c8a3-8cf5-4ce0-a9d1-e974308ce70f">
<p align="center"><i>Figura 2. Ejemplo de una señal EEG para un paciente sano </i></p>
</div>


#### b. Oscilaciones del EEG
Para la interpretación del EEG, es importante considerar la caracterización que presentan las señales en función a su ubicación, amplitud, frecuencia, morfología, continuidad, simetría o reactividad. Sin embargo, el método más utilizado para interpretar es a partir de la frecuencia, estipulando que la señal medida es una mezcla de diferentes frecuencias subyacentes que se consideran reflejo de estados cognitivios, afectivos o de atención. A continuación, se observa una tabla de la clasificación de las ondas cerebrales según la frecuencia <sup>[7](https://doi.org/10.1016/j.ijpsycho.2015.02.003.)</sup> <sup>[8](https://www.ncbi.nlm.nih.gov/books/NBK539805)</sup> :

<div align="center">
	
|  **Tipo de banda**  | **Frecuencia (Hz)** | **Estado del cerebro** |
|:------------:|:---------------:|:------------:|
|**Delta**|0.5 - 4.0|<p align="justify"> La banda delta es la oscilación más lenta y de mayor amplitud del EEG. Aparece durante el sueño profundo y contribuye a la consolidación de la memoria y el aprendizaje. Normalmente, se observa en las regiones frontocentrales de la cabeza, pero su presencia en estados de vigilia puede indicar problemas cerebrales como encefalopatía o disfunción focal.</p>|
|**Theta**|4.0 - 7.0|<p align="justify"> La banda theta del EEG está relacionada con la somnolencia y las etapas iniciales del sueño, predominando en las regiones frontocentrales y reemplazando al ritmo alfa con el aumento de la somnolencia. Además, se intensifica durante emociones fuertes y en tareas mentales desafiantes. Su presencia focal en la vigilia puede indicar disfunción cerebral focal y está asociada con la atención y la memoria de trabajo.</p>|
|**Alpha**|8.0 - 12.0|<p align="justify"> El ritmo alfa dominante posterior se observa en EEG normales de personas despiertas, ubicado en la región occipital. Es el ritmo de fondo de EEG en adultos y suele mantenerse estable desde los 3 años hasta la novena década de vida en individuos sanos. Variaciones rápidas de este ritmo pueden ocurrir en personas normales. Su ralentización sugiere disfunción cerebral generalizada. El ritmo alfa está relacionado con la relajación y la inhibición sensorial, aumentando con los ojos cerrados y relajación, y disminuyendo con actividad y ojos abiertos.</p>|
|**Beta**|13.0 - 30.0|<p align="justify"> El ritmo beta es el ritmo EEG más común en adultos y niños normales. Predomina en las regiones frontal y central de la cabeza y se debilita hacia las áreas posteriores. Se relaciona con el pensamiento activo, la concentración y la planificación de movimientos. También puede activarse cuando se observan movimientos de otras personas.</p>|
|**Gamma**|>30|<p align="justify"> El ritmo gamma pertenece a la clasificación de ondas de alta frecuencia. Su importancia en diversas funciones cognitivas está bien documentada. Estos ritmos pueden ser útiles para detectar desmielinización y otros problemas de integridad cortical. Se sugiere que los ritmos gamma están relacionados con la integración de percepciones sensoriales y la atención.</p>|
<p align="center"><i>Tabla 1. Oscilaciones del EEG </i></p>
</div>


#### c. Activación neural
El cerebro se compone de millones de neuronas interconectadas que generan potenciales eléctricos. Como se mencionó previamente, esta actividad es detectada a partir del EEG, utilizando electrodos que registran los dipolos eléctricos creados por poblaciones neuronales situadas perpendicularmente a la superficie de la cabeza, principalmente por neuronas piramidales ubicadas entre las capas 3 y 5 de la corteza cerebral. Estas neuronas generan campos eléctricos como resultado de señales electroquímicas transmitidas entre ellas. Cuando generan campos eléctricos al mismo tiempo, estos son lo suficientemente significativos para ser captados por el EEG <sup> [9](https://doi.org/10.1038/nrn3137)</sup> .Asimismo, a nivel fisiológico, las señales del EEG provienen de las corrientes iónicas transmembrana en las neuronas piramidales; estas células, se encuentran en todas las áreas de la corteza cerebral: occipital, temporal, parietal y frontal, y están siempre orientadas perpendicularmente a la superficie cortical, con el cuerpo celular dirigido hacia el interior del cerebro y las dendritas apuntando hacia la superficie cortical <sup> [10](https://onlinelibrary.wiley.com/doi/full/10.1684/epd.2020.1217)</sup> .


#### d. Artefactos
Si bien el EEG permite registrar la actividad eléctrica cerebral, también registra actividades eléctricas que se originan en lugares distintos del cerebro. Esta actividad registrada se denomina artefacto pues no es de origen cerebral y puede dificultar la interpretación clínica o el posterior análisis cuantitativo. Los artefactos surgen de fuentes fisiológicas, como ritmo cardíaco, actividad muscular o movimiento ocular y extrafisiológicas, como el ruido ambiental o del propio sistema de medición <sup> [11](https://doi.org/10.1088/1741-2560/12/3/031001)</sup> <sup> [12](https://doi.org/10.1016/j.clinph.2006.10.019)</sup> . Por ello, resulta importante considerar protocolos para la adquisición correcta de las señales EEG que permitan disminuir la mayor cantidad de artefactos y un correcto pre-procesamiento de la señal para su análisis posterior. 

<a name="objetivos"></a>
## Objetivos
1. Adquirir señales biomédicas de EEG.
2. Hacer una correcta configuración de BiTalino y Ultracortex Mark IV.
3. Extraer la información de las señales ECG del software OpenSignals (r)evolution y OpenBCI
   
<a name="metodologia"></a>
## Metodología 
La metodología seguida para la adquisición y procesamiento de las señales EEG utilizando el kit BITalino fue implementada siguiendo el protocolo de adquisición y posicionamiento de los electrodos de la guía “"BITalino HOME-GUIDE #3 ELECTROENCEFALOGRAM(ECG) Exploring Signals at the Skin Surface" <sup> [13](https://www.pluxbiosignals.com/products/bitalino-revolution-board-kit-ble-bt)</sup> . Asimismo, se utilizó el Ultracortex Mark IV EEG Headset siguiendo el sistema 10-20, que es el estándar aceptado internacionalmente para la colocación de electrodos en el contexto del EEG.

<a name="materiales"></a>
### 1. Materiales y Equipos
<div align="center">
	
|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|(R)EVOLUTION|**Kit BITalino**:Kit electrónico formada por varios módulos individuales utilizados para la recolección de datos boiomédicos. Se pueden adquirir señales como EMG,ECG o EEG.|1|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c8d4e3ed-4054-4c4d-9820-0c1dbd5ddd6f">|
|-|**Laptop o PC**:Se descargará el software de análisis para procesar las señales|1|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|
|-|**Electrodos**: Registran la actividad eléctrica de los músculos durante la contracción y relajamiento muscular|3|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/21dab0fa-801d-4dd1-b0c9-3b29bf3be7fb">|
|OpenBCI|**Ultracortex Mark IV EEG Headset** : Es un casco de encefalografía diseñado para registrar actividad eléctrica del cerebro, utilizada comúnmente en investigaciones relacionadas con la neurociencia, la interfaz cerebro-computadora (BCI) y monitorización de la salud mental|1|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/62500fc6-f80b-4aed-88de-dfb30c20a060">|
|OpenBCI|**OpenBCI Cyton 8-channel Board** : Es una placa de adquisición de datos de electroencefalografía (EEG) de ocho canales fabricada por OpenBCI|1|<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8735fad8-29d3-4401-b952-f3df243f17d1">|
<p align="center"><i>Tabla 2. Materiales y equipos </i></p>
</div>


<a name="adquisicion"></a>
### 2. Procedimiento
Para la adquisición de datos, el sujeto de prueba fue una mujer de 22 años con las siguientes características:
<div align="center">
	
|  **Edad**  | **Peso** | **Sexo** | **Condición** |
|:------------:|:---------------:|:------------:|:----------:|
|22|58 kg|Femenino|Sano|
<p align="center"><i>Tabla 3. Características del sujeto de prueba escogido </i></p>
</div>

#### 2.1. Protocolo de conexión
##### Conexión con BiTalino
En primer lugar, se realizó la conexión entre el BITalino con el programa OpenSignal para visualizar la señal generada a partir de Bluetooth. Para utilizar el BITalino y cumplir con los objetivos del laboratorio, como la lectura de señales EEG, es necesario seguir ciertos pasos clave. El uso del programa OpenSignals es esencial para este propósito. En caso de no tener la instalación correspondiente, se puede proceder a través de la página web (enlace) para ejecutar el sistema operativo.

Una vez realizada la instalación o acceso al programa, encendemos el BITalino cambiando el estado del interruptor a ON. Posteriormente, para configurar la placa y el sensor BITalino (r)evolution en OpenSignals, primero se abre el administrador de dispositivos de OpenSignals (r)evolution. Una vez dentro, se selecciona el dispositivo que se desea utilizar para la adquisición de datos haciendo clic en el botón ENABLE en el panel correspondiente. Se verifica que el dispositivo esté activado si es que aparece una señal de color azul.

Después de seleccionar el dispositivo, se hace clic en el logo de BITalino para acceder a las configuraciones disponibles. En este paso, se elige el canal al que está conectado el sensor y se selecciona el tipo de sensor correspondiente desde el menú desplegable. Para este laboratorio sería el de EEG. Una vez seleccionado el canal y el tipo de sensor, se activa el canal para la adquisición. Finalmente, cuando se esté listo para comenzar con la adquisición de datos, se hace clic en el botón de grabación en la interfaz principal de OpenSignals. Este procedimiento garantiza que el BITalino esté correctamente configurado y listo para capturar los datos necesarios para el experimento en el laboratorio.

##### Conexión del BITalino (r)evolution con sensores y actuadores
La Placa BITalino (r)evolution viene con sensores y actuadores ya conectados a ella (ver Figura 3). Los sensores EEG, EDA, ECG y EMG necesitan ser conectados a un cable de electrodo utilizando el puerto del sensor, que está marcado en rojo para facilitar su identificación, en el caso específico para la toma de EEG el puerto al cual se debe conectar los electrodos al puerto **A4** del BiTalino <sup> [13](https://www.pluxbiosignals.com/products/bitalino-revolution-board-kit-ble-bt)</sup>.

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/d6304c8a-ef2e-459b-bb0a-2514072ec3a2">
<p align="center"><i>Figura 3. Placa BITalino (r)evolution con sensores y actuadores preconectados. Puertos de sensores para conexión a un cable de electrodos marcados en rojo [13] </i></p>
</div>

Para conectar estos sensores, se requiere un cable de electrodo adecuado, que puede tener 2 o 3 cables conductores. La información sobre qué tipo de cable se necesita para cada sensor se encuentra en la Figura 4.<sup> [13](https://www.pluxbiosignals.com/products/bitalino-revolution-board-kit-ble-bt)</sup>

</div>
<p align="center">
<image width="350" height="100"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/f7dbd185-a7bb-4d4a-81bb-3c448e913c5e">
<p align="center"><i>Figura 4. Combinaciones de sensores y cable de electrodos [13]. </i></p>
</div>


#### b. Colocación de electrodos
Luego, se realizó la conexion EEG en la placa del BITalino utilizando el sensor EEG de 3 electrodos. Posteriormente, se realizó el posicionamiento de los electrodos en el sujeto de prueba para realizar la configuración bipolares de acuerdo al sistema internacional 10-20. En esta configuración, se colocaron los electrodos de la siguiente manera, también observada en la Tabla 3:
* **FP1** (electrodo positivo/rojo) se coloca en la sección de la frente izquierda .
* **FP2** (electrodo negativo/negro) se coloca en la sección de la frente derecha.
* **REF** (electrodo de referencia/blanco) se coloca en el hueso mastoideo, debido a que representa una zona de baja interferencia electromagnética.


<div align="center">	
	
|  **Colocación de electrodos para el registro de señales EEG con el Kit Bitalino**  | **Colocación de electrodos para el registro de las señales EEG con el Open BCI Ultracortex Mark IV** | 
|:------------:|:--------:|
|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/7662c920-4066-4869-8268-9ae4a66a83e5">|<image width="450" height="300" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e3011564-1b5d-4230-a901-0898b5af9709">|
<p align="center"><i>Tabla 4. Posicionamiento de los electrodos en el sujeto de prueba</i></p>
</div>

#### 2.2. Protocolo de adquisición
Para la adquisición de datos, se realizó el protocolo de adquisición brindado por la guía y los docentes del curso en la cual se registraron las señales EEG para el análisis en cuatro diferentes estados:

**a. Estado de reposo**: El sujeto de prueba se quedó en una posición estable y manteniendo la calma para el registro de una línea base de señal con poco ruido y sin movimientos. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Estado de ojos cerrado-ojos abiertos**: El sujeto mantuvo los ojos cerrados y abiertos completando un ciclo (5 veces cada estado), manteniendo ambas fases durante 5 segundos. Para evitar artefactos, el sujeto se mantuvo calmado y mirando hacia un punto específico. El registro de la señal fue grabado por 50 segundos.

**c. Estado de segundo reposo**: Tras la primera actividad, el sujeto de prueba mantuvo nuevamente el estado de calma y sin movimiento como segunda fase de referencia. El registro de la señal fue grabado por 30 segundos.

**d. Estado de preguntas**: Se realizaron una serie de ejercicios matemáticos <sup> [14](https://doi.org/10.3758/s13415-019-00703-5)</sup>
 de menor a mayor complejidad al sujeto de prueba para que pueda resolverlo mentalmente enfocando su mirada en un punto específicos para evitar artefactos. La duración entre el lapso de registro de la respuesta y la siguiente pregunta fue de 12 segundos. Las preguntas realizadas se observan en la Tabla 4.

|  **Categoría**  | **Pregunta** | 
|:------------:|:---------------:|
|**Simple**|<p align="justify"> Hay 3 pájaros en un árbol; Llegan 7 más. ¿Cuántos pájaros hay ahora?</p>|
|**Simple**|<p align="justify"> Jonás tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tienen en total?</p>|
|**Simple**|<p align="justify"> Hanna tiene 9 dólares pero gastó 4. ¿Cuántos dólares le quedan?</p>|
|**Compleja**|<p align="justify"> John anotó 45 puntos para su equipo; 10 más que José. Marie anotó 13 puntos más que John y Joseph juntos. ¿Cuántos puntos obtuvieron en total?</p>|
|**Compleja**|<p align="justify"> El grupo A tiene 24 estudiantes; 13 menos que el grupo B. El grupo C tiene 12 alumnos más que los grupos A y B juntos. ¿Cuál es el número total de estudiantes?</p>|
|**Compleja**|<p align="justify"> Una tienda vendió 21 refrescos por la mañana y 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y por la tarde juntas. ¿Cuántos refrescos se vendieron en total?</p>|
<p align="center"><i>Tabla 5. Preguntas realizadas al sujeto de prueba </i></p>
</div>

#### 2.3. Ultracortex Mark IV EEG Headset
Por otra parte, para la conexión del Ultracortex Mark IV se utilizó asimismo el sistema 10-20 para el posicionamiento de los electrodos, como se observa en la Figura 5. Asimismo, la adquisición de las señales obtenidas fue registrada en OpenBCI para su posterior análisis. La conexión fue realizada a un sujeto de prueba (mujer, 22 años, condición sana) de un equipo de trabajo distinto al nuestro debido a complicaciones con el manejo del tiempo para el uso. 

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1572adee-70d4-4bde-9c4e-e38c0ed51ea3">
<p align="center"><i>Figura 5. Posicionamiento de los electrodos según el sistema 10-20.</i></p>
</div>

Para la prueba con el Ultracortex, estamos mostrando datos y fotos de otro grupo debido a dificultades con el tiempo, a continuación se muestra la foto del sujeto de prueba:

</div>
<p align="center">
<image width="250" height="400"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/4a1ed420-10cc-4877-acdd-5fb0131de3a4">
<p align="center"><i>Figura 6. Posicionamiento de los electrodos según el sistema 10-20 en el sujeto de prueba.</i></p>
</div>

<a name="procesamiento"></a>
### 3. Procesamiento de datos
Para el procesamiento de las señales adquiridas, se realizó el ploteo en Python para el análisis cuantitativo de segmentos específicos y determinar las características de cada señal EEG, así como los intervalos de duración de cada parámetro. Asimismo, se realizó la transformada rápida de Fourier (FFT) para determinar las frecuencias.

<a name="resultados"></a>
## Resultados
<a name="bitalino"></a>
### 1. Prueba con Bitalino
####  1.1. Visualización de señal eléctrica mediante video y OpenSignals
A continuación se pueden observar los videos correspondientes, tanto del sujeto de prueba como de la señal eléctrica registrada según cada estado en OpenSignals.
<div align="center">	
	
| **Estados** | **Videos** |
|:------------:|:---------------:|
| <p align="justify">**a. Estado de reposo**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/60a9c0ed-fcfd-4c2f-9139-7b9dd845d8f8">|
| <p align="justify">**b. Estado de ojos cerrado-ojos abiertos**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8cc12b02-0daf-4a6d-9831-6299945492e2">|
| <p align="justify">**c. Estado de segundo reposo**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/5aba84d2-9a56-4b4f-a673-329ed3819a50">|
| <p align="justify">**d. Estado de preguntas**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/959c0340-0668-4424-9f28-764e0b352842">|
<p align="center"><i>Tabla 6. Videos obtenidos en los distintos estados con el Bitalino</i></p>
</div>

#### 1.2. Ploteo de señales en Python
Se realizó el ploteo de las señales obtenidas en Python y se calculó la presencia de las bandas de frecuencia de las oscilaciones EEG y comparar las señales obtenidas con valores estándar según cada estado evaluado. Se observa la respuesta en el tiempo de los registros del sujeto de prueba en los cuatro estados. Estos registros muestran el comportamiento general de las señales adquiridas, para las cuales se obtuvo como tendencia cambios en la amplitud del voltaje y en la frecuencia de las oscilaciones al pasar de un estado a otro.

**a. Estado 01 - reposo** : En el primer estado, se observa la presencia de oscilaciones de la banda delta, la cual se presenta en las diferentes fases del sueño, pues se observan oscilaciones mas lentes y con amplitud considerable. Asimismo, se observa la presencia de ondas alfa pues se presentan en un estado de relajación y aumentan con los ojos cerrados. La amplitud que presenta la señal oscilaba entre los 600-700 mV aproximadamente. Los valores obtenidos de la frecuencia del sujeto de prueba coinciden con valores estándar en fase de reposo en cuanto a amplitud y presencia de la banda delta <sup> [15](http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0120-33472021000200201&lng=en.)</sup>.

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/861f93da-1add-4bce-823b-806163ca2bda">
<p align="center"><i>Figura 7.  Ploteo de la señal en estado de reposo</i></p>
</div>

**b. Estado 02 - ojos cerrados y abiertos**: En el segundo estado, se observa la presencia de picos en la amplitud de la señal, los cuales se intensifican debido a que representan el periodo de apertura de ojos por los cinco segundos. Se observa, además, que desde el segundo 05 al segundo 10, existe la mayor amplitud presentada y esto se debe a que el sujeto de prueba fue expuesto ante la intensidad luminosa del medio ambiente o el movimiento ocular, lo cual representa un artefacto en la medición. Asimismo, observamos la presencia de las bandas alfa y beta, debido a que al abrir los ojos y comenzar a enfocarse en el entorno, es común observar un aumento en la actividad beta. 

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/149fb3f8-3991-407c-833d-6b5d7db8fd44">
<p align="center"><i>Figura 8. Ploteo de la señal en estado de ojos cerrados-abiertos </i></p>
</div>


**c. Estado 03 - segundo reposo**: En el tercer estado, el sujeto estuvo en un periodo de reposo tras el primer ejercicio. Se observa que la señal presenta similitudes con el primer estado y la presencia de las bandas alfa, delta y theta pues se encuentra en un estado de relajación, con mayor predominio de las bandas alfa. La amplitud oscilaba entre los 600 y 700 mV.

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2f47155e-4f65-47d2-9d77-906e0ccbccba">
<p align="center"><i>Figura 9. Ploteo de la señal en estado de segundo reposo</i></p>
</div>

**d. Estado 04 - ejercicios matemáticos**: En el cuarto estado, se registró la señal durante la resolución de los ejercicios matemáticos mentales. Se dividió la señal en dos fases: la fase de preguntas simples y la fase de preguntas complejas. En la Figura 10, se observa la señal durante la fase de preguntas simples, en las que se observa la presencia de bandas beta, pues esta banda esta más asociada con la actividad mental, la concentración y la resolución de problemas, así como bandas theta debido a que eran ejercicios simples. Asimismo, la amplitud que presenta esta señal seccionada oscila entre los 400 y 700 mV, con picos de intensidad que representan los posibles artefactos durante la medición.

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/72a70136-8be4-433d-a5aa-ce5fd6521e14">
<p align="center"><i>Figura 10. Ploteo de la señal en estado de preguntas matemáticas (preguntas simples)
</i></p>
</div>

Por otra parte, en la Figura 11, observamos la señal durante la fase de preguntas complejas, la cual requirió mayor atención y procesamiento cerebral para el sujeto. Se observa principalmente la presencia de bandas beta y gamma debido a que estas se presentan cuando existen procesos cognitivos complejos, como la percepción y el procesamiento de información. Al resolver problemas matemáticos, la actividad gamma puede aumentar, especialmente con problemas de alta complejidad que requieren más procesamiento cerebral. Asimismo, se observa la presencia de picos continuos durante el registro y con amplitud variable.

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/9e373400-74c2-4421-99aa-8684c0fe93a1">
<p align="center"><i>Figura 11. Ploteo de la señal en estado de preguntas matemáticas (preguntas complejas)
</i></p>
</div>
	
<a name="ultracortex"></a>
### 2.Prueba con Ultracortex Mark IV EEG Headset
####  2.1. Visualización de las señales
A continuación se pueden observar los videos correspondientes a la adquisición con el Ultracortex Mark IV, tanto del sujeto de prueba como de la señal eléctrica registrada según cada estado en OpenBCI. Estos videos son originalmente de otro equipo de trabajo del horario debido a complicaciones con el tiempo para la adquisición.
<div align="center">
	
| **Estados** | **Videos** |
|:------------:|:---------------:|
| <p align="justify">**a. Estado de reposo**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1a871be1-8505-4283-9a19-00b304ee21f9">|
| <p align="justify">**b. Estado de ojos cerrado-ojos abiertos**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/b52bb9c7-ed06-4281-9c48-5cdcd29d4356">|
| <p align="justify">**c. Estado de segundo reposo**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/91cc940b-80d4-4e0b-89a0-3cc730dd57e2">|
| <p align="justify">**d. Estado de preguntas**</p>|<video width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/5cd1d33f-88a2-4460-8c93-0473fbf844e4">|
<p align="center"><i>Tabla 7. Videos obtenidos en los distintos estados con el Ultracortex</i></p>
</div>

#### 2.2. Ploteo de señales en Python
**a. Estado de reposo:**
</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/3ae98b4f903f5af0ca94d986653505c7906e8349/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/Imagenes_Cortex/reposo.jpeg">
<p align="center"><i>Figura 12. Ploteo de la señal en estado de reposo
</i></p>
</div>
	
**b. Estado de ojos cerrados-abiertos:**
</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/3ae98b4f903f5af0ca94d986653505c7906e8349/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/Imagenes_Cortex/parpadeo.jpeg">
<p align="center"><i>Figura 13. Ploteo de la señal en estado parpadeo
</i></p>
</div>
	
**c. Estado de segundo reposo:**
</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/3ae98b4f903f5af0ca94d986653505c7906e8349/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/Imagenes_Cortex/reposo2.jpeg">
<p align="center"><i>Figura 14. Ploteo de la señal en estado de segundo reposo
</i></p>
</div>
	
**d. Estado 04 - ejercicios matemáticos**:
</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/blob/3ae98b4f903f5af0ca94d986653505c7906e8349/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/Imagenes_Cortex/preguntas.jpeg">
<p align="center"><i>Figura 15. Ploteo de la señal en estado de preguntas matemáticas
</i></p>
</div>
	
La gráfica de EEG ofrece un reflejo detallado de la amplitud y frecuencia de las señales cerebrales en diversas bandas de ondas. Las ondas delta, de baja frecuencia y alta amplitud, se distinguen por oscilaciones lentas y picos prominentes, asociados con el sueño profundo y la relajación. En contraste, las ondas theta, con frecuencia moderada y amplitud media, presentan oscilaciones más rápidas pero igualmente significativas, ligadas a la relajación, meditación y ciertos estados de atención.  Las ondas alpha, caracterizadas por una frecuencia media y baja amplitud, exhiben oscilaciones suaves y consistentes, señales de relajación o focalización de la atención. Mientras tanto, las ondas beta, de alta frecuencia y baja amplitud, se distinguen por oscilaciones rápidas y diminutas, relacionadas con la actividad mental activa, concentración y procesamiento cognitivo. Por último, las ondas gamma, de alta frecuencia y baja amplitud similar a las beta pero en un rango superior, muestran oscilaciones veloces y mínimas, asociadas a la integración sensorial, percepción y conciencia.

<a name="archivos"></a>
## Archivo de las señales ploteadas en Python
### Prueba de BiTalino
* **Código en Python**
  - [Código para Estados bases](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/plotEEG1.py)
  - [Código para Estado ojo cerrado-ojo abierto](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/EEGprueba2.py)
  - [Código para segundo reposo](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/EEGreposo2.py)
  - [Código para Estado de preguntas](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/EEGpreguntas2.py)

* **Datos de señales del Bitalino ploteadas en Python**
  - [Estado de reposo](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/BITALINO/EEG1.txt)
  - [Estado de ojos cerrado-ojos abiertos](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/BITALINO/PruebaEEG2.txt)
  - [Estado de segundo reposo](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/BITALINO/EEG3.txt)
  - [Estado de preguntas](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/BITALINO/EEGprueba4.txt)


### Prueba de Ultracortex
* **Código en Python**
  - [Código para Estados bases](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/PLOTBCI(base).py)
  - [Código para Estado ojo cerrado-ojo abierto](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/PLOTBCI_abre_cierra.py)
  - [Código para Estado de preguntas](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/PLOTBCI_preguntas.py)
    
* **Datos de señales eléctricas del Ultracortex ploteadas en Python**
  - [Estado de reposo](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/OpenBCI-RAW-base.txt)
  - [Estado de ojos cerrado-ojos abiertos](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/OpenBCI-RAW-abrecierra.txt)
  - [Estado de segundo reposo](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/OpenBCI-RAW-base2.txt)
  - [Estado de preguntas](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/OpenBCI-RAW-mate.txt)


<a name="discusion"></a>
## Discusión
El análisis de las señales EEG obtenidas durante el estudio de los diferentes estados del sujeto evaluado permiten observar la variabilidad de la presencia de las bandas del EEG, características electroencefalográficas y anatómicas del cerebro para realizar una comparación con valores estándar y anormales. 

Según un estudio realizado por Molina et.al. <sup> [14](https://doi.org/10.3758/s13415-019-00703-5)</sup>, la resolución de problemas complejos requiere un patrón característico de activación y sincronización funcional entre cortices. Estos patrones incluyen un aumento de la activación izquierda (frontal y parietal) asociada a una desactivación de la corteza temporal derecha, así como un aumento de la correlación entre las tres cortices <sup> [16](https://doi.org/10.1146/annurev-neuro-071714-034111)</sup> <sup> [17](https://doi.org/10.1097/00001756-200003200-00004)</sup>. Durante la resolución de los problemas matemáticos de alta complejidad, se registró una mayor actividad en las bandas de frecuencia theta y gamma en las áreas frontales y parietales izquierdas, las cuales están directamente relacionadas con el razonamiento matemático y el cálculo <sup> [18](https://doi.org/10.1007/s11517-024-03028-9)</sup>. Asimismo, se requiere de la activación de la región prefrontal-parietal izquierda, para mantener y manipular múltiple cantidad de información junto con un desacoplamiento funcional de las cortezas parietal-temporal derechas para suprimir el razonamiento dependiente del contexto y centrar más recursos cognitivos en el razonamiento matemático necesario para la resolución de problemas <sup> [19](https://doi.org/10.3389/fnhum.2016.00454)</sup> <sup> [20](https://doi.org/10.3758/s13415-019-00703-5)</sup>. 

Por otra parte, la presencia de artefactos influye directamente en el resultado de la señal, como se observa en los picos obtenidos en las señales, pues produce altas impedancias en los electrodos y por ende, altera los resultados <sup> [21](https://doi.org/10.1111/j.1469-8986.2010.01009.x)</sup>. Los movimientos oculares afectan las lecturas del EEG y constituyen un artefacto en la detección debido a la estructura dipolar de la retina y su proximidad a los electrodos frontales. Los cambios en la posición del ojo generan fluctuaciones en el potencial eléctrico detectado por los electrodos, que permite que aumente y disminuye, alterando así la señal <sup> [12](https://doi.org/10.1016/j.clinph.2006.10.019)</sup>. Asimismo, el parpadeo o conexión eléctrica a otros dispositivos también constituyen artefactos durante la adquisición <sup> [12](https://doi.org/10.1016/j.clinph.2006.10.019)</sup>por lo que una práctica de adquisición recomendada es fijar un punto de referencia para que el sujeto de prueba no presente distracciones, así como evitar tener conexiones cercanas a la zona de adquisición. 

<a name="conclusiones"></a>
## Conclusiones
- Durante los estados de reposo, la señal mostró patrones característicos de actividad cerebral basal, con la presencia de oscilaciones delta y alfa, indicando un estado de relajación.
- En los momentos de apertura y cierre de los ojos, se observaron picos de amplitud en la señal, junto con la aparición de bandas alfa y beta, sugiriendo una respuesta cerebral ante estímulos visuales y atención al entorno.
- La actividad cerebral durante el segundo periodo de reposo fue consistente con el primer estado de reposo, indicando un retorno a un estado de calma después de la actividad.
- Durante la resolución de ejercicios matemáticos, se observaron cambios en la actividad cerebral entre las fases de preguntas simples y complejas. En las preguntas simples, predominaron las bandas beta y theta, mientras que en las preguntas complejas, se registró una mayor presencia de bandas beta y gamma, reflejando un aumento significativo en el procesamiento cognitivo y la atención requerida para resolver problemas más desafiantes.
- La presencia de artefactos cerca del sujeto y que este esté conectado eléctricamente a otros dispositivos pueden generar altas impedancias en los electrodos de EEG y alterar los rangos normales.

En conjunto, esto indica que la señal registrada refleja cambios relacionados con diferentes estados mentales y actividades realizadas por el sujeto.

<a name="referencias"></a>
## Referencias bibliográficas
[1] M. Soufineyestani, D. Dowling, and A. Khan, “Electroencephalography (EEG) Technology Applications and Available Devices,” Applied Sciences, vol. 10, no. 21, p. 7453, Oct. 2020, doi: https://doi.org/10.3390/app10217453.

[2] Mayo Clinic, “Electroencefalografía (EEG) - Mayo Clinic,” www.mayoclinic.org, 2022. https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875

[3] M. K. Islam and A. Rastegarnia, "Recent advances in EEG (non-invasive) based BCI applications," Front. Comput. Neurosci., vol. 17, 1151852, 2023, https://doi.org/10.3389/fncom.2023.1151852

[4] A. U. Patil et al., "Review of EEG-based neurofeedback as a therapeutic intervention to treat depression," Psychiatry Res. Neuroimaging, vol. 329, 111591, 2023, https://doi.org/10.1016/j.pscychresns.2023.111591

[5] M. A. Lopez-Gordo, D. Sanchez-Morillo, y F. Pelayo Valle, "Dry EEG electrodes," Sensors, vol. 14, no. 7, pp. 12847–12870, 2014. [En línea]. Disponible: https://doi.org/10.3390/s140712847

[6] J. Artieda, M. Alegre, M. Valencia, E. Urrestarazu, M. Pérez-Alcázar, M. J. Nicolás, J. López Azcárate, y J. Iriarte, "Oscilaciones cerebrales: papel fisiopatológico y terapéutico en algunas enfermedades neurológicas y psiquiátricas," Anales del Sistema Sanitario de Navarra, vol. 32, Supl. 3, pp. 45-60, 2009. Recuperado el 04 de mayo de 2024, de http://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272009000600004&lng=es&tlng=es.

[7] C. S. Herrmann et al., "EEG oscillations: From correlation to causality," Int. J. Psychophysiol., vol. 103, pp. 12–21, 2016, https://doi.org/10.1016/j.ijpsycho.2015.02.003.

[8] C. S. Nayak and A. C. Anilkumar, "EEG Normal Waveforms," in StatPearls [Internet], Treasure Island (FL): StatPearls Publishing, updated Jul. 24, 2023, Available: https://www.ncbi.nlm.nih.gov/books/NBK539805.

[9] M. Siegel, T. Donner, y A. Engel, "Spectral fingerprints of large-scale neuronal interactions," Nat. Rev. Neurosci., vol. 13, pp. 121–134, 2012. [En línea]. Disponible: https://doi.org/10.1038/nrn3137

[10] S. Beniczky and D. L. Schomer, "Electroencephalography: basic biophysical and technological aspects important for clinical applications," Epileptic Disorders, vol. 22, no. 6, pp. 697–715, Dec. 2020, https://doi.org/10.1684/epd.2020.1217

[11] J. A. Urigüen and B. Garcia-Zapirain, "EEG artifact removal-state-of-the-art and guidelines," J. Neural Eng., vol. 12, no. 3, 031001, Jun. 2015, https://doi.org/10.1088/1741-2560/12/3/031001

[12] M. Fatourechi, A. Bashashati, R. K. Ward, and G. E. Birch, "EMG and EOG artifacts in brain computer interface systems: A survey," Clin. Neurophysiol., vol. 118, no. 3, pp. 480–494, Mar. 2007. [Online]. Available: https://doi.org/10.1016/j.clinph.2006.10.019

[13] PLUX – Wireless Biosignals, “BITalino (r)evolution User Manual” 2020. Disponible en: https://www.pluxbiosignals.com/products/bitalino-revolution-board-kit-ble-bt

[14] J. Molina del Río, M. A. Guevara, M. Hernández González, et al., "EEG correlation during the solving of simple and complex logical–mathematical problems," Cogn Affect Behav Neurosci, vol. 19, pp. 1036–1046, 2019. https://doi.org/10.3758/s13415-019-00703-5

[15] V. Gaviria García, D. Loaiza López, C. Serna Rojas, S. Ríos Arismendy, E. Montoya Guevara, J. D. Mora Lesmes, et al., "Evaluación de los cambios de la actividad eléctrica cerebral durante anestesia general usando electroencefalografía portable," Rev. colomb. anestesiol., vol. 49, no. 2, e201, 2021. Available: http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0120-33472021000200201&lng=en.

[16] A. Z. Harris and J. A. Gordon, "Long-range neural synchrony in behavior," Annual Review of Neuroscience, vol. 38, no. 1, pp. 171–194, 2015. https://doi.org/10.1146/annurev-neuro-071714-034111

[17] A. R. Haig, E. Gordon, J. J. Wright, R. A. Meares, and H. Bahramali, "Synchronous cortical gamma-band activity in task-relevant cognition," NeuroReport, vol. 11, no. 4, pp. 669–675, 2000. https://doi.org/10.1097/00001756-200003200-00004

[18] G. M. Bonança, G. J. L. Gerhardt, A. L. Molan, et al., "EEG alpha and theta time-frequency structure during a written mathematical task," Med. Biol. Eng. Comput., 2024. [En línea]. Disponible: https://doi.org/10.1007/s11517-024-03028-9

[19] S. I. Dimitriadis, Y. Sun, N. V. Thakor, and A. Bezerianos, "Causal interactions between Frontal θ − Parieto-Occipital α2 predict performance on a mental arithmetic task," Frontiers in Human Neuroscience, vol. 10, pp. 1–17, 2016. https://doi.org/10.3389/fnhum.2016.00454

[20] J. Molina, M. A. Guevara, M. Hernández-González, R. M. Hidalgo-Aguirre, M. A. Cruz-Aguilar, and J. C. Hevia, "Cognitive training on the solving of mathematical problems: an EEG study in young men," Act. Psi, vol. 35, no. 130, pp. 131–147, 2021. Available: http://www.scielo.sa.cr/scielo.php?script=sci_arttext&pid=S2215-35352021000100131&lng=en.

[21] E. S. Kappenman y S. J. Luck, "The effects of electrode impedance on data quality and statistical significance in ERP recordings," Psychophysiology, vol. 47, no. 5, pp. 888–904, 2010. [En línea]. Disponible: https://doi.org/10.1111/j.1469-8986.2010.01009.x
