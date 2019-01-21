### OBJETIVO
* Ejecutar un job MapReduce por medio de Pig, sobre datos estructurados 

### GUIA
1. Ir a la carpeta de Pig  
`cd /taller/pig/`

2. Crear carpeta en HDFS  
`hdfs dfs -mkdir /user/<tu_nombre>/movierating`

3. Subir archivo a HDFS  
`hdfs dfs -put movierating.csv /user/<tu_nombre>/movierating`

4. Duplicar el archivos de comandos  
`cp comandos_pig.txt comandos_pig_<tu_nombre>.txt`

4. Editar el archivo comandos_pig.txt duplicado  
`cambiar la expresión "<tu_nombre>" en el archivo por el valor correspondiente a la carpeta en HDFS  
Aproveche de revisar y entender que operación analítica ejecutan los comandos`

5. Ejecutar el Pig Script  
`pig comandos_pig_<tu_nombre>.txt`

### REFERENCIA

http://pig.apache.org/docs/r0.17.0/start.html
