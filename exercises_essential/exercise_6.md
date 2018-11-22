### OBJETIVO
* Crear una tabla en Hive con Serde para leer datos de logs de eventos de Apache Web Server 

### GUIA
1. Revisar los logs de eventos de acceso de Apache, por consola (Putty o terminal):  
`hdfs dfs -cat /user/hdfs/web_logs/access.log | head`

2. Crear una tabla en Hive por la interface de Hue:  
`CREATE EXTERNAL TABLE <tu_nombre>.access_log (
        ip STRING,
        time_local STRING,
        method STRING,
        uri STRING,
        protocol STRING,
        status STRING,
        bytes_sent STRING,
        referer STRING,
        useragent STRING
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
    WITH SERDEPROPERTIES ('input.regex'='^(\\S+) \\S+ \\S+ \\[([^\\[]+)\\] "(\\w+) (\\S+) (\\S+)" (\\d+) (\\d+) "([^"]+)" "([^"]+)".*')
    LOCATION '/user/hdfs/web_logs';`
    
3. Visualizar los datos  
`SELECT * FROM <tu_nombre>.access_log LIMIT 100;`

4. Ejecutar consultas sobre la tabla  
`CREATE TABLE <tu_nombre>.metricas_accesos AS 
SELECT uri, status, COUNT(*) cantidad FROM <tu_nombre>.access_log GROUP BY uri, status;`

### REFERENCIA

https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL
