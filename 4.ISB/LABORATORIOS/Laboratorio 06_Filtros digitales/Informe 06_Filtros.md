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
7. [Referencias bibliográficas](#referencias)

  
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

</div>
<p align="center">
<image width="600" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8fce10a5-b0d1-4a8f-8879-84d3213e96ce">
<p align="center"><i>Figura 2. Método de ventanas para los filtros FIR <sup>[4](http://www.labbookpages.co.uk/audio/firWindowing.html)</sup> </i></p>
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

</div>
<p align="center">
<image width="300" height="200" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/6e3a61fb-d755-42b7-8d2e-a81cadebc114">
<p align="center"><i>Figura 3. Tipos de filtros IIR [5] </i></p>
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
|-|**Laptop o PC**: Laptop equipada con el programa Python, para poder implementar ahí el código, para realizar los respectivos filtrados|1|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1e850abc-e826-47a5-aa7b-292a134d94ec">|

<p align="center"><i>Tabla 4. Materiales y equipos utilizados</i></p>
</div>

<a name="adquisicion"></a>
### 2. Procedimiento
#### Señal ECG
La señal del electrocardiograma proporciona información sobre la actividad eléctrica cardíaca medida a partir de la diferencia de potencial eléctrico de las derivaciones entre dos electrodos colocados en el sujeto de prueba. Sin embargo, es susceptible a diferentes tipos de ruidos como los provocados por el incorrecto posicionamiento de los electrodos, interferencia electromagnética, limpieza inadecuada de la zona de posicionamiento o artefactos producidos por corriente alterna que afectan la línea base del ECG. Para el filtrado de la señal ECG, se consideró el uso de las señales de electrocardiograma (ECG) obtenidas en el Laboratorio 04, las cuales se obtuvieron en diferentes estados: reposo, respiración controlada y después de realizar actividad física. Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana Blackman para el filtro FIR debido a que estos filtros ofrecen una excelente atenuación de lóbulos secundarios, mejor que las ventanas Hanning y Hamming.  Asimismo, de definió el filtro butterworth para el filtro IIR debido a que tiene una respuesta suave en todas las frecuencias y van disminuyendo de manera constante a partir d ela frecuencia de corte. Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR. A continuación, se definen los parámetros obtenidos a partir de <sup>[6](https://www.researchgate.net/publication/340100534_Implementation_of_Effective_Hybrid_Window_Function_for_ECG_Signal_Denoising)</sup> <sup>[7](https://ieeexplore-ieee-org.ezproxybib.pucp.edu.pe/document/9290646)</sup> para el filtrado de la señal ECG según cada tipo de filtro respectivamente.

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|Notch|Butterworth|
|Frecuencia de corte|0 - 0.5 Hz|40 Hz|
|Frecuencia de muestreo|1000 Hz|1000 Hz|
|Ventana|Blackman|-|
|Orden|56|4|

<p align="center"><i>Tabla 5. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal ECG </i></p>
</div>

#### Señal EMG
La señal del electromiograma brinda información sobre la actividad eléctrica msucular para una futura aplicación en rehabilitación. Al igual que la señal ECG, es susceptible a ruidos los cuales interfieren con la interpretación de la señal muscular. Para el filtrado de la señal EMG, se consideró el uso de las señales de electromiograma (EMG) obtenidas en el Laboratorio 03, las cuales se obtuvieron en diferentes estados: reposo, contracción leve y contracción fuerte al realizar. Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana () para el filtro FIR debido a que (). Asimismo, de definió el filtro () para el filtro IIR debido a que ().  Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR. A continuación, se definen los parámetros obtenidos a partir de [8] <sup>[9](https://doi.org/10.1109/ICPCES.2010.5698652)</sup> para FIR y <sup>[10]()</sup> para IIR de la señal EMG según cada tipo de filtro.

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|Notch||
|Frecuencia de corte|35-45 Hz||
|Frecuencia de muestreo|256 Hz||
|Ventana|-||
|Orden|37||

<p align="center"><i>Tabla 6. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal EMG </i></p>
</div>

#### Señal EEG
Para el filtrado de la señal EEG, se consideró el uso de las señales de electroencefalograma (EEG) obtenidas en el Laboratorio 05, las cuales se obtuvieron en diferentes estados: reposo, durante el parpadeo y mientras se realizaba y respondía preguntas matemáticas. Estas fueron inicialmente filtradas utilizando un filtro pasabandas pues permiten preparar la señal para un procesamiento posterior. Se definió el método de ventana hamming para el filtro FIR debido a que permite la reducción de las oscilaciones y el rizado en las bandas y permitir su identificación. Asimismo, de definió el filtro butterworth para el filtro IIR para detetctar amplitudes de las oscilaciones en las diferentes bandas de frecuencia. Por último, se realizó la comparación entre la señal cruda obtenida y la señal filtrada tanto con FIR como con IIR.A continuación, se definen los parámetros obtenidos a partir de <sup>[11](https://doi.org/10.1080/1448837x.2020.1771662)</sup> <sup>[12](https://doi.org/10.1016/j.clinph.2005.07.025)</sup> para el filtrado de la señal EEG según cada tipo de filtro.

<div align="center">
   
|  **Parámetro**  | **FIR** | **IIR** | 
|:------------:|:---------------:|:------------:|
|Tipo de filtro|Pasa-Baja|Butterworth|
|Frecuencia de corte|0.5 - 50 Hz|0.5 - 50 Hz|
|Frecuencia de muestreo|5000 Hz|1000 Hz|
|Ventana|Hanning|-|
|Orden|2|4|


<p align="center"><i>Tabla 7. Parámetros considerados para el diseño de los filtro FIR e IIR en la señal EEG </i></p>
</div>

En las tres señales analizadas, el objetivo fue analizar cuál de los dos tipos de filtro era más efectivo en minimizar el ruido causado por los diferentes artefactos y mejorar la claridad de las señales para un análisis posterior. Se realizó el ploteo en Python y se tomo en consideración las características de las ondas ECG (complejo QRS e intervalo RR), las características de las onda EMG y de las ondas EEG (extracción de bandas theta, alpha, beta).

<a name="resultados"></a>
## Resultados
### Señal ECG
La señal ECG, adquirida mediante el BITalino con el uso de los electrodos en configuración 10-20, presentó una frecuencia de muestreo de 250 Hz, un filtro para el filtro IIR y el uso de la ventana blackman para el FIR, así como los demás parámetros observados en la Tabla Y. 

En el estado de reposo, se observa la presencia y cantidad del complejo QRS en ambos filtros lo cual indica que es posible determinar la frecuencia cardíaca, además de poder medir el intervalor RR y QT para los valores aproximados de latidos por minuto. Asimismo, observamos en el filtro IIR que la señal se observa menos distorsiona lo cual indica que se ha reducido los ruidos causados por los artefactos durante la medición. El filtrado que logró una mayor reducción de ruido fue el filtro FIR y la ventana blackman.

En el estado de repiración y post-ejercicio, se observa que la señal presenta un mayor intervalo RR, y permite la visualización del complejo QRS para determinar la frecuencia cardíaca y los latidos por minuto en el filtro IIR. Se observa que para el filtro IIR es el que reduce significativamente más el ruido generado, mientras que en FIR se observa un incremento abrupto en los picos, posiblemente debido a la configuración que presenta en el momento del ploteo.

A continuación, se presenta la tabla con los resultados obtenidos tras el filtrado de la señal ECG con los dos tipos de filtro.

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Filtro FIR** | **Filtro IIR** |
|:------------:|:---------------:|:------------:|:------------:|
|Reposo|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/7326d1ac-3a2a-475c-80aa-d6debc45640d">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ebe113fa-64c8-4ef2-9798-6ad36601002f">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/d2f63894-b5b1-4d70-a6fa-9e21822e751f">|
|Respiración|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/9910e9ba-bf53-4c46-8843-cb00d5650169">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ad3fab25-eb17-45e9-85d6-65d22e8d974d">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1643c7a3-6d7a-442d-9e84-4117990f852e">|
|Post-ejercicio|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/175ef340-1c25-447a-a3b2-3a5e8cf41da6">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/42ebd9f2-da7f-4a16-b0fb-15b4940f86e9">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/64636c9a-adaa-4ea9-88af-db8c541273fb">|
<p align="center"><i>Tabla 8. Resumen de la señal filtrada con filtros FIR e IIR para la data ECG </i></p>
</div>

### Señal EMG

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Filtro FIR** | **Filtro IIR** |
|:------------:|:---------------:|:------------:|:------------:|
|Pulgar|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/cc07f5c1-a085-48d6-a8fa-0b3210d32760">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2bf127eb-8d3e-4100-be22-9ee6a6011495">|<image width="300" height="100" src="">|
|Biceps|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/a9297293-a409-4e61-a8b7-0119fa1de8d7">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c3aff2d2-7ace-4b57-a2e1-6d73004293e0">|<image width="300" height="100" src="">|
<p align="center"><i>Tabla 9. Resumen de la señal filtrada con filtros FIR e IIR para la data EMG del pulgar y biceps</i></p>
</div>


### Señal EEG

La señal EEG, adquirida mediante el BITalino con el uso de los electrodos en configuración 10-20, presentó una frecuencia de muestreo de 1000 Hz, un filtro butterworth para el filtro IIR y el uso de la ventana hamming para el FIR, así como los demás parámetros observados en la Tabla x.
 
En el estado de reposo, se observa que la señal presentó una mayor reducción de ruido mediante el filtro FIR y las frecuencias significativas han sido mantenidas. Los ruidos que se consideraron en esta señal son el movimiento ocular presentado y pensamientos del sujeto de prueba. Asimismo, observamos la disminución en la amplitud de la señal para ambos filtros, en la que los picos oscilan entre los 100 y 200 mV, significativamente menor a los picos de la señal original. 

En el estado de parpadeo, observamos que el filtro que permitió una mayor reducción del ruido fue el filtro IIR aplicado, pues vemos una mayor reducción de la amplitud en comparación al filtro FIR. Los ruidos que se consideraron fueron la intensidad luminosa al abrir los ojos y el movimiento ocular. Se utilizó un filtro butterworth el cual permite identificar la presencia de las bandas alfa y theta, presentes durante este estado. Asimismo, se consideró la frecuencia de 12Hz para el diseño del filtro pasa-baja para la adquisición de las bandas alfa presentes. 

En el último estado, el estado de preguntas matemáticas que conlleva a un razonamiento, se observa una mayor reducción del ruido a partir del filtro IIR. Los ruidos considerados en este estado se relacionan con distracciones visuales del sujeto e interferencias electromagnéticas presentes. Observamos que la amplitud en ambos filtros reduce significativamente y los picos entre los 10 y 20 segundos representan el tiempo en el que se realizaron las preguntas de mayor dificultad. Asimismo, en el filtro FIR se obtiene la presencia de las ondas alfa en 13 Hz que indica una actividad mental que requiere de mayor concentración y esfuerzo mental, mientras que en el filtro IIR se obtiene la presencia de las ondas beta y alfa a frecuencias de 13Hz nuevamente y 20 Hz aproxidamente.

A continuación, se presenta la tabla con los resultados obtenidos tras el filtrado de la señal EEG con los dos tipos de filtro.

<div align="center">
	
|  **Campo de actividad**  | **Señal cruda** | **Filtro FIR** | **Filtro IIR** |
|:------------:|:---------------:|:------------:|:------------:|
|Reposo|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/2f0c7a26-45bb-4a92-be6d-2590784faa29">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/0d3f29e9-15fa-4d33-9256-17f61967ced8">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ac25ead8-527a-400e-a33d-90514acf9477">|
|Parpadeo|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/8e0f12c4-fe20-415e-b71a-43bf39d77f5f">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e6385a7a-658b-4867-bd3e-c5d60a612777">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/511995e1-59ee-4166-a3d7-06f37b6d9313">|
|Razonamiento|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/53212f1c-0a72-442b-84c0-e2fcc6ffa68f">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e61526bb-31e0-4bc5-8416-80f903818654">|<image width="300" height="100" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/d308d8f7-828d-4621-b3ca-a0e1c88bcafa">|
<p align="center"><i>Tabla 10. Resumen de la señal filtrada con filtros FIR e IIR para la data EEG </i></p>
</div>

<a name="archivos"></a>
## Archivo de las señales ploteadas en Python
* **Código en Python**
  - [Código para señal ECG]
  - [Código para señal EMG]
  - [Código para señal EEG]


<a name="discusion"></a>
## Discusión





<a name="referencias"></a>
## Referencias bibliográficas
[1] P. Podder, Md. Mehedi Hasan, Md. Rafiqul Islam, and M. Sayeed, “Design and Implementation of Butterworth, Chebyshev-I and Elliptic Filter for Speech Signal Analysis,” International Journal of Computer Applications, vol. 98, no. 7, 2014, doi: 10.5120/17195-7390.

[2] A. de Cheveigné and I. Nelken, “Filters: When, why, and how (not) to use them,” Neuron, vol. 102, no. 2, pp. 280–293, 2019. https://doi.org/10.1016/j.neuron.2019.02.039

[3] R. Oshana, “Overview of DSP algorithms,” in DSP for Embedded and Real-Time Systems, Elsevier, 2012, pp. 113–131. https://doi.org/10.1016/B978-0-12-386535-9.00007-X

[4]“FIR Filters by Windowing - The Lab Book Pages,” www.labbookpages.co.uk. http://www.labbookpages.co.uk/audio/firWindowing.html

[5] “Filter Topology Face Off: A closer look at the top 4 filter types,” Bliley.com. [Online]. Available: https://blog.bliley.com/hs-fs/hubfs/filter_post/filter-response-comparison.png?width=960&name=filter-response-comparison.png. 

[6] M. Das, B. Chandra, and R. Kumar, “Implementation of effective hybrid window function for E.C.G signal denoising,” IIETA, https://www.iieta.org/journals/ts/paper/10.18280/ts.370116 (accessed May 5, 2024).

[7] Basu, S., & Mamud, S. (2020, September). Comparative study on the effect of order and cut off frequency of Butterworth low pass filter for removal of noise in ECG signal. In 2020 IEEE 1st International Conference for Convergence in Engineering (ICCE) (pp. 156-160). https://ieeexplore-ieee-org.ezproxybib.pucp.edu.pe/document/9290646

[8] John R. Hampton”ECG Made Easy. Elsevier Health Sciences, 2008.

[9] R. Chand, P. Tripathi, A. Mathur, and K. C. Ray, “FPGA implementation of fast FIR low pass filter for EMG removal from ECG signal,” in 2010 International Conference on Power, Control and Embedded Systems, 2010.

[10] 

[11] A. Mahabub, “Design and implementation of cost-effective IIR filter for EEG signal on FPGA,” Australian Journal of Electrical and Electronics Engineering, vol. 17, no. 2, pp. 83–91, Apr. 2020, doi: https://doi.org/10.1080/1448837x.2020.1771662

[12] X. Wan, K. Iwata, J. Riera, M. Kitamura, y R. Kawashima, "Artifact reduction for simultaneous EEG/fMRI recording: adaptive FIR reduction of imaging artifacts," Clin. Neurophysiol., vol. 117, no. 3, pp. 681–692, 2006. [En línea]. Disponible: https://doi.org/10.1016/j.clinph.2005.07.025
