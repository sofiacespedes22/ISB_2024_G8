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
#### **a. ¿Qué es un filtro?** <sup>[2](https://www.sciencedirect.com/science/article/pii/S0896627319301746?via%3Dihub)</sup>
Un filtro es una herramienta que transforma una señal de entrada, representada como "x", en una señal de salida, representada como "y". En este proceso, cada muestra de la forma de onda de salida "y" se calcula como una suma ponderada de varias muestras de la forma de onda de entrada "x".Para un filtro digital:

</div>
<p align="center">
<image width="200" height="50" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ae6d4322-dd94-4925-ae12-de12c6bef0a8">
<p align="center"><i>Figura 1. Actividad cerebral registrada por encefalograma [2] </i></p>
</div>

Donde "t" es el punto de análisis en el tiempo, y "h(n)", n = 0,1, …, N es la respuesta al impulso. Esta operación se llama convolución.

La salida de un filtro difiere de su entrada según la forma específica de la respuesta al impulso del filtro. Algunos filtros pueden suavizar la forma de onda de entrada, mientras que otros pueden realizar rápidas variaciones. Existe una amplia teoría y métodos para diseñar y aplicar filtros de acuerdo a las necesidades de una aplicación.

Se muestran cuatro tipos comunes de filtros: paso bajo, paso alto, paso de banda y rechazo de banda (o notch).

* **Filtros de paso bajo**: Son aquellos filtros que atenúan las frecuencias altas y permiten el paso de frecuencias por debajo de un punto de corte, conocida como frecuencia de corte (fc).
* **Filtros de paso alto**: Son aquellos filtros que atenúan las frecuencias bajas, por debajo de una frecuencia de corte especfíca y permiten el paso de señales de alta frecuencia. 
* **Filtros de paso de banda**: Estos filtros atenúan las frecuencias fuera de la banda de interés y permiten el paso de las frecuencias que se encuentren dentro de la banda. 
* **Filtros notch**: Son filtros que se encargan de bloquear un rango específico de frecuencias y permite el paso de las frecuencias fuera de esa banda.

La transición de frecuencia puede ser gradual (azul) o abrupta (roja), lo que influye en la longitud de la respuesta al impulso en el dominio del tiempo. La velocidad de estas transiciones depende del tipo y orden del filtro.

#### **b. Filtros analógicos y digitales**
Entre los filtros, podemos encontrar 2 tipos, los analógicos y los digitales:
* **Filtros analógicos**: Los filtros analógicos emplean circuitos electrónicos discretos como resistencias, condensadores, entre otros. Estos filtros pueden tomar cualquier valor dentro de un intervalo, es decir tratamiento de señales continuas en el tiempo. 
* **Filtros digitales**: Los filtros digitales son sistemas lineales e invariantes en el tiempo discreto y usan procesadores digitales que efectúan operaciones matemáticas en valores muestreados de la señal, es decir, que toma valores discretos. 

#### **c. Tipos filtros digitales** 
Ahora hablando específicamente de los filtros digitales, estos podemos dividirlos en 2 clases, los filtros de respuesta al impulso finito (FIR) y los filtro de respuesta al impulso infinito (IIR). Ahora, adaptando la fórmula general de los filtros a cada uno, obtenemos las siguientes fórmulas que se pueden observar en la _Tabla 1_.

<div align="center">
	
|**FILTRO IIR**|**FILTRO FIR**|
|:------------:|:------------:|
|<image width="200" height="50" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/010fef30-58b0-4b02-abe4-acc5691e5d6b">|<image width="200" height="50" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e3558b0a-cca9-4585-bbd0-1b01795e6a80">|
<p align="center"><i>Tabla 1. Representaciones de los filtros IIR y FIR </i></p>
</div>


