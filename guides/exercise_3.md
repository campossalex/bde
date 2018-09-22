### OBJETIVO
* Ejecutar un job MapReduce por medio de Pig, sobre datos estructurados 

### GUIA
1. Ir a la carpeta de Pig  
`cd /taller/pig/`

2. Crear carpeta en HDFS  
`hdfs dfs -mkdir /user/<tu_nombre/movierating`

3. Subir archivo a HDFS  
`hdfs dfs -put movierating.txt /user/<tu_nombre/movierating`

4. Editar el archivo comandos_pig.txt  
`cambiar <tu_nombre> por el valor correspondiente`

5. Ejecutar el Pig Script  
`pig comandos_pig.txt`

### REFERENCIA

http://pig.apache.org/docs/r0.17.0/start.html
