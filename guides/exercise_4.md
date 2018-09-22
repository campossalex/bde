### OBJETIVO
* Ingestar datos desde base de datos

### GUIA
1. El instructor mostrará el formato de datos  

2. Ejecutar el siguiente comando de Sqoop  
`sqoop import --driver com.mysql.jdbc.Driver --connect jdbc:mysql://<IP_DataBase>:3306/taller --username taller --password taller --table orden --split-by orden_trabajo_id --target-dir /user/<tu_nombre>/orden_trabajo`

3. Revisar la ingesta en el directorio HDFS  
`hdfs dfs -ls /user/<tu_nombre>/orden_trabajo`

4. Intentar ejecutar el comando del punto 2 nuevamente.

5. Revisar el mensaje de error que se mosrtrará en pantalla.

### GUIA CONTINUACION

1. Tomando en consideración el comando anterior, modificarlo de la siguiente forma  
`sqoop import --driver com.mysql.jdbc.Driver --connect jdbc:mysql://<IP_DataBase>:3306/taller --username taller --password taller --table orden --split-by orden_trabajo_id --target-dir /user/<tu_nombre>/orden_trabajo --delete-target-dir --as-parquetfile`

2. Revisar la ingesta en el directorio HDFS  
`hdfs dfs -ls /user/<tu_nombre>/orden_trabajo`

### REFERENCIA

https://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html