##### **c.1. Filtros FIR**: <sup>[3](https://doi.org/10.1016/B978-0-12-386535-9.00007-X)</sup>
Los filtros FIR (Finite Impulse Response) son aquellos que no utilizan retroalimentación en su ecuación, lo que les otorga estabilidad inherente. Esta característica los hace ideales para aplicaciones que requieren fases lineales, ya que pueden producir estas fases de manera consistente. Sin embargo, debido a la falta de retroalimentación, los filtros FIR tienden a requerir más coeficientes en su ecuación para cumplir con los mismos requisitos que un filtro IIR, lo que resulta en una mayor carga computacional y de memoria, especialmente en sistemas exigentes. 

###### **Diseño de Filtros FIR**:
La clave para diseñar un filtro FIR eficaz radica en encontrar los coeficientes adecuados. Hoy en día existen varios algoritmos eficientes y programas de diseño de software que facilitan este proceso de cálculo. Una vez que se obtienen los coeficientes, implementar el filtro en un algoritmo resulta relativamente sencillo.

Una técnica popular para diseñar filtros FIR es la ventana (windowing). Esta técnica implica generar los coeficientes de frecuencia a partir de una respuesta al impulso ideal. Sin embargo, la respuesta en el dominio del tiempo de esta respuesta al impulso ideal puede ser infinitamente larga, lo que presenta un problema al truncar el filtro, ya que esto puede generar oscilaciones alrededor de la frecuencia de corte en el dominio de la frecuencia debido a las discontinuidades en el dominio del tiempo. Para mitigar este problema, se utiliza una técnica llamada “windowing”.Esta consiste en multiplicar los coeficientes en el dominio del tiempo por un algoritmo que suavice los "bordes" de los coeficientes. El compromiso aquí es reducir las oscilaciones a costa de aumentar el ancho de transición. 

Existen varias ventanas populares, cada una con un equilibrio entre el ancho de transición y la atenuación de la banda de parada. Algunos tipos podemos observarlos en la _Tabla 2_

<div align="center">
	
|  **Tipo**  | **Descripción** |
|:----------:|:-------------------:|
|**Rectangular**|<p align="justify">Transición más afilada, con menor atenuación en la banda de parada (21 dB)</p>|
|**Hanning**|<p align="justify">Transición más suave que la rectangular, con una atenuación de 30 dB</p>|
|**Haming**|<p align="justify">Transición aún más suave que la Hanning, con 40 dB de atenuación</p>|
|**Blackman**|<p align="justify">Transición aún más suave que la Hamming, con 74 dB de atenuación</p>|
|**Kaiser**|<p align="justify">Permite generar ventanas personalizadas según la atenuación de la banda de parada deseada</p>|
<p align="center"><i>Tabla 2. Tipos de filtros FIR </i></p>
</div>

Al diseñar un filtro utilizando la técnica de ventana, el primer paso es decidir qué ventana sería apropiada según las curvas de respuesta o el ensayo y error. Luego, se elige el número deseado de coeficientes del filtro y una vez determinada la longitud y el tipo de ventana, se pueden calcular los coeficientes de la ventana y multiplicarlos por la respuesta del filtro ideal.

##### **c.2. Filtros IIR**: <sup>[3](https://doi.org/10.1016/B978-0-12-386535-9.00007-X)</sup>
Por otro lado, los filtros IIR (Infinite Impulse Response) utilizan tanto las entradas como las salidas anteriores en su ecuación, lo que les permite operar de manera más eficiente en términos de requisitos computacionales. Esto se debe a la retroalimentación que incorporan en su diseño. Sin embargo, mantener una fase lineal en los filtros IIR es más difícil de lograr debido a esta retroalimentación. A pesar de ello, los filtros IIR son una opción preferida cuando se busca reducir la carga del sistema y el número de coeficientes necesarios en la ecuación del filtro.

Los filtros IIR al incorporar retroalimentación en su ecuación, permite que la ecuación contenga significativamente menos coeficientes que sus contrapartes FIR, aunque también puede distorsionar la fase y complicar el diseño e implementación del filtro.

