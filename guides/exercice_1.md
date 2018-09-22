### Objetivo

- Interactuar con el componente HDFS
- Familiarizarse con los comandos básicos del HDFS

### Guia

1. Ir a la carpeta principal  
`cd /taller/cdr`

2. Crear carpeta en HDFS  
`hdfs dfs -mkdir /user/<tu_nombre>`  
`hdfs dfs -mkdir /user/<tu_nombre>/cdr`

3. Subir archivo a HDFS  
`hdfs dfs -put /taller/cdr/* /user/<tu_nombre>/cdr`

4. Revisar los archivos agregados al HDFS  
`hdfs dfs -ls /user/<tu_nombre>/cdr`

5. Ver los archivos en Browser  
Ir a http://<IP_NameNode>:50070/ , ir a la pestaña Browser, y buscar los archivos recién subidos al HDFS. 
Revisar los bloques de cada archivo recién agregado.

### Referencia

https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-common/FileSystemShell.html
