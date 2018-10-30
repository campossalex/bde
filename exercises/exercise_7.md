### OBJETIVO
* Realizar ingesta de datos en formato csv en Hbase 

### GUIA

1. Ir a la carpeta principal  
`cd /taller/hbase`

2. Crear carpeta en HDFS  
`hdfs dfs -mkdir /user/<tu_nombre>`  
`hdfs dfs -mkdir /user/<tu_nombre>/emp_data`

3. Subir archivo a HDFS  
`hdfs dfs -put /taller/hbase/* /user/<tu_nombre>/emp_data`

4. Crear la tabla en Hbase  
`hbase shell`   
`create 'emp_data',{NAME => 'info'}`

5. Cargar la información en Hbase  
`hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY,info:ename,info:designation,info:manager,info:hire_date,info:sal,info:deptno' emp_data /user/hdfs/emp_data/emp_data.csv`

6. Realizar operaciones sobre los datos
`hbase shell`  
`scan 'emp_data'`  
`get 'emp_data', '7369'`   
`put 'emp_data', '7369', 'info:sal','1500'`  
`get 'emp_data', '7369'`  
`count 'emp_data'`  


### REFERENCIA

https://www.cloudera.com/documentation/other/tutorial/CDH5/topics/ht_flume_to_hdfs.html