###### **Diseño de Filtros IIR**:
Se diseñan mediante dos técnicas principales: el diseño directo y el diseño indirecto. El diseño directo opera en el dominio digital (z), mientras que el diseño indirecto trabaja en el dominio analógico (s) y luego convierte los resultados al dominio digital. Las técnicas analógicas optimizadas, como Butterworth, Chebyshev, Chebyshev II, Bessel y Eliptical, son comúnmente utilizadas en el diseño indirecto y pueden observarlas mejor en la _Tabla 3_

<div align="center">
	
|  **Tipo**  | **Descripción** |
|:----------:|:-------------------:|
|**Butterworth**|<p align="justify">Este filtro es utilizado para una ondulación plana en la banda de paso. Además de ello, mientras va aumentando la frecuencia, la respuesta en magnitud no aumentará. </p>|
|**Chebyshev**|<p align="justify"> Estos filtros se encargan de maximizar la pendiente de la característica de ganancia en la región de transición, ya que tienen una transición más pronunciada que la Butterworth, con el coste de una mayor fluctuación en la banda de paso.</p>|
|**Chebyshev II**|<p align="justify"> Estos filtros tienen la banda de paso monótona pero agrega ondas a la banda de parada. </p>|
|**Bessel**|<p align="justify"> Estos filtros tienen como objetivo lograr una respuesta de fase lineal en un margen de frecuencias amplio alrededor de la frecuencia de corte. La ganancia en la banda de paso no es tan plana como en un filtro Butterworth ni la pendiente en la banda de transición tan acentuada como en un filtro Chebyshev. </p>|
|**Eliptical**|<p align="justify"> se caracteriza por tener ondulaciones constantes tanto en la banda de paso como en la banda de corte. </p>|
<p align="center"><i>Tabla 3. Tipos de filtros IIR </i></p>
</div>

Para el diseño indirecto, se utilizan técnicas analógicas optimizadas para desarrollar el filtro, y luego se convierten al dominio digital mediante la Transformación Bilineal. Esta técnica mapea todas las frecuencias en el círculo unitario de manera no lineal, por lo que es necesario "pre-warpear" las frecuencias antes del diseño del filtro.


<a name="objetivos"></a>
## Objetivos
1. Diseño de un filtro IIR a partir de uno de los siguientes tipos: Bessel, Butterworth, Chebyshev, o Elíptico.
2. Diseñar un filtro FIR utilizando dos de las siguientes técnicas de ventaneo: Hanning, Hamming, Bartlett, rectangular, o Blackman.
3. Implementar los filtros diseñados para el acondicionamiento de las señales ECG, EMG y EEG adquiridas en laboratorios pasados

<a name="metodologia"></a>
## Metodología 
La metodología del siguiente laboratorio consistió en el diseño de filtros digitales FIR e IIR para atenuar las frecuencias altas generadas por el ruido en la adquisición y procesamiento de señales ECG, EMG y EEG a partir del protocolo de (incluir nombre) Kit BITalino realizado en laboratorios anteriores. Puesto que las señales adquirida no han atravesado ningún tipo de pre-procesamiento, contienen ruidos debido a los artefactos que surgieron durante la adquisición y por lo tanto resulta relevante la aplicación del filtrado para obtener una mayor claridad de la señal y así una interpretación mas acertada.

<a name="materiales"></a>
### 1. Materiales y Equipos

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|-|**Laptop o PC**: Laptop equipada con el programa Python, para poder implementar ahí el código, para realizar los respectivos filtrados|1|<image width="300" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|

<p align="center"><i>Tabla 4. Materiales y equipos utilizados</i></p>
</div>

