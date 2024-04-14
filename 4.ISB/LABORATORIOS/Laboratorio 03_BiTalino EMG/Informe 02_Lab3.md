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
   - [Actividad muscular del bíceps braquial (brazo) - Prueba 01](#d1)
   - [Actividad muscular del del abductor corto del pulgar - Prueba 02](#d2)
   - [Actividad muscular del músculo trapecio descendente (superior) - Prueba 03](#d3)
7. [Ploteo de las señales en python](#ploteado)
   - [Músculo bícep braquial](#a1)
   - [Músculo abductor corto del pulgar](#a2)
   - [Músculo trapecio descendente](#a3)
8. [Archivo de la señal ploteada en Python y de los datos de la señal](#phyton)
   - [Señales ploteadas en python](#r3)
   - [Datos de la señal ploteada](#r4)
9. [Referencias bibliográficas](#referencias)

<a name="lista"></a>
## Lista de participantes
- Sofia Camila Céspedes Trece - 71738148
- Nicole Stefany Acuña Malpartida - 71400976
- Chris Margory Viviano Salvatierra - 75138288
- Harold Alonso Alemán Ramírez - 71386429
  
<a name="objetivos"></a>
## Objetivos
1. Adquirir señales biomédicas de EMG.
2. Hacer una correcta configuración de BiTalino.
3. Extraer la información de las señales EMG del software OpenSignals (r)evolutiondigital.
   
<a name="materiales"></a>
## Materiales y Equipos
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** | **Imagen** |
|:------------:|:---------------:|:------------:|:----------:|
|(R)EVOLUTION|Kit BITalino|1|<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/c8d4e3ed-4054-4c4d-9820-0c1dbd5ddd6f">|
|-|Laptop o PC|1|<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/571d6d42-97c0-461c-8767-a4e8cb3a9318">|
<p align="center"><i>Tabla 1. Materiales y equipos </i></p>
</div>

<a name="entregables"></a>
## Entregables 
- Fotos de conexión usada (Electrodos-cuerpo, BITalino-cables).
-  Video de señal en silencio eléctrico o reposo, que se muestre las conexiones electrodos cuerpo y señal ploteada.
-  Ploteo de la señal en OpenSignals.
-  Resumen y explicación de la señal ploteada.
-  El archivo de los datos de la señal ploteada.
-  Ploteo de la señal en Python.

<a name="metodologia"></a>
## Metodología
<a name="m1"></a>
### a. Conexión de BITalino
En primer lugar, se realizó la conexión entre el BITalino con el programa OpenSignal para visualizar la señal generada a partir de Bluetooth como se muestra en la Figura 1. Luego, se realizó la conexion EMG en la placa del BITalino utilizando el sensor EMG de 3 electrodos. 
</div>
<p align="center">
<image width="200" height="150" src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/04343231-f26e-4609-b82a-0fc0013d6e35">
<p align="center"><i>Figura 1. Conexión del BITalino </i></p>
</div>

<a name="m2"></a>
### b. Protocolo de adquisición
Para la adquisición de las señales EMG, se siguió el procedimiento de la guía BITalino (r)evolution Lab Guide del año 2021 elaborada por PLUX-Wireless Biosignals <sup>[1](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf)</sup> para el posicionamiento de los electrodos en el sujeto de prueba. Se utilizaron 3 protocolos: actividad muscular del bíceps braquial (brazo), del abductor corto del pulgar y del músculo trapecio descendente (superior), de los cuales se realizaron las tomas en reposo, sin oposición y con oposición. 

Para el primer y segundo protocolo, el electrodo de referencia fue colocado en el codo, pues representa un punto neutro, mientras que los otros dos electrodos fueron colocados a lo largo de las fibra muscular a 2 cm de distancia entre ellos. Para el tercer protocolo, el electrodo de referencia se coloco detrás de la oreja como punto neutro, mientras que los otros dos electrodos a lo largo del trapecio para su correcta medición. La representación de estas conexiones se visualiza en la siguiente tabla:

<p align="center">
   
|**Actividad muscular del bíceps braquial (brazo)**|**Abductor corto del pulgar**|**Músculo trapecio descendente (superior)**|
|:------------------------------------------------:|:---------------------------:|:-----------------------------------------:|
| <image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/689819fb-0cc4-48cd-99c5-81426bf539b8"> | <image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/24667bbc-350a-44de-9169-9667bb646216"> | <image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/caf6bed1-0514-4964-908e-9117d88cb320"> | 
<p align="center"><i>Tabla 2. Representación de posicionamiento de los electrodos según el protocolo </i></p>
</div>

<a name="resultados"></a>
## Resultados y discusión
<a name="d1"></a>
### 1. Actividad muscular del bíceps braquial (brazo) - Prueba 01
Se adquirieron las señales a partir de las tomas en reposo y contracción del bíceps braquial considerando la conexión a tierra (electrodo de referencia) en el codo, pues ayuda a reducir la interferencia eléctrica o el ruido que puede ser captado por los electrodos. Se observó la diferencia significativa entre la señal EMG del músculo sin oposición que con oposición debido al incremento de fuerza resultante. Esta toma permite futuras aplicaciones en el área de la rehabilitación biomecánica. Los videos de las tres tomas se observan a continuación:

<p align="center">
   
|  **Actividad muscular del bíceps braquial en reposo** | **Actividad muscular del bíceps braquial sin oposición** | **Actividad muscular del bíceps braquial con oposición** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|:---------------------------------------------------------:|
| <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/78b5ab29-77dc-4d52-bfb3-999ccdad1bd7"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/fc9ff355-4f66-4022-84d8-b755d0d1fd17"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/9afa171d-6c99-4a46-9587-c2937de8ea78"> | 
<p align="center"><i>Tabla 3. Videos de la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo bíceps braquial </i></p>
</div>

<a name="d2"></a>
### 2. Actividad muscular del del abductor corto del pulgar - Prueba 02
Para la segunda adquisición, se realizaron tomas en reposo y contracción del abductor corto del pulgar considerando la conexión a tierra (electrodo de referencia) nuevamente en el codo, pues en este caso permite una fácil colocación de los electrodos sin interferir con el movimiento natural durante la realización de las pruebas. Al igual que para el bíceps braquial, la funcionalidad de esta prueba radica en futuras aplicaciones en cuanto a la rehabilitación de este músculo. Los videos de las tres tomas se observan a continuación:

<p align="center">
   
|  **Abductor corto del pulgar en reposo** | **Abductor corto del pulgar sin oposición** | **Abductor corto del pulgar con oposición** |
|:----------------------------------------:|:-------------------------------------------:|:-------------------------------------------:|
| <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/1b429514-5569-4729-b74f-6aaf23c959f9"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/6d053c5d-6a04-499d-b3aa-1950be9d9ed4"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/bdcb3a51-93c2-49ba-846b-992fbc81f4ab"> | 
<p align="center"><i>Tabla 4. Videos de la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo abductor corto del pulgar.
</i></p>
</div>

<a name="d3"></a>
### 3. Actividad muscular del músculo trapecio descendente (superior) - Prueba 03
Por último, se adquirieron las señales EMG a partir de la toma en reposo y contracción del músculo trapecio descendente considerando la conexión a tierra (electrodo de referencia) sobre el hueso mastoideo pues representa lugar ideal para colocar un electrodo de referencia porque es relativamente inerte en términos de actividad electromiográfica. Las aplicaciones que tiene este tipo de tomas radican en determinar dolor muscular en los hombros, dolores de cabeza o lesiones por esfuerzo en la zona. Los videos de las tres tomas se observan a continuación:

<p align="center">
   
|  **Músculo trapecio descendente en reposo** | **Músculo trapecio descendente sin oposición** | **Músculo trapecio descendente con oposición** |
|:-------------------------------------------:|:----------------------------------------------:|:----------------------------------------------:|
| <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/6071749c-f009-46f8-b410-ed545bd8a189"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/4e5bf39c-6620-40d5-887f-9a256c63b886"> | <video src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/26b2369c-66b6-4e82-9e29-05ee2071da29"> | 
<p align="center"><i>Tabla 5. Videos de la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo trapecio descendente.</i></p>
</div>

<a name="ploteado"></a>
## Ploteo de las señales en python
<a name="a1"></a>
### 1. Músculo bíceps braquial
Se observa las señales ploteadas en OpenSignal del músculo bíceps braquial en las tres tomas realizadas. La toma en reposo

<p align="center">


| **Posición** | **Señal y FFT** |
|:------------:|:---------------:|
| **En reposo**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/26848c36-3aa7-4650-a415-68facd5099dc">|
| **Sin oposición**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/0a5bcecf-0923-4aa1-ab85-5f01b6ec4e50">|
| **Con oposición**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/f60cf9e5-eefe-4e4f-9214-8731e8355ca0">|
<p align="center"><i>Tabla 6. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>
</div>

<a name="a2"></a>
### Músculo abductor corto del pulgar
<p align="center">

| **Posición** | **Señal y FFT** |
|:------------:|:---------------:|
| **En reposo**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/e96274cd-fb87-4d43-a979-3529c5978078">|
| **Sin oposición**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/af073b00-3f88-4e3a-bb94-85ff13b5ef59">|
| **Con oposición**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/74b98b83-5753-491f-b423-6b233ad3d404">|
<p align="center"><i>Tabla 6. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>
</div>

<a name="a3"></a>
### Músculo trapecio descendente
<p align="center">

| **Posición** | **Señal y FFT** |
|:------------:|:---------------:|
| **En reposo**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/141da4a9-e6a1-4cb2-bdb7-ee85c59913aa">|
| **Sin oposición**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/ded1f4fb-bbac-4df7-8610-b5af67fa82a0">|
| **Con oposición**|<image src="https://github.com/sofiacespedes22/ISB_2024_G8/assets/164541825/3684ef21-30c5-4a83-a992-8e614fd4fd8f">|
<p align="center"><i>Tabla 6. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>
</div>

<a name="phyton"></a>
## Archivo de la señal ploteada en Python y de los datos de la señal
<a name="r3"></a>
  - [Señales ploteadas en python](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/7.%20LABORATORIOS/Laboratorio%2003_BiTalino%20EMG/Archivos%20de%20Ploteo/plot.py)
<a name="r4"></a>
  - [Datos de la señal ploteada](https://github.com/sofiacespedes22/ISB_2024_G8/blob/main/7.%20LABORATORIOS/Laboratorio%2003_BiTalino%20EMG/Archivos%20de%20Ploteo/se%C3%B1al.txt)
   
## Referencias bibliográficas
[1] “BITalino (r)evolution Lab Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS”. https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf
