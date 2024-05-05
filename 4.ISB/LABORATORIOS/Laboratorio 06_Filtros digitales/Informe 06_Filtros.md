# Laboratorio N°6 - Filtros digitales
## **Tabla de contenidos**
1. [Introducción](#introduccion)\
   1.1 [Contexto](#contexto)\
   1.2 [Marco teórico](#marco)
2. [Objetivos](#objetivos)
3. [Metodología](#metodologia)\
   3.1 [Materiales y equipos](#materiales)\
   3.2 [Procedimiento](#adquisicion)\
   3.3 [Procesamiento de datos](#procesamiento)
4. [Resultados](#resultados)\
   4.1 [Prueba con Bitalino](#bitalino)\
   4.2 [Prueba con Ultracortex Mark IV](#ultracortex)
5. [Archivos](#archivos)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Referencias bibliográficas](#referencias)

  
<a name="introduccion"></a>
## **Introducción**
<a name="contexto"></a>
### **Contexto**
Los filtros son herramientas que sirven para eliminar ruidos o extraer partes útiles de una señal. Estos son utilizados en sistemas de comunicación,procesamientos de audio, radar, procesamiento de señales de voz y vídeo y en el procesamiento de señales biomédicas <sup>[1](https://arxiv.org/abs/2002.03130)</sup>.

En el ámbito de la ingeniería biomédica, la obtención y correcta interpretación de señales médicas como ECG, EMG y EEG, son de suma importancia para el diagnóstico de enfermedades e investigación. Es por ello que en el procesamiento de señales biomédicas, los filtros cumplen un papel muy importante, que es el de eliminar ciertas partes que no se desean e interrumpen la interpretación de las mismas <sup>[1](https://arxiv.org/abs/2002.03130)</sup>.
 
<a name="marco"></a>
### **Marco teórico**
#### **a. ¿Qué es un filtro?**
Un filtro es una herramienta que transforma una señal de entrada, representada como "x", en una señal de salida, representada como "y". En este proceso, cada muestra de la forma de onda de salida "y" se calcula como una suma ponderada de varias muestras de la forma de onda de entrada "x".Para un filtro digital:


<a name="objetivos"></a>
## Objetivos

<a name="metodologia"></a>
## Metodología 
La metodología del siguiente laboratorio consistió en el diseño de filtros digitales FIR e IIR para atenuar las frecuencias altas generadas por el ruido en la adquisición y procesamiento de señales ECG, EMG y EEG a partir del protocolo de (incluir nombre) Kit BITalino realizado en laboratorios anteriores. Puesto que las señales adquirida no han atravesado ningún tipo de pre-procesamiento, contienen ruidos debido a los artefactos que surgieron durante la adquisición y por lo tanto resulta relevante la aplicación del filtrado para obtener una mayor claridad de la señal y así una interpretación mas acertada.

<a name="materiales"></a>
### 1. Materiales y Equipos


<a name="adquisicion"></a>
### 2. Procedimiento
#### Señal ECG
La señal del electrocardiograma proporciona información sobre la actividad eléctrica cardíaca medida a partir de la diferencia de potencial eléctrico de las derivaciones entre dos electrodos colocados en el sujeto de prueba. Sin embargo, es susceptible a diferentes tipos de ruidos como los provocados por el incorrecto posicionamiento de los electrodos, interferencia electromagnética, limpieza inadecuada de la zona de posicionamiento o artefactos producidos por corriente alterna que afectan la línea base del ECG. Para el filtrado de la señal ECG, se consideró el uso de las señales de electrocardiograma (ECG) obtenidas en el Laboratorio 03 [ref], las cuales se obtuvieron en diferentes estados: reposo, respiración controlada y después de realizar actividad física. Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana () para el filtro FIR debido a que (). Asimismo, de definió el filtro () para el filtro IIR debido a que (). Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR. A continuación, se definen los parámetros obtenidos a partir de [][] para el filtrado de la señal ECG según cada tipo de filtro.

#### Señal EMG
La señal del electromiograma brinda información sobre la actividad eléctrica msucular para una futura aplicación en rehabilitación. Al igual que la señal ECG, es susceptible a ruidos los cuales interfieren con la interpretación de la señal muscular. Para el filtrado de la señal EMG, se consideró el uso de las señales de electromiograma (EMG) obtenidas en el Laboratorio 04, las cuales se obtuvieron en diferentes estados: reposo, contracción leve y contracción fuerte al realizar (). Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana () para el filtro FIR debido a que (). Asimismo, de definió el filtro () para el filtro IIR debido a que ().  Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR. A continuación, se definen los parámetros obtenidos a partir de [][] para el filtrado de la señal EMG según cada tipo de filtro.

#### Señal EEG
Para el filtrado de la señal EMG, se consideró el uso de las señales de electroencefalograma (EEG) obtenidas en el Laboratorio 05, las cuales se obtuvieron en diferentes estados: reposo, durante el parpadeo y mientras se realizaba y respondía preguntas matemáticas. Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana () para el filtro FIR debido a que (). Asimismo, de definió el filtro () para el filtro IIR debido a que (). Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR.A continuación, se definen los parámetros obtenidos a partir de [][] para el filtrado de la señal EEG según cada tipo de filtro.

En las tres señales analizadas, el objetivo fue analizar cuál de los dos tipos de filtro era más efectivo en minimizar el ruido causado por los diferentes artefactos y mejorar la claridad de las señales para un análisis posterior. Se realizó el ploteo en Python y se tomo en consideración las características de las ondas ECG (complejo QRS e intervalo RR), las características de las onda EMG y de las ondas EEG (extracción de bandas theta, alpha, beta).

<a name="resultados"></a>
## Resultados
### Señal ECG

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|||
|Frecuencia de corte sup|||
|Frecuencia de corte inf|||
|Frecuencia de muestreo|||
|Ventana|||
|Orden|||

<p align="center"><i>Tabla 1. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal ECG </i></p>
</div>

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Filtro FIR** | **Filtro IIR** |
|:------------:|:---------------:|:------------:|:------------:|
|Reposo||||
|Respiración||||
|Post-ejercicio||||
<p align="center"><i>Tabla 1. Resumen de la señal filtrada con filtros FIR e IIR para la data ECG </i></p>
</div>

### Señal EMG

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|||
|Frecuencia de corte sup|||
|Frecuencia de corte inf|||
|Frecuencia de muestreo|||
|Ventana|||
|Orden|||

<p align="center"><i>Tabla 1. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal ECG </i></p>
</div>

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Filtro FIR** | **Filtro IIR** |
|:------------:|:---------------:|:------------:|:------------:|
|Reposo||||
|Contracción leve||||
|Contracción fuerte||||
<p align="center"><i>Tabla 2. Resumen de la señal filtrada con filtros FIR e IIR para la data EMG </i></p>
</div>

### Señal EEG

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|||
|Frecuencia de corte sup|||
|Frecuencia de corte inf|||
|Frecuencia de muestreo|||
|Ventana|||
|Orden|||

<p align="center"><i>Tabla 1. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal ECG </i></p>
</div>

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Filtro FIR** | **Filtro IIR** |
|:------------:|:---------------:|:------------:|:------------:|
|Reposo||||
|Parpadeo||||
|Razonamiento||||
<p align="center"><i>Tabla 3. Resumen de la señal filtrada con filtros FIR e IIR para la data EEG </i></p>
</div>

<a name="archivos"></a>
## Archivo de las señales ploteadas en Python
* **Código en Python**
  - [Código para Estados bases](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/plotEEG1.py)
  - [Código para Estado ojo cerrado-ojo abierto](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/EEGprueba2.py)
  - [Código para segundo reposo](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/EEGreposo2.py)
  - [Código para Estado de preguntas](https://github.com/sofiacespedes22/ISB_2024_G8/blob/ee2fd7eb8a4922d2dcae8d2fab752b2530563190/4.ISB/LABORATORIOS/Laboratorio%2005_Registro%20de%20EEG/C%C3%B3digos%20y%20TXT/EEGpreguntas2.py)


<a name="discusion"></a>
## Discusión


<a name="conclusiones"></a>
## Conclusiones


<a name="referencias"></a>
## Referencias bibliográficas
[1] P. Podder, Md. Mehedi Hasan, Md. Rafiqul Islam, and M. Sayeed, “Design and Implementation of Butterworth, Chebyshev-I and Elliptic Filter for Speech Signal Analysis,” International Journal of Computer Applications, vol. 98, no. 7, 2014, doi: 10.5120/17195-7390.

