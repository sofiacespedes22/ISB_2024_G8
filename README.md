## *Bienvenidos al repositorio del Grupo 8 en el curso “Introducción a Señales Biomédicas”*
_Proyecto realizado por estudiantes de la carrera de Ingeniería Biomédica, pertenecientes a la Pontificia Universidad Católica del Perú (PUCP) y la Universidad Peruana Cayetano Heredia (UPCH), en el semestre 2024-1_


# **PROYECTO: MibHolter: real-time Holter monitor for arrythmia classification using HL7 communication**
Se buscará desarrollar un sistema que permita la adquisición y procesamiento de señales de un electrocardiograma (ECG) para la detección del tipo de arritmia en pacientes adultos a partir de clasificadores (CNN y SVM).

<p align="center">  
<image src ="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/b127d17a-f956-476d-9281-47ab93999567"> 
</p>
<p align="center"><i>Figura 1. Electrocardiograma</i></p>

## Tabla de contenidos
1. [Resumen](#intro)
2. [Motivación](#problematica)
3. [Principales Hallazgos](#estado)
4. [Sobre Nosotros](#analisis)
5. [Docentes](#docentes)
6. [Referencias](#referencias)

<a name="intro"></a>
## Resumen
Este proyecto presenta MibHolter, un monitor Holter de ECG de bajo coste y en tiempo real diseñado para clasificar las arritmias utilizando el estándar HL7 para mejorar la integración de datos con los sistemas sanitarios electrónicos. Los monitores Holter tradicionales se enfrentan a problemas de integración de datos, lo que provoca errores y retrasos en la interpretación médica. La solución que proponemos consiste en utilizar el kit BITalino para la adquisición de señales de ECG, aplicar técnicas de preprocesamiento como el filtrado FIR y Notch, y extraer características para identificar las características significativas del ECG. El sistema emplea el algoritmo K-Nearest Neighbors (kNN) para la clasificación de arritmias y garantiza la visualización y transmisión de datos sin fisuras a través de HL7. Los resultados iniciales demuestran la eficacia de este enfoque, con una elevada precisión de clasificación y un sólido rendimiento a la hora de distinguir las arritmias de los ritmos cardíacos normales. Aprovechando HL7, este proyecto pretende mejorar la monitorización cardiaca en tiempo real y, con ello, la atención al paciente y la eficacia diagnóstica.
<a name="problematica"></a>

## Motivación
El monitoreo cardíaco remoto es una tecnología avanzada que permite la vigilancia continua de la actividad cardíaca de un paciente sin necesidad de su presencia en un entorno clínico. Utilizando dispositivos portátiles o implantables, se recopilan datos cardíacos para su posterior interpretación, lo que mejora el diagnóstico de ciertas patologías. Uno de los dispositivos más utilizados en este ámbito es el monitor Holter, que registra la actividad eléctrica del corazón de forma continua durante 24 a 48 horas <sup>[1](https://www.ncbi.nlm.nih.gov/books/NBK538203/)</sup> , proporcionando datos primarios como el complejo QRS y el intervalo RR. El uso del monitor Holter ha aumentado significativamente con el tiempo, convirtiéndose en una herramienta crucial para los profesionales de la salud en la detección temprana y manejo de arritmias y otras patologías cardíacas. 
Sin embargo, una de las principales limitaciones de los dispositivos Holter tradicionales es la integración de los datos recolectados con los sistemas de información de salud  electrónicos. Los datos de estos dispositivos a menudo requieren procesos manuales de transferencia y conversión, lo que puede llevar a errores y retrasos en la interpretación médica. Esta falta de integración eficaz impide una atención 
médica oportuna y coordinada, afectando negativamente el manejo de los pacientes. <sup>[2](https://digital.ahrq.gov/sites/default/files/docs/citation/pghd-practical-guide.pdf)</sup>
Es por ello, que la motivación principal para desarrollar el proyecto MibHolter surge de la necesidad crítica de mejorar la integración y eficiencia de los datos cardíacos en el monitoreo remoto. A pesar de que los dispositivos Holter tradicionales son esenciales para la detección y manejo de arritmias, enfrentan desafíos significativos en la transmisión y almacenamiento de datos, lo que puede llevar a errores y retrasos en la interpretación médica. Encuestas realizadas a profesionales de la salud revelaron que el 50 % se mostró insatisfecho con los problemas relacionados con la gestión de los dispositivos de monitoreo remoto, señalando la mala conectividad, los problemas de personal y el gran volumen de alertas como principales inconvenientes <sup>[3](https://www.sciencedirect.com/science/article/pii/S2666501821002804)</sup> . La implementación del estándar HL7 se presenta como una solución prometedora para superar estas limitaciones, facilitando la interoperabilidad entre los dispositivos de monitoreo y los sistemas de información de salud electrónicos. Al adoptar HL7, se espera que MibHolter proporcione una transmisión y almacenamiento de datos más eficientes y seguros, permitiendo una atención médica más oportuna y coordinada. Además, este proyecto busca ofrecer una solución rentable y accesible utilizando componentes asequibles como el kit BITalino, haciendo que el monitoreo cardíaco avanzado sea más accesible para una población de pacientes más amplia. En resumen, la integración exitosa de HL7 en MibHolter tiene el potencial de revolucionar el monitoreo cardíaco remoto, mejorando la calidad de la atención médica y optimizando la gestión de datos cardíacos en tiempo real.

<a name="estado"></a>
## Principales hallazgos
MibHolter ha demostrado una eficiencia notable en la obtención de mediciones de señales ECG, así como de la clasificación en el tipo de arritmias. Los principales hallazgos del proyecto incluyen la efectividad del filtrado utilizado, pues se logró una significativa mejor en la claridad de las arritmias. Asimismo, el análisis en tiempo real de las características extraídas resaltó la robustez del sistema al evidenciar parámetros como minRR, maxRR, avgRR y rmsSD. El modelo de clasificación utilizado, kNN, alcanzó una precisión del 97.3% en la clasificación de arritmias, con una baja tasa de error del 2.7% como se observó en la matriz de confusión. Un hallazago fundamente fue la la integración del estándar HL7 en la interfaz de visualización y transmisión de datos, pues asegura una gestion eficiente y segura de los datos del paciente, permitiendo una atención oportuna y coordinada para permitir el telemonitoreo. Estos hallazgos resaltan la capacidad del MibHolter de ser una solución rentable y accesible para la monitorización cardíaca avanzada, promoviendo innovación y mejorando la atención cardíaca mediante la integración de tecnologías de monitoreo remoto. 


<a name="analisis"></a>
## Sobre nosotros

### Referencia al entregable 1:
[Entregable 1](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/1.MIEMBROS%20DEL%20EQUIPO/Grupo8.md)

|**CAMILA CESPEDES TRECE SOFIA**|**CHRIS MARGORY VIVIANO SALVATIERRA**|**NICOLE STEFANY ACUÑA MALPARTIDA**|**HAROLD ALONSO ALEMÁN RAMIREZ**|
|:-----------------------------:|:-----------------------------------:|:---------------------------------:|:------------------------------:|
|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c1777d5e-c6a9-44af-9c63-50191a33c99d"> | <image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2e35eae2-2687-4834-ad24-e1687f64e66e"> | <image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/d8213425-cc5d-4177-a49a-a034dad09d43"> | <image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/991fdbfd-2dc6-4fe9-be24-f5403c0b02b7"> |
|sofia.cespedes@upch.pe|chris.viviano@upch.pe|nicole.acuna@upch.pe|harold.aleman@upch.pe|
|Estudiante de último año de la carrera de Ingeniería Biomédica PUCP-UPCH. Apasionada por los materiales, la nanotecnología y la Ingeniería de Tejidos y Materiales. Actualmente es investigora en el grupo de modificación de materiales (Mod-MAT PUCP).|Estudiante de sépitmo ciclo de la carrera de Ingeniería Biomédica PUCP-UPCH, con interés la Ingeniería de Tejidos y Materiales. Actualmente forma parte del Grupo de Investigación,Innovación y Desarrollo de Ingeniería Clínica (GIIDIC)| Estudiante de noveno ciclo de la carrera de Ingeniería Biomédica PUCP-UPCH, interesada en la aplicación de la ingeniería biomédica en entornos clínicos. Actualmente trabajando en un proyecto de investigación junto con al Grupo de Ciencia de Materiales y Energía Renovables (MatEr).|Estudiante de la carrera de Ingeniería Biomédica PUCP-UPCH. Actualmente realizando pasantías en el Instituto Nacional del Niño y en simulación médica en la UPCH. Además cuenta con una empresa que se dedica a utilizar tecnología para optimizar procesos agropecuarios. 
<p align="center"></i></p>
</div>

<a name="docentes"></a>
## Docentes del curso:

<a name="profesores"></a>
### Profesores
- Umbert Lewis De La Cruz Rodriguez [umbert.de.la.cruz@upch.pe]
- Moisés Stevend Meza Rodriguez [moises.meza@upch.pe]

<a name="jp"></a>
### Jefes de Prácticas
- Julissa Elvira Venancio Huerta [julissa.venancio@upch.pe]
- Jose Alonso Cáceres del Aguila [jose.caceres.d@upch.com]


<a name="referencias"></a>
## Referencias
[1] A. Mubarik and A. M. Iqbal, Holter Monitor. StatPearls Publishing,2022.

[2] “Integrating Patient-Generated Health Data into Electronic Health.Records in Ambulatory Care Settings: A Practical Guide,” Ahrq.gov,Dec-2021. [Online]. Available:https://digital.ahrq.gov/sites/default/files/docs/citation/pghd-practicalguide.pdf. [Accessed: 03-Jul-2024].

[3] M. Harvey and A. Seiler, “Challenges in managing a remote monitoring device clinic,” Heart Rhythm O2, vol. 3, no. 1, pp. 3–7, 2022
