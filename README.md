# mis-primeros-programas
iniciacion en el mundo de la programacion en Python con interfaz gráfica basada en Qt
#  GENERACIÓN DE UN POLÍGONO A PARTIR DE COORDENADAS
Programa en Python con interfaz gráfica basada en Qt que permita emplear este programa como un generador de polígono a partir de coordenadas suministradas por el usuario, esto con el fin de identificar la forma y calcular el área y perímetro de un predio del cual sean conocidas sus coordenadas. 

### Pre-requisitos- datos de partida 📋

Los datos de partida consisten en: 

Tabla con los datos de las coordenadas de los vértices que forman el polígono que alindera el predio en formato CSV, estos datos deben estar en un sistema de referencia UTM.

### Resultados 🛠️ 

•	Se obtiene una capa tipo punto en la memoria con opción de exportar si se desea mediante las opciones de QGIS con los vértices del predio. Dentro de los atributos se encuentra las coordenadas de cada uno de ellos.

•	Se obtiene una capa tipo polígono en la memoria con opción de exportar si se desea mediante las opciones de QGIS con la forma del predio. Dentro de los atributos se encuentra especificado el área del predio y la longitud de sus linderos (perímetro).


## Requisitos funcionales. ⚙️

•	Seleccionar el fichero CSV destino el cual debe contener la siguiente información: número del vértice (ID), coordenada Este y coordenada Norte.

•	Se mostrará la información de cálculo de área y perímetro en la tabla de atributos del polígono resultante.

•	Se visualizará en pantalla los vértices del predio, mediante un objeto en geometría tipo punto.

•	Se visualizará en pantalla la forma del predio, trazándose un objeto en geometría tipo polígono.

### Resultados y conclusiones 🔩

El programa desarrollado permite generar una herramienta sencilla para identificar la forma, área y perímetro de un predio el cual ha tenido un levantamiento topográfico y se conocen las coordenadas de los puntos que delimitan sus linderos. 

### Líneas abiertas de trabajo: posibles mejoras o alternativas. ⌨️

•	Como posible mejora se puede implementar el hecho de que los resultados queden exportados como funcionalidad del complemento, como una capa externa para realizar otros procesos sobre ella.

•	Permitir al usuario ingresar las coordenadas 1 a 1 sin necesidad de cargar un archivo CSV

•	Permitir al usuario ingresar coordenadas geográficas de los linderos para que el complemento realice la conversión y pueda calcular el área del polígono.

## Autores ✒️
### VIVIANA ANDREA ESCOBAR MARQUEZ

INGENIERA CATASTRAL Y GEODESTA 
-UNIVERISIDAD DISTRITAL FRANCISCO JOSE DE CALDAS

GEOGRAFA 
-UNIVERSIDAD NACIONAL DE COLOMBIA

ESTUDIANTE MAESTRIA GEOTECNOLOGIAS CARTOGRAFICAS PARA INGENIERIA Y ARQUITECTURA
-UNIVERSIDAD DE SALAMANCA USAL
