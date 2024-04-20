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

* La onda P indica la despolarización auricular.
* El complejo QRS señala la despolarización ventricular sincronizada.
* La onda T refleja la repolarización ventricular, mientras que la onda U se presenta posteriormente a la despolarización ventricular.
  
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
La metodología seguida para la adquisición y procesamiento de las señales ECG utilizando el kit BITalino fue implementada siguiendo el protocolo de adquisición y posicionamiento de los electrodos de la guía **“"BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface"** <sup>[3](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>. 

<a name="materiales"></a>
### 1. Materiales y Equipos
<div align="center">
	
|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|(R)EVOLUTION|**Kit BITalino**:Kit electrónico formada por varios módulos individuales utilizados para la recolección de datos boiomédicos. Se pueden adquirir señales como EMG,ECG o EEG.|1|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c8d4e3ed-4054-4c4d-9820-0c1dbd5ddd6f">|
|-|**Laptop o PC**:Se descargará el software de análisis para procesar las señales|1|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|
|Fluke|**Prosim4**: Simulador de signos vitales diseñado para comprobar y verificar el funcionamiento básico de varios parámetros fisiológicos, como la respiració, presión arterial, entre otros.|1|<image width="100" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/376ac065-9d63-4bc6-b7d6-21d9b7afe0f4">|
|-|**Electrodos**: Registran la actividad eléctrica de los músculos durante la contracción y relajamiento muscular|1|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/21dab0fa-801d-4dd1-b0c9-3b29bf3be7fb">|
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
En primer lugar, se realizó la conexión entre el BITalino con el programa OpenSignal para visualizar la señal generada a partir de Bluetooth. Luego, se realizó la conexion ECG en la placa del BITalino utilizando el sensor ECG de 3 electrodos. Posteriormente, se realizó el posicionamiento de los electrodos en el sujeto de prueba para realizar la configuración bipolar de Einthoven <sup>[3](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>. En esta configuración, se colocaron los electrodos de la siguiente manera, también observada en la Tabla 2:
* **IN+** (electrodo positivo/rojo) se coloca en la muñeca izquierda .
* **IN-** (electrodo negativo/negro) se coloca en la muñeca derecha.
* **REF** (electrodo de referencia/blanco) se coloca en la cresta ilíaca,debido a que representa una zona de baja interferencia electromagnética.

<div align="center">	
	
|  **Colocación de electrodos para la derivación I**  | **Colocación de electrodos en el sujeto de prueba** | 
|:------------:|:--------:|
|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/a393348e-5c2c-40d4-9d7a-012674926f9b">|<image width="100" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c0e7d84a-0ebe-4694-8c91-8a3f3033f92f">|
<p align="center"><i>Tabla 2. Posicionamiento de los electrodos en el sujeto de prueba: IN+ (rojo) e IN-(negro) en las muñecas y REF (blanco) en la cresta ilíaca </i></p>
</div>


#### Protocolo de adquisición
Para la adquisición de datos, se realizó el protocolo de adquisición brindado por la guía en la cual se registraron las señales ECG para el análisis en tres diferentes estados:
a. **Estado de reposo**:El sujeto de prueba se quedó en una posición estable y manteniendo la calma. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.
b. **Estado de respiración prolongada**: El sujeto mantuvo la respiración por 30 segundos y se registró la señal durante la inspiración, mantención y expiración. El registro de la señal fue grabado por 30 segundos.
c. **Estado de ejercicio intensivo**: El sujeto de prueba realizó la actividad física de 10 burpees por 3 minutos y la señal fue registrada durante y después de la actividad realizada. El registro de la señal fue grabado por 30 segundos.

Adicionalmente, se realizó la adquisición de datos del estado de un paciente que llegaría a paro cardíaco utilizado el Prosim4 por cuatro ciclos con los siguientes parámetros, como se observa en la Figura 2:
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

<a name="procesamiento"></a>
### 3. Procesamiento de datos
Para el procesamiento de las señales adquiridas, se realizó el ploteo en Python para el análisis cuantitativo de segmentos específicos y determinar las características de cada señal ECG, así como los intervalos de duración de cada parámetro. Asimismo, se realizó la transformada rápida de Fourier (FFT) para determinar particularidades de una la señal en mucha mayor medida.

<a name="resultados"></a>
## Resultados
### Resultado a
|  **Estado Basal** | **Manteniendo la respiración durante 10 segundos** | **Actividad muscular del bíceps braquial con oposición** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|:---------------------------------------------------------:|
| <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/78b5ab29-77dc-4d52-bfb3-999ccdad1bd7"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/fc9ff355-4f66-4022-84d8-b755d0d1fd17"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/9afa171d-6c99-4a46-9587-c2937de8ea78"> | 
<p align="center"><i>Tabla 3. Videos de la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo bíceps braquial </i></p>
</div>

### b. 

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
