from kafka import KafkaConsumer
from json import loads
consumer = KafkaConsumer('sample', auto_offset_reset='earliest', consumer_timeout_ms=1000, value_deserializer=lambda x: loads(x.decode('utf-8')))
for msg in consumer:
    #print(msg.value)
    print("Key=MYID, Value={}".format(msg.value['MYID']))
    print("Key=MYNAME, Value={}".format(msg.value['MYNAME']))
    print("Key=MYEYECOLOR, Value={}".format(msg.value['MYEYECOLOR']))
consumer.close()