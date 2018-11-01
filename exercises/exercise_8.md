### OBJETIVO
* Ejecutar código Spark para wordcount 

### GUIA

1. Abrir una consola de pyspark:  
`pyspark`  

2. Ejecutar las siguientes léneas, una por una, en la consola:     
`contentRDD =sc.textFile('/user/<tu_nombre>/libros')`  
`nonempty_lines = contentRDD.filter(lambda x: len(x) > 0)`  
`counts = nonempty_lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x,y: x+y)`  
`output = counts.collect()`  
`for (word, count) in output:`  
`    print("%s: %i" % (word, count))`  
Dar 4 espacios antes del print

3. Revisar el resultado.


### REFERENCIA

https://github.com/apache/spark/blob/master/examples/src/main/python/wordcount.py
