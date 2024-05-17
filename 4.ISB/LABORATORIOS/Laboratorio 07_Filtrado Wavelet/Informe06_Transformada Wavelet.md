# Laboratorio N°7 - Filtrado con transformada wavelet
## **Tabla de contenidos**
1. [Introducción](#introduccion)\
   1.1 [Contexto](#contexto)\
   1.2 [Marco teórico](#marco)
2. [Objetivos](#objetivos)
3. [Metodología](#metodologia)\
   3.1 [Materiales y equipos](#materiales)\
   3.2 [Procedimiento](#adquisicion)
4. [Resultados](#resultados)\
   4.1 [Señal ECG](#ecg)\
   4.1 [Señal EMG](#emg)\
   4.1 [Señal EEG](#eeg)
5. [Archivos](#archivos)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Referencias bibliográficas](#referencias)

  
<a name="introduccion"></a>
## **Introducción**
<a name="contexto"></a>
### **Contexto**

<a name="marco"></a>
### **Marco teórico**


<a name="objetivos"></a>
## Objetivos
1. Diseño de un filtro IIR a partir de uno de los siguientes tipos: Bessel, Butterworth, Chebyshev, o Elíptico.
2. Diseñar un filtro FIR utilizando dos de las siguientes técnicas de ventaneo: Hanning, Hamming, Bartlett, rectangular, o Blackman.
3. Implementar los filtros diseñados para el acondicionamiento de las señales ECG, EMG y EEG adquiridas en laboratorios pasados

<a name="metodologia"></a>
## Metodología 

<a name="materiales"></a>
### 1. Materiales y Equipos

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|-|**Laptop o PC**: Laptop equipada con el programa Python, para poder implementar ahí el código, para realizar los respectivos filtrados|1|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|

<p align="center"><i>Tabla 4. Materiales y equipos utilizados</i></p>
</div>

<a name="adquisicion"></a>
### 2. Procedimiento
#### Señal ECG


#### Señal EMG




#### Señal EEG

Para el filtrado de la señal EEG, se consideró el uso de las señales de electroencefalograma (EEG) obtenidas en el Laboratorio 05, las cuales se obtuvieron en diferentes estados: reposo, durante el parpadeo, reposo tras el parpadeo y mientras se realizaba y respondía preguntas matemáticas (razonamiento):

**a. Estado de reposo**: El sujeto de prueba se quedó en una posición estable y manteniendo la calma para el registro de una línea base de señal con poco ruido y sin movimientos. Este estado representa nuestra prueba control. El registro de la señal fue grabado por 30 segundos.

**b. Estado de ojos cerrado-ojos abiertos**: El sujeto mantuvo los ojos cerrados y abiertos completando un ciclo (5 veces cada estado), manteniendo ambas fases durante 5 segundos. Para evitar artefactos, el sujeto se mantuvo calmado y mirando hacia un punto específico. El registro de la señal fue grabado por 50 segundos.

**c. Estado de segundo reposo**: Tras la primera actividad, el sujeto de prueba mantuvo nuevamente el estado de calma y sin movimiento como segunda fase de referencia. El registro de la señal fue grabado por 30 segundos.

**d. Estado de preguntas**: Se realizaron una serie de ejercicios matemáticos <sup> [14](https://doi.org/10.3758/s13415-019-00703-5)</sup> de menor a mayor complejidad al sujeto de prueba para que pueda resolverlo mentalmente enfocando su mirada en un punto específicos para evitar artefactos. La duración entre el lapso de registro de la respuesta y la siguiente pregunta fue de 12 segundos. Las preguntas realizadas se observan en la Tabla 4.

<div align="center">
	
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

El filtro utilizado para la eliminación de ruido en la señal es un filtro DWT (continuar). Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada con el DWT para observar la eficiencia del filtrado. A continuación, se definen los parámetros obtenidos para el filtrado de las señales EEG a partir de la literatura de referencia <sup>[X]()</sup>.

<div align="center">
	
|  **Función Wavelet**  | **Nivel** | **Umbral** | **Frecuencia** | **Coeficiente de aproximación** | **Coeficientes de detalle** | 
|:------------:|:---------------:|:------------:|:------------:|:------------:|:------------:|
|bior2.6 (Biorthogonal 2.6)|5|16|1000 Hz|A5| D1, D2, D3, D4, D5|
<p align="center"><i>Tabla 4. Parámetros considerados para el diseño del filtro en la señal EEG </i></p>

</div>

<a name="resultados"></a>
## Resultados

<a name="ecg"></a>
### Señal ECG
<div align="center">

|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Reposo|<image width="300" height="100" src="">|<image width="300" height="100" src="">|
||<image width="300" height="100" src="">|<image width="300" height="100" src="">|
||<image width="300" height="100" src="">|<image width="300" height="100" src="">|
||<image width="300" height="100" src="">|<image width="300" height="100" src="">|
<p align="center"><i>Tabla 8. Resumen de la señal filtrada con DWT para la data EcG </i></p>
</div>

<a name="emg"></a>
### Señal EMG
<div align="center">

|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Reposo|<image width="300" height="100" src="">|<image width="300" height="100" src="">|
||<image width="300" height="100" src="">|<image width="300" height="100" src="">|
||<image width="300" height="100" src="">|<image width="300" height="100" src="">|
||<image width="300" height="100" src="">|<image width="300" height="100" src="">|
<p align="center"><i>Tabla 8. Resumen de la señal filtrada con DWT para la data EMG </i></p>
</div>

<a name="eeg"></a>
### Señal EEG

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Señal filtrada con DWT** |
|:------------:|:---------------:|:------------:|
|Reposo|<image width="300" height="100" src="">|<image width="300" height="100" src="">|
|Parpadeo|<image width="300" height="100" src="">|<image width="300" height="100" src="">|
|Segundo reposo|<image width="300" height="100" src="">|<image width="300" height="100" src="">|
|Razonamiento|<image width="300" height="100" src="">|<image width="300" height="100" src="">|
<p align="center"><i>Tabla 8. Resumen de la señal filtrada con DWT para la data EEG </i></p>
</div>

<a name="archivos"></a>
## Archivo de las señales ploteadas en Python
* **Codigo**
  - [ECG]()
  - [EMG]()
  - [EEG]()

<a name="discusion"></a>
## Discusión


<a name="conclusiones"></a>
## Conclusiones

<a name="referencias"></a>
## Referencias bibliográficas
