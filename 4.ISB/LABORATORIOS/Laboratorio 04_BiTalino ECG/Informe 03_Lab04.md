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

- La onda P indica la despolarización auricular.
- El complejo QRS señala la despolarización ventricular sincronizada.
- La onda T refleja la repolarización ventricular, mientras que la onda U se presenta posteriormente a la despolarización ventricular.
  
Estos elementos, junto con los intervalos como el intervalo PR, el período QRS y el intervalo QT, brindan información valiosa sobre la actividad cardíaca y pueden ser indicativos de diversas condiciones cardíacas. Además, los intervalos RR y PP están relacionados con la duración o frecuencia de los ciclos ventriculares y auriculares, respectivamente. <sup>[4](https://doi.org/10.1016/j.bea.2023.100089)</sup>

</div>
<p align="center">
<image width="500" height="350"src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c90c0996-9e1f-4b7f-887d-b750cb7197ab">
<p align="center"><i>Figura 1. Morfología del ECG: diferentes segmentos de señal de ECG para una persona normal <sup>[4](https://doi.org/10.1016/j.bea.2023.100089)</sup> </i></p>
</div>

#### b. Electrocardiograma
El electrocardiograma (ECG) es una herramienta diagnóstica esencial que registra la actividad eléctrica del corazón. A través de electrodos colocados estratégicamente en el cuerpo, se capturan las señales eléctricas generadas por cada contracción cardíaca. Estas señales se representan gráficamente como ondas en un papel o pantalla. El ECG proporciona una amplia gama de información, incluyendo la velocidad del ritmo cardíaco, la regularidad de los impulsos eléctricos y la fuerza de la actividad eléctrica en distintas regiones del corazón. Además, permite evaluar la morfología de las ondas cardíacas, lo que puede revelar detalles sobre la estructura y función cardíacas. <sup>[5](https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/)</sup>


<a name="objetivos"></a>
## Objetivos
1. Adquirir señales biomédicas de ECG.
2. Hacer una correcta configuración de BiTalino.
3. Extraer la información de las señales ECG del software OpenSignals (r)evolution

<a name="metodologia"></a>
## Metodología 
La metodología seguida para la adquisición y procesamiento de las señales ECG utilizando el kit BITalino fue implementada siguiendo el protocolo de adquisición y posicionamiento de los electrodos de la guía “"BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface"[1]. 

<a name="materiales"></a>
### Materiales y Equipos
<div align="center">
	
|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|(R)EVOLUTION|Kit BITalino|1|<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c8d4e3ed-4054-4c4d-9820-0c1dbd5ddd6f">|
|-|Laptop o PC|1|<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/571d6d42-97c0-461c-8767-a4e8cb3a9318">|
<p align="center"><i>Tabla 1. Materiales y equipos </i></p>
</div>

<a name="adquisicion"></a>
### Adquisición de datos
Para la adquisición de datos, el sujeto de prueba fue un hombre de 22 años con las siguientes características:


<a name="procesamiento"></a>
### Procesamiento de las señales

<a name="resultados"></a>
## Resultados

<a name="discusion"></a>
## Discusión

<a name="conclusiones"></a>
## Conclusiones


<a name="referencias"></a>
## Referencias bibliográficas
[1] V. Gupta and M. Mittal, “ECG Signal Analysis: Past, Present and Future,” IEEE Xplore, Dec. 01, 2018. https://ieeexplore.ieee.org/document/8704365
[2] Mayo Clinic, “Electrocardiogram (ECG or EKG)” www.mayoclinic.org, May 18, 2022. https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983#:~:text=Electrocardiograma-
[3] PLUX – Wireless Biosignals, “BITalino (r)evolution Lab Guide,” Feb. 2021. Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf
[4] T. Anbalagan, M. K. Nath, D. Vijayalakshmi, and A. Anbalagan, “Analysis of various techniques for ECG signal in healthcare, past, present, and future,” Biomedical Engineering Advances, vol. 6, p. 100089, Nov. 2023, doi: https://doi.org/10.1016/j.bea.2023.100089.
[5] MedlinePlus, “Electrocardiograma” medlineplus.gov, Feb. 28, 2023. https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/