<a name="adquisicion"></a>
### 2. Procedimiento
#### Señal ECG
La señal del electrocardiograma proporciona información sobre la actividad eléctrica cardíaca medida a partir de la diferencia de potencial eléctrico de las derivaciones entre dos electrodos colocados en el sujeto de prueba. Sin embargo, es susceptible a diferentes tipos de ruidos como los provocados por el incorrecto posicionamiento de los electrodos, interferencia electromagnética, limpieza inadecuada de la zona de posicionamiento o artefactos producidos por corriente alterna que afectan la línea base del ECG. Para el filtrado de la señal ECG, se consideró el uso de las señales de electrocardiograma (ECG) obtenidas en el Laboratorio 03 [ref], las cuales se obtuvieron en diferentes estados: reposo, respiración controlada y después de realizar actividad física. Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana hamming para el filtro FIR debido a que (). Asimismo, de definió el filtro butterworth para el filtro IIR debido a que (). Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR. A continuación, se definen los parámetros obtenidos a partir de [][] para el filtrado de la señal ECG según cada tipo de filtro.

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|Notch|Butterworth|
|Frecuencia de corte|0.5 - 108 Hz|40 Hz|
|Frecuencia de muestreo|-||
|Ventana|Hamming|-|
|Orden|56|4|

<p align="center"><i>Tabla 1. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal ECG </i></p>
</div>

#### Señal EMG
La señal del electromiograma brinda información sobre la actividad eléctrica msucular para una futura aplicación en rehabilitación. Al igual que la señal ECG, es susceptible a ruidos los cuales interfieren con la interpretación de la señal muscular. Para el filtrado de la señal EMG, se consideró el uso de las señales de electromiograma (EMG) obtenidas en el Laboratorio 04, las cuales se obtuvieron en diferentes estados: reposo, contracción leve y contracción fuerte al realizar (). Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana () para el filtro FIR debido a que (). Asimismo, de definió el filtro () para el filtro IIR debido a que ().  Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR. A continuación, se definen los parámetros obtenidos a partir de [][] para el filtrado de la señal EMG según cada tipo de filtro.


#### Señal EEG
Para el filtrado de la señal EMG, se consideró el uso de las señales de electroencefalograma (EEG) obtenidas en el Laboratorio 05, las cuales se obtuvieron en diferentes estados: reposo, durante el parpadeo y mientras se realizaba y respondía preguntas matemáticas. Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana () para el filtro FIR debido a que (). Asimismo, de definió el filtro () para el filtro IIR debido a que (). Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR.A continuación, se definen los parámetros obtenidos a partir de [][] para el filtrado de la señal EEG según cada tipo de filtro.

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro||-|
|Frecuencia de corte|0.5 Hz||
|Frecuencia de muestreo|-|-|
|Ventana|Hamming||
|Orden|56||

EMG
<p align="center"><i>Tabla 1. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal ECG </i></p>
</div>

|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|Notch||
|Frecuencia de corte|35-45 Hz||
|Frecuencia de muestreo|256 Hz||
|Ventana|-||
|Orden|37||

<p align="center"><i>Tabla 1. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal EMG </i></p>
</div>

En las tres señales analizadas, el objetivo fue analizar cuál de los dos tipos de filtro era más efectivo en minimizar el ruido causado por los diferentes artefactos y mejorar la claridad de las señales para un análisis posterior. Se realizó el ploteo en Python y se tomo en consideración las características de las ondas ECG (complejo QRS e intervalo RR), las características de las onda EMG y de las ondas EEG (extracción de bandas theta, alpha, beta).

<a name="resultados"></a>
## Resultados
### Señal ECG

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

[2] A. de Cheveigné and I. Nelken, “Filters: When, why, and how (not) to use them,” Neuron, vol. 102, no. 2, pp. 280–293, 2019. https://doi.org/10.1016/j.neuron.2019.02.039

[3] R. Oshana, “Overview of DSP algorithms,” in DSP for Embedded and Real-Time Systems, Elsevier, 2012, pp. 113–131. https://doi.org/10.1016/B978-0-12-386535-9.00007-X

[4] Electrositio, '¿Qué Es Un Filtro Analógico? - Diferentes Tipos De Filtros Analógicos,' Electrositio, 2023. [En línea]. Disponible: https://electrositio.com/que-es-un-filtro-analogico-diferentes-tipos-de-filtros-analogicos/. [Accedido: 03-may-2024].
