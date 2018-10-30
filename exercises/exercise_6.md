### OBJETIVO
* Realizar ingesta de datos en tiempo real con Flume 

### GUIA
1. Ir a Cloudera Manager e iniciar los servicios HDFS, Flume y Hue  

2. Abrir una CLI para instalar telnet (yum install telnet o apt-get install telnet) 

3. Iniciar telnet  
`telnet localhost <puerto>`
Una vez que aparezca el prompt, digitar "Hello World from Flume"

4. Abrir otra CLI para ver los logs de Flume
`tail -f /var/log/flume-ng/flume-cmf*.log`
Usted podrá ver los mensajes que ha ingresado por telnet

### CONTINUACION

Ahora usted deberá modificar la configuración de Flume para almacenar los mensajes en HDFS

1. Ir a Cloudera Manager -> Servicio Flume -> Pestaña Configuración  

2. Crear la siguiente carpeta en HDFS y dar permisos de escritura:
`hdfs dfs -mkdir /user/hdfs`
`hdfs dfs -mkdir /user/hdfs/flume`
`hdfs dfs -mkdir /user/hdfs/flume/events`
`hdfs dfs -chmod 777 /user/hdfs/flume/events`

3. Bajar o buscar "Configuration File" y agregar las siguientes lineas:
`tier1.sinks.sink1.type= HDFS
tier1.sinks.sink1.fileType=DataStream
tier1.sinks.sink1.channel      = channel1
tier1.sinks.sink1.hdfs.path = hdfs://localhost:8020/user/hdfs/flume/events`  

4. Guardar los cambios en "Save" y reiniciar en serviio en "Actions -> Restart":

5. Iniciar telnet  
`telnet localhost <puerto>`
Una vez que aparezca el prompt, digitar "Hello World from Flume"

6. Ver los archivos en Browser:
Ir a http://<IP_NameNode>:50070/ , ir a la pestaña Browser, y buscar los archivos recién creados por el proceso Flume.

### REFERENCIA

https://www.cloudera.com/documentation/other/tutorial/CDH5/topics/ht_flume_to_hdfs.html
