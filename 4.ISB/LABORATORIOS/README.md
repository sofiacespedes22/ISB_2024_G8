# Introducción a Señales Biomédicas
Somos un equipo de estudiantes de Ingeniería Biomédica de las universidades PUCP y UPCH. Durante el semestre 2024-1 trabajaremos en un proyecto de adquisición y procesamiento de señales de ECG para pacientes con arritmia.
## Tabla de contenidos
1. [Descripción del curso](#descripcion)
2. [Contexto del Proyecto](#contexto)
   - [¿Qué son las señales biomédicas?](#señal)
   - [¿Cómo se adquiere y procesa las señales del electrocardiograma (ECG)?](#ecg)
4. [Objetivos del curso](#objetivos)
5. [Contenidos](#contenido)
6. [Integrantes](#integrantes)
7. [Docentes del curso](#docentes)
   - [Profesores](#profesores)
   - [Jefes de práctica](#jp)
     
<a name="descripcion"></a>
## Descripción del curso
<div align="justify">
Este curso tiene por objetivo dar al estudiante una formación básica y sólida en los sistemas de adquisición y procesamiento de señales biomédicas. Abordaremos las diferentes materias que están presentes en los procesos de análisis de señales biomédicas tales como: la fisiología, electrónica, informática médica y procesamiento de señales. Asimismo, se desarrollará un proyecto que esté basado en el procesamiento de señales biomédicas. Se darán las bases para que el alumno pueda profundizar en temas más avanzados en los tópicos presentes en los procesos de análisis de señales biomédicas, tales como: introducción al Tiny Machine Learning y análisis de datos estructurados.
</div>

<a name="contexto"></a>

## Contexto del Proyecto

<a name="señal"></a>

### ¿Qué son las señales biomédicas?

<div align="justify">
Las señales biomédicas son representaciones cuantitativas de diversas funciones fisiológicas del cuerpo humano, capturadas a través de varios tipos de dispositivos de medición y sensores. Estas señales pueden ser de naturaleza eléctrica, mecánica, térmica o química y son esenciales para el diagnóstico médico, el monitoreo de condiciones de salud y la realización de investigaciones científicas. Entre las más comunes se encuentran el electrocardiograma (ECG), que registra la actividad eléctrica del corazón para detectar anomalías cardíacas; el electroencefalograma (EEG), que mide la actividad eléctrica en el cerebro y es fundamental en la investigación de trastornos neurológicos y psiquiátricos; y la electromiografía (EMG), que evalúa la actividad eléctrica de los músculos, importante para el diagnóstico de enfermedades neuromusculares.

La captura y análisis de estas señales biomédicas se han transformado radicalmente con los avances tecnológicos, permitiendo ahora una mayor precisión y la posibilidad de realizar seguimientos en tiempo real, lo cual es crucial para intervenciones médicas rápidas y efectivas. El análisis de estas señales a menudo utiliza sofisticadas técnicas de procesamiento de señales y aprendizaje automático, lo que facilita la identificación de patrones sutiles que pueden indicar el inicio de una enfermedad o la respuesta a un tratamiento específico. Así, las señales biomédicas no solo son vitales para la práctica médica actual, sino que continúan impulsando la innovación en el campo de la salud.
</div>
<a name="ecg"></a>

### ¿Cómo se adquiere y procesa las señales del electrocardiograma (ECG)?
La adquisición y procesamiento de señales de electrocardiograma (ECG) implica colocar electrodos en el paciente para capturar las señales eléctricas del corazón, las cuales se amplifican y filtran para eliminar ruidos e interferencias. Estas señales son luego digitalizadas para permitir un análisis computarizado. En el procesamiento, se utilizan algoritmos para identificar y analizar componentes clave de la señal, como las ondas P, QRS y T, que son críticos para diagnosticar condiciones cardíacas. Este proceso integral es esencial en la práctica médica moderna, permitiendo monitorear la salud cardiovascular y detectar anomalías con precisión y eficiencia.
<p align="center">  
<image width="500" height="350" src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/b127d17a-f956-476d-9281-47ab93999567"> 
</p>
<p align="center"><i>Figura 1. Señal biomédica de un electrocardiograma (ECG) </i></p>

</div>

<a name="objetivos"></a>

## Objetivos del curso

<div align="justify">
   
1. Describir las características intrínsecas de las diferentes señales biomédicas teniendo en cuenta los principios fisiológicos y la metodología de adquisición.
2. Formular correctamente algoritmos de procesamiento de señales electrocardiográficas, electromiográfícas y electroencefalográficas en un computador o microcontrolador, utilizando el lenguaje de programación Python.
3. Integrar de manera efectiva los principios básicos de la construcción de sistemas de información en la telemedicina, aplicando los conocimientos adquiridos sobre señales biomédicas.
4. Desarrollar soluciones de ingeniería mediante un prototipo aplicando los conocimientos discutidos en el curso y los principios del método científico.
</div>

<a name="contenido"></a>

## Contenidos
<div align="center">
   
|**Unidad 1: INTRODUCCIÓN Y ADQUISICIÓN DE SEÑALES EMG, ECG Y EEG.**|**Unidad 2: PROCESAMIENTO Y ANÁLISIS DE SEÑALES ECG, EMG y EEG**|**Unidad 3: INTRODUCCIÓN AL ANÁLISIS DE DATOS E INTELIGENCIA ARTIFICIAL.**|
|:------------:|:---------------:|:------------:|
| Introducción, señales biomédicas más usadas. Características de una señal biomédica. | Filtros digitales para señales biomédicas I. | Datos estructurados: Análisis estadístico. |
 | Git y GitHub. | Filtros digitales para señales biomédicas II | Creación de dataset de las señales biomédicas adquiridas. |
| Conceptos básicos de adquisición y ploteo de señales. | Tratamiento de señal EMG, Electromiograma: Análisis básico de la señal y detección de la actividad muscular. | Introducción a la Inteligencia Artificial y TinyML. |
| Electromiograma: Fisiología, medición y características. | Tratamiento de señal ECG, Algoritmo de detección QRS, Dispersión QT (QTd), Variabilidad de la frecuencia cardiaca | Creación de modelos de ML con Edgeimpulse | 
| Electrocardiograma: Anatomía del corazón, Ondas del ECG, Derivaciones, Características y Arritmia. | Tratamiento de señal EEG, Electroencefalograma: Análisis básico de la señal (alpha, beta, gamma y theta | Revisión de informe final. | 
| Electroencefalograma: Ritmos, medición, adquisición, canales |  | Feria de póster | 

</div>
<p align="center"><i>Tabla 1. Contenido del curso</i></p>

<a name="integrantes"></a>

## Integrantes 
|**SOFIA CAMILA CESPEDES TRECE**|**CHRIS MARGORY VIVIANO SALVATIERRA**|**NICOLE STEFANY ACUÑA MALPARTIDA**|**HAROLD ALONSO ALEMÁN RAMIREZ**|
|:-----------------------------:|:-----------------------------------:|:---------------------------------:|:------------------------------:|
|<image src=""> | <image src=""> | <image src=""> | <image src=""> |
|sofia.cespedes@upch.pe|chris.viviano@upch.pe|nicole.acuna@upch.pe|harold.aleman@upch.pe|
|Estudiante de último año de la carrera de Ingeniería Biomédica PUCP-UPCH. Apasionada por los materiales, la nanotecnología y la Ingeniería de Tejidos y Materiales. Actualmente es investigora en el grupo de modificación de materiales (Mod-MAT PUCP).|Estudiante de sépitmo ciclo de la carrera de Ingeniería Biomédica PUCP-UPCH, con interés la Ingeniería de Tejidos y Materiales. Actualmente forma parte del Grupo de Investigación,Innovación y Desarrollo de Ingeniería Clínica (GIIDIC)| Estudiante de noveno ciclo de la carrera de Ingeniería Biomédica PUCP-UPCH, interesada en la aplicación de la ingeniería biomédica en entornos clínicos. Actualmente trabajando en un proyecto de investigación junto con al Grupo de Ciencia de Materiales y Energía Renovables (MatEr).|Estudiante de la carrera de Ingeniería Biomédica PUCP-UPCH. Actualmente realizando pasantías en el Instituto Nacional del Niño y en simulación médica en la UPCH. Además cuenta con una empresa que se dedica a utilizar tecnología para optimizar procesos agropecuarios. 
<p align="center"></i></p>
</div>
<a name="docentes"></a>

## Docentes del curso <a name="id7"></a>

<a name="profesores"></a>

### Profesores
- Umbert Lewis De La Cruz Rodriguez [umbert.de.la.cruz@upch.pe]
- Moisés Stevend Meza Rodriguez [moises.meza@upch.pe]

<a name="jp"></a>

### Jefes de Prácticas
- Julissa Elvira Venancio Huerta [julissa.venancio@upch.pe]
- Jose Alonso Cáceres del Aguila [jose.caceres.d@upch.com]
