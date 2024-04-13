# LABORATORIO N°3 - Uso de BiTalino para EMG 
## Tabla de contenidos
1. [Lista de participantes](#lista)
2. [Objetivos](#objetivos)
3. [Materiales y Equipos](#materiales)
4. [Entregables](#entregables)
5. [Metodología](#metodologia)
   - [Conexión de BITalino](#m1)
   - [Protocolo de adquisición](#m2)
6. [Resultados y discusión](#resultados)
   - [](#r1)
   - [Señal cuadrada](#r2)
   - [Señal rampa](#r3)
   - [Señal pulso](#r4)
   - [Fuentes de error](#r5)
7. [Referencias bibliográficas](#referencias)

<a name="lista"></a>
## Lista de participantes
- Sofia Camila Céspedes Trece - 71738148
- Nicole Stefany Acuña Malpartida - 71400976
- Chris Margory Viviano Salvatierra - 75138288
- Harold Alonso Alemán Ramírez - 71386429
  
<a name="objetivos"></a>
## Objetivos
1. Adquirir señales biomédicas de EMG y ECG.
2. Hacer una correcta configuración de BiTalino.
3. Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolutiondigital.
   
<a name="materiales"></a>
## Materiales y Equipos
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|(R)EVOLUTION|Kit BITalino|1|<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c8d4e3ed-4054-4c4d-9820-0c1dbd5ddd6f">|
|-|Laptop o PC|1|<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/571d6d42-97c0-461c-8767-a4e8cb3a9318">|
<p align="center"><i>Tabla 1. Materiales y equipos </i></p>
</div>

## Entregables 
- Fotos de conexión usada (Electrodos-cuerpo, BITalino-cables).
-  Video de señal en silencio eléctrico o reposo, que se muestre las conexiones electrodos cuerpo y señal ploteada.
-  Ploteo de la señal en OpenSignals.
-  Resumen y explicación de la señal ploteada.
-  El archivo de los datos de la señal ploteada.
-  Ploteo de la señal en Python.

## Metodología 
### a. Conexión de BITalino
En primer lugar, se realizó la conexión entre el BITalino con el programa OpenSignal para visualizar la señal generada a partir de Bluetooth como se muestra en la Figura 1. Luego, se realizó la conexion EMG en la placa del BITalino utilizando el sensor EMG de 3 electrodos. 
</div>
<p align="center">
<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/04343231-f26e-4609-b82a-0fc0013d6e35">
<p align="center"><i>Figura 1. Conexión del BITalino </i></p>
</div>
   
### b. Protocolo de adquisición
Para la adquisición de las señales EMG, se siguió el procedimiento de la guía BITalino (r)evolution Lab Guide del año 2021 elaborada por PLUX-Wireless Biosignals <sup>[1](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf)</sup> para el posicionamiento de los electrodos en el sujeto de prueba. Se utilizaron 3 protocolos: actividad muscular del bíceps braquial (brazo), del abductor corto del pulgar y del músculo trapecio descendente (superior), de los cuales se realizaron las tomas en reposo, sin oposición y con oposición. 

Para el primer y segundo protocolo, el electrodo de referencia fue colocado en el codo, pues representa un punto neutro, mientras que los otros dos electrodos fueron colocados a lo largo de las fibra muscular a 2 cm de distancia entre ellos. Para el tercer protocolo, el electrodo de referencia se coloco detrás de la oreja como punto neutro, mientras que los otros dos electrodos a lo largo del trapecio para su correcta medición. La representación de estas conexiones se visualiza en la siguiente tabla:

</div>
<p align="center">
|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|  |  |  | <image width="200" height="150" src=""> | 
| |  |  | <image width="200" height="150" src =""> 
|  |  | | <image width="200" height="150" src=""> |
<p align="center"><i>Tabla 2. Representación de posicionamiento de los electrodos según el protocolo </i></p>
</div>
   
## Resultados y discusión


## Referencias bibliográficas
[1] “BITalino (r)evolution Lab Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS”. https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf
