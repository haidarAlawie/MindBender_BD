from pyspark import SparkContext                                                                                        
from pyspark.sql import SparkSession                                                                                    
from pyspark.streaming import StreamingContext                                                                          
from pyspark.streaming.kafka import KafkaUtils     
import json                                                                     
                                                                                                                        
def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():
        global ss           
        # create dataframe       

        df = ss.createDataFrame(rdd, schema=['location', 'weather', 'description', 'humidity'])

        df.show()        
        df.write.saveAsTable(name='default.weather', format='hive', mode='append')                                       

# spark context                                                                                                                
sc = SparkContext(appName="Something")
# spark streaming context                                                                                  
ssc = StreamingContext(sc, 5)                                                                                           
# spark session                                                                                                                 
ss = SparkSession.builder.appName("Something").config("spark.sql.warehouse.dir", "/user/hive/warehouse").config("hive.metastore.uris", "thrift://localhost:9083").enableHiveSupport().getOrCreate()

ss.sparkContext.setLogLevel('WARN')

ks = KafkaUtils.createDirectStream(ssc, ['api'], {'metadata.broker.list': 'localhost:9099'})

lines = ks.map(lambda x: x[1])
line = lines.map(lambda x: json.loads(x))



# parse = lines.map(lambda x: json.loads(x))


# get count of words and total length
transform = line.map(lambda row: (row["name"],row['weather'][0]['main'],row['weather'][0]['description'],row['main']['humidity'] ))                                  
print("******************************")
print("******************************")
print("******************************")
print("******************************")
print("******************************")
print(transform)           
print("******************************")
print("******************************")
print("******************************")
print("******************************")
# handle dataframe                                                                                                  
transform.foreachRDD(handle_rdd)
ssc.start()
ssc.awaitTermination()