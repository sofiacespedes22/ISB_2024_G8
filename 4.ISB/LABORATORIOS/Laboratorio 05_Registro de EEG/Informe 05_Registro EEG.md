# Laboratorio N°5 - Procedimiento de registro de señales de electroencefalograma (EEG)
## Tabla de contenidos
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
   5.1 [Archivos](#archivos)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Referencias bibliográficas](#referencias)

<a name="lista"></a>
## Lista de participantes
- Sofia Camila Céspedes Trece - 71738148
- Nicole Stefany Acuña Malpartida - 71400976
- Chris Margory Viviano Salvatierra - 75138288
- Harold Alonso Alemán Ramírez - 71386429
  
<a name="introduccion"></a>
## Introducción

<a name="contexto"></a>
### Contexto

<a name="marco"></a>
### Marco teórico
#### ¿Qué es una señal EEG?
<p align="justify">
El electroencefalograma (EEG) es una técnica de neuroimagen no invasiva que permite el registro de la actividad eléctrica del cerebro mediante la colocación de electrodos en el cuero cabelludo que detectan la señal [ref1]. Estas señales brindan información en cuanto a los diferentes mecanismos operativos que presenta el cerebro, permitiendo la identificación de patrones, trastornos neurológicos y explorar diversos procesos cognitivos como la memoria, atención o percepción [ref2]. Asimismo, el EEG representa un patrón de señal que es obtenida amplificando y registrando el potencial biológico del cerebro en el cuero cabelludo. Este potencial refleja la actividad macroscópica de la superficie cerebral y permite que los electrodos capturen los impulsos eléctricos inherentes y periódicos generados por grupos de células cerebrales [ref3]. Las oscilaciones e voltaje que presentan estas señales revelan cierta actividad cerebral significativa, lo cual se refleja en estados de sueño profundo o en coma, donde las oscilaciones son lentas y las amplitudes elevadas [ref4]. 
 </p>

 ![image](https://github.com/sofiacespedes22/ISB_2024_G8/assets/164461832/1971c8a3-8cf5-4ce0-a9d1-e974308ce70f)

[Ref1] Islam M.K., Rastegarnia A. Recent advances in EEG (non-invasive) based BCI applications. Front. Comput. Neurosci. 2023;17:1151852. doi: 10.3389/fncom.2023.1151852.
[ref2] Patil A.U., Lin C., Lee S.H., Huang H.W., Wu S.C., Madathil D., Huang C.M. Review of EEG-based neurofeedback as a therapeutic intervention to treat depression. Psychiatry Res. Neuroimaging. 2023;329:111591. doi: 10.1016/j.pscychresns.2023.111591.
[ref3] Chaddad, A., Wu, Y., Kateb, R., & Bouridane, A. (2023). Electroencephalography Signal Processing: A Comprehensive Review and Analysis of Methods and Techniques. Sensors (Basel, Switzerland), 23(14), 6434. https://doi.org/10.3390/s23146434
[ref4] B. Giesbrecht and J. Garrett, "Electroencephalography," Reference Module in Neuroscience and Biobehavioral Psychology, Jan. 2024, doi: 10.1016/B978-0-12-820480-1.00007-3.

#### Oscilaciones del EEG
<p align="justify">
Para la interpretación del EEG, es importante considerar la caracterización que presentan las señales en función a su ubicación, amplitud, frecuencia, morfología, continuidad, simetría o reactividad. Sin embargo, el método más utilizado para interpretar es a partir de la frecuencia, estipulando que la señal medida es una mezcla de diferentes frecuencias subyacentes que se consideran reflejo de estados cognitivios, afectivos o de atención. A continuación, se observa una tabla de la clasificación de las ondas cerebrales según la frecuencia [ref5][ref6]:
</p>
<div align="center">
	
|  **Tipo de banda**  | **Frecuencia (Hz)** | **Estado del cerebro** |
|:------------:|:---------------:|:------------:|
|Delta|0.5 - 4.0|<p align="justify"> La banda delta es la oscilación más lenta y de mayor amplitud del EEG. Aparece durante el sueño profundo y contribuye a la consolidación de la memoria y el aprendizaje. Normalmente, se observa en las regiones frontocentrales de la cabeza, pero su presencia en estados de vigilia puede indicar problemas cerebrales como encefalopatía o disfunción focal.</p>|
|Theta|4.0 - 7.0|<p align="justify"> La banda theta del EEG está relacionada con la somnolencia y las etapas iniciales del sueño, predominando en las regiones frontocentrales y reemplazando al ritmo alfa con el aumento de la somnolencia. Además, se intensifica durante emociones fuertes y en tareas mentales desafiantes. Su presencia focal en la vigilia puede indicar disfunción cerebral focal y está asociada con la atención y la memoria de trabajo.</p>|
|Alpha|8.0 - 12.0|<p align="justify"> El ritmo alfa dominante posterior se observa en EEG normales de personas despiertas, ubicado en la región occipital. Es el ritmo de fondo de EEG en adultos y suele mantenerse estable desde los 3 años hasta la novena década de vida en individuos sanos. Variaciones rápidas de este ritmo pueden ocurrir en personas normales. Su ralentización sugiere disfunción cerebral generalizada. El ritmo alfa está relacionado con la relajación y la inhibición sensorial, aumentando con los ojos cerrados y relajación, y disminuyendo con actividad y ojos abiertos.</p>|
|Beta|13.0 - 30.0|<p align="justify"> El ritmo beta es el ritmo EEG más común en adultos y niños normales. Predomina en las regiones frontal y central de la cabeza y se debilita hacia las áreas posteriores. Se relaciona con el pensamiento activo, la concentración y la planificación de movimientos. También puede activarse cuando se observan movimientos de otras personas.</p>|
|Gamma|>30|<p align="justify"> El ritmo gamma pertenece a la clasificación de ondas de alta frecuencia. Su importancia en diversas funciones cognitivas está bien documentada. Estos ritmos pueden ser útiles para detectar desmielinización y otros problemas de integridad cortical. Se sugiere que los ritmos gamma están relacionados con la integración de percepciones sensoriales y la atención.</p>|
<p align="center"><i>Tabla 1. Materiales y equipos </i></p>
</div>

[ref5] Herrmann, C. S., Strüber, D., Helfrich, R. F., & Engel, A. K. (2016). EEG oscillations: From correlation to causality. International journal of psychophysiology: official journal of the International Organization of Psychophysiology, 103, 12–21. https://doi.org/10.1016/j.ijpsycho.2015.02.003
[ref6] Nayak CS, Anilkumar AC. EEG Normal Waveforms. [Updated 2023 Jul 24]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK539805/

#### Activación neural
El cerebro se compone de millones de neuronas interconectadas que generan potenciales eléctricos. Como se mencionó previamente, esta actividad es detectada a partir del EEG, utilizando electrodos que registran los dipolos eléctricos creados por poblaciones neuronales situadas perpendicularmente a la superficie de la cabeza, principalmente por neuronas piramidales ubicadas entre las capas 3 y 5 de la corteza cerebral. Estas neuronas generan campos eléctricos como resultado de señales electroquímicas transmitidas entre ellas. Cuando generan campos eléctricos al mismo tiempo, estos son lo suficientemente significativos para ser captados por el EEG [ref7].Asimismo, a nivel fisiológico, las señales del EEG provienen de las corrientes iónicas transmembrana en las neuronas piramidales; estas células, se encuentran en todas las áreas de la corteza cerebral: occipital, temporal, parietal y frontal, y están siempre orientadas perpendicularmente a la superficie cortical, con el cuerpo celular dirigido hacia el interior del cerebro y las dendritas apuntando hacia la superficie cortical [ref8].

[ref7] Cohen, M. X. (2017). Where does EEG come from  and  what  does  it  mean? Trends  in Neurosciences, 40(4), 208-218.https://doi.org/10.1016/j.tins.2017.02.004
[ref8] S. Beniczky and D. L. Schomer, "Electroencephalography: basic biophysical and technological aspects important for clinical applications," Epileptic Disorders, vol. 22, no. 6, pp. 697–715, Dec. 2020, doi: 10.1684/EPD.2020.1217.

#### Artefactos
Si bien el EEG permite registrar la actividad eléctrica cerebral, también registra actividades eléctricas que se originan en lugares distintos del cerebro. Esta actividad registrada se denomina artefacto pues no es de origen cerebral y puede dificultar la interpretación clínica o el posterior análisis cuantitativo. Los artefactos surgen de fuentes fisiológicas, como ritmo cardíaco, actividad muscular o movimiento ocular y extrafisiológicas, como el ruido ambiental o del propio sistema de medición [ref9][ref10]. Por ello, resulta importante considerar protocolos para la adquisición correcta de las señales EEG que permitan disminuir la mayor cantidad de artefactos y un correcto pre-procesamiento de la señal para su análisis posterior. 
[ref9] Urigüen JA, Garcia-Zapirain B. EEG artifact removal-state-of-the-art and guidelines. J Neural Eng. 2015 Jun. 12 (3):031001.
[ref10] Zhang C, Tong L, Zeng Y, Jiang J, Bu H, Yan B, et al. Automatic Artifact Removal from Electroencephalogram Data Based on A Priori Artifact Information. Biomed Res Int. 2015. 2015:720450.

<a name="objetivos"></a>
## Objetivos
1. Adquirir señales biomédicas de EEG.
2. Hacer una correcta configuración de BiTalino y Ultracortex Mark IV.
3. Extraer la información de las señales ECG del software OpenSignals (r)evolution y OpenBCI
   
<a name="metodologia"></a>
## Metodología 


<a name="materiales"></a>
### 1. Materiales y Equipos
<div align="center">
	
|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
||||
||||
||||
|OpenBCI|Ultracortex Mark IV EEG Headset|1|
|OpenBCI|OpenBCI Cyton 8-channel Board|1|
<p align="center"><i>Tabla 1. Materiales y equipos </i></p>
</div>


<a name="adquisicion"></a>
### 2. Procedimiento


<a name="procesamiento"></a>
### 3. Procesamiento de datos

<a name="resultados"></a>
## Resultados


<a name="archivos"></a>
### Archivo de las señales ploteadas en Python
   
<a name="discusion"></a>
## Discusión

<a name="conclusiones"></a>
## Conclusiones

<a name="referencias"></a>
## Referencias bibliográficas
