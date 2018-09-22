### OBJETIVO
* Crear una tabla en Impala con los datos ingestados de la base de datos 

### GUIA
1. Copiar la ruta del primer archuivo parquet en directorio HDFS  
`hdfs dfs -ls /user/<tu_nombre>/orden_trabajo`

2. Acceder la consola de Hue o impala-shell (consola línea de comando)  

3. Crear una base de datos en Impala con tu nombre  
`CREATE DATABASE <tu_nombre>;`

4. Crear la tabla externa que apunte al directorio en HDFS  
`CREATE EXTERNAL TABLE <tu_nombre>.orden LIKE PARQUET '<ruta del parquet>' STORED AS PARQUET LOCATION '/user/<tu_nombre>/orden_trabajo';`  
Ejemplo ruta parquet: /user/<tu_nombre>/orden_trabajo/6b672ea3-45fa-4fca-b4ad- 47617245b76e.parquet


5. Describir los campos de la tabla  
`DESCRIBE <tu_nombre>.orden;`

6. Ejecutar queries libres con los datos utilizados. Ejemplos:  
`select * from <tu_nombre>.orden limit 30;`  
`select count(*) from <tu_nombre>.orden;`  
`select tipo_orden_nombre, count(*) from table <tu_nombre>.orden group by tipo_orden_nombre;`  

### REFERENCIA

https://www.cloudera.com/documentation/enterprise/5-8-x/topics/impala_create_table.html
