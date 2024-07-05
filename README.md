## *Bienvenidos al repositorio del Grupo 8 en el curso “Introducción a Señales Biomédicas”*
_Proyecto realizado por estudiantes de la carrera de Ingeniería Biomédica, pertenecientes a la Pontificia Universidad Católica del Perú (PUCP) y la Universidad Peruana Cayetano Heredia (UPCH), en el semestre 2024-1_


# **PROYECTO: Cardiac arrhythmia classification using deep learning algorithm integrated with HL7 protocol**
La propuesta del proyecto consiste en el desarrollo de un algoritmo de deep learning que permita el análisis de señales ECG obtenidas de monitores Holter para la posterior clasificación de arritmias. Asímismo, diseñamos una interfaz en la cual se podrán visualizar tanto las señales ECG como las clasificaciones arrojadas por nuestro algortimo y utiliza el estándar HL7 para garantizar una monitorización del estado del paciente, para garantizar una integración fluida y eficiente con los diferentes sitemas de información existentes en las instituciones de salud.

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
En un contexto donde las enfermedades cardiovasculares (ECV) representan la principal causa de muerte a nivel global, con un alarmante 31% de los decesos atribuidos a ellas según la Organización Mundial de la Salud <sup>[1](https://www.who.int/news-room/factsheets/detail/cardiovascular-diseases-(cvds))</sup> , las arritmias cardíacas emergen como trastornos críticos que afectan la frecuencia y el ritmo cardíaco. En Perú, estas arritmias muestran una prevalencia significativa entre adultos mayores de 60 años, con un riesgo del 50.8% <sup>[2](https://www.gob.pe/institucion/minsa/noticias/655525-el-50-8-de-personas-de-60-anos-a-mas-tienen-muy-alto-riesgo-de-padecer-de-enfermedades-cardiovasculares.)</sup>. La detección temprana de estas irregularidades cardiacas es crucial, siendo el monitor Holter la herramienta más utilizada para el monitoreo continuo de la actividad eléctrica del corazón durante 24 a 48 horas mediante señales electrocardiográficas (ECG), destacando el análisis de parámetros como el complejo QRS y el intervalo RR. Sin embargo, la escasez de especialistas médicos, especialmente cardiólogos, plantea desafíos significativos para un diagnóstico oportuno y tratamiento efectivo <sup>[3](http://bvs.minsa.gob.pe/local/minsa/3107-2.pdf)</sup>. Además, la falta de métodos automatizados precisos para la clasificación de arritmias y la interoperabilidad limitada entre sistemas de salud y dispositivos de monitoreo ECG subrayan la necesidad urgente de estandarización en la estructura y formato de los datos generados por los Holter, garantizando así una interpretación consistente y decisiones clínicas precisas <sup>[4](10.1016/j.jelectrocard.2018.07.028)</sup> <sup>[5](https://www.iosrjournals.org/iosr-jmca/papers/Vol2-issue2/D0221925.pdf)</sup>.

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
[1]	“Cardiovascular diseases (CVDs).” https://www.who.int/news-room/factsheets/detail/cardiovascular-diseases-(cvds)

[2]	Ministerio de Salud (MINSA), "El 50.8 % de personas de 60 años a más tienen muy alto riesgo de padecer de enfermedades cardiovasculares" [En línea]. Disponible en: https://www.gob.pe/institucion/minsa/noticias/655525-el-50-8-de-personas-de-60-anos-a-mas-tienen-muy-alto-riesgo-de-padecer-de-enfermedades-cardiovasculares. 

[3](N.d.). Gob.Pe. Retrieved July 5, 2024, from http://bvs.minsa.gob.pe/local/minsa/3107-2.pdf

[4]Badilini F., Young B., Brown B., Vaglio M. Archiving and exchange of digital ECGs: A review of existing data formats. J. Electrocardiol. 2018;51:S113–S115. doi: 10.1016/j.jelectrocard.2018.07.028.

[5]Olamidipupo S.A., Danas K. Review of interoperability techniques in data acquisition of wireless ECG devices. IOSR J. Mob. Comput. Appl. 2015;2:19–25.

