from kafka import KafkaProducer
import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
data = {'MYID':'A20476293', 'MYNAME':'Rutul Mehta', 'MYEYECOLOR':'black'}
producer.send('sample', data)
producer.close()