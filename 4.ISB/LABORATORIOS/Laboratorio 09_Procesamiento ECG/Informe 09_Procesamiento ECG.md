# Laboratorio N°8 - Procesamiento de señales ECG
## **Tabla de contenidos**
1. [Introducción](#introduccion)\
   1.1 [Marco teórico](#marco)
2. [Objetivos](#objetivos)
3. [Metodología](#metodologia)\
   3.1 [Materiales y equipos](#materiales)\
   3.2 [Procedimiento](#adquisicion)
4. [Resultados](#resultados)\
5. [Archivos](#archivos)
6. [Discusión](#discusion)
7. [Referencias bibliográficas](#referencias)

<a name="introduccion"></a>
## **INTRODUCIÓN**
### **CONTEXTO**




<a name="marco"></a>
### **MARCO TEÓRICO**


<a name="objetivos"></a>
## OBJETIVOS
* Investigar literatura científica sobre técnica de procesamiento de señales electrocardiográficas (ECG).
* Identificar e implementar la mejor técnica filtrado para eliminar el ruido de las señales ECG.
* Implementar un proceso de segmentación de las señales ECG.
* Extraer características relevantes de las señales ECG en diferentes dominios.

<a name="metodologia"></a>
## METODOLOGÍA 
Para este laboratorio, se utilizarán datos de señales ECG adquiridas por el BITalino en la sesión de laboratorio 04. El proceso de adquisición se llevó a cabo siguiendo un protocolo estándar utilizando el dispositivo BITalino y el programa OpenSignal. Inicialmente, se estableció la conexión entre el BITalino y OpenSignal mediante Bluetooth para visualizar las señales en tiempo real. Luego, se conectó el sensor ECG de 3 electrodos al BITalino para comenzar la adquisición de señales.

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
Siguiendo las indicaciones de la guía BITalino (r)evolution Lab Guide 2021 proporcionada por PLUX-Wireless Biosignals <sup>[5](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)</sup>, se implementaron tres protocolos para medir la actividad eléctrica cardíaca en diferentes estados: estado de reposo, estado de respiración prolongada y estado de ejercicio intensivo. Los electrodos se colocaron de acuerdo con las especificaciones del protocolo, garantizando una captura precisa de las señales ECG para realizar la configuración bipolar de Einthoven de la siguiente manera:

* **IN+** (electrodo positivo/rojo) se coloca en la muñeca izquierda .
* **IN-** (electrodo negativo/negro) se coloca en la muñeca derecha.
* **REF** (electrodo de referencia/blanco) se coloca en la cresta ilíaca, debido a que representa una zona de baja interferencia electromagnética.
  
**a. Actividad eléctrica en estado de reposo**: Durante esta prueba, se registró la actividad eléctrica cardíaca del sujeto de prueba en una posición estable y manteniendo la calma. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Actividad eléctrica en estado de respiración prolongada**: El sujeto mantuvo la respiración por 30 segundos y se registró la señal durante la inspiración, mantención y expiración. El registro de la señal fue grabado por 30 segundos. Esta ubicación del electrodo permitió una colocación cómoda y no intrusiva durante las mediciones, lo que resulta beneficioso para evaluar la función cardíaca.

**a. Actividad eléctrica en estado de ejercicio intensivo**: Durante esta prueba, se registró la actividad eléctrica del sujeto de prueba al realizar la actividad física de 10 burpees por 3 minutos y la señal fue registrada durante y después de la actividad realizada. El registro de la señal fue grabado por 30 segundos..

#### DATOS ADQUIRIDOS EMG

En este laboratorio, nos enfocaremos en el análisis y la interpretación de las características de las señales ECG previamente adquiridos, como los picos de la onda R y la variabilidad de la frecuencia cardíaca (HRV). Las señales registradas durante los estado serán utilizadas para el análisis respectivo y así poder extraer conclusiones relevantes sobre la actividad cardíaca de diferentes estados del paciente en diferentes condiciones experimentales. Asimismo, para el cálculo del HRV y parte del procesamiento de la señal se utilizó un artículo de referencia que presentaba un enfoque en tiempo real del análisis del HRV <sup>[6]()</sup>.

#### Pre-procesamiento de la señal
- **Filtrado**

Se aplicó un filtro pasa banda con frecuencias de corte de 0.5Hz para frecuencia inferior y 40 Hz para superior. Estas fueron implementadas para eliminar la línea base, evitar el ruido de alta frecuencia generado por artefactos como la presencia de la actividad muscular no deseada. Este filtrado permitió mejorar la calidad de las señales ECG al eliminar el ruido no deseado y así facilitar la detección de pico.

- **Segmentación**

Las señales de voltaje se segmentaron y anotaron en los puntos P, Q, R, S y T, que corresponden a diferentes intervalos de despolarización/repolarización atrial/ventricular, lo cual resulta relevante para el análisis de la señal al conocer sus características principales.

#### Detección de picos en onda R



#### Cálculo del HRV


- **Extracción de características**


<a name="resultados"></a>
## RESULTADOS


<a name="archivos"></a>
## ARCHIVO DE LA SEÑAL PLOTEADA EN PYTHON
* **Codigo**
  - [EMG](https://github.com/sofiacespedes22/ISB_2024_G8/tree/df24f30fb5e09ca55f7570ee885619f6fd250f00/4.ISB/LABORATORIOS/Laboratorio%2008_Procesamiento%20EMG/Codigos)

<a name="discusion"></a>
## Discusión


<a name="referencias"></a>
## REFERENCIAS BIBLIOGRÁFICAS
