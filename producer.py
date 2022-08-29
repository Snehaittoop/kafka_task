
from importlib.metadata import metadata
from kafka import KafkaProducer

read_value=str(input("enter the dta to be send"))
print(read_value)
topic="nestDigital"
server="localhost:9092"
producer=KafkaProducer(bootstrap_servers =[server])
producer=KafkaProducer()
message=producer.send(topic, bytes(read_value, encoding='utf-8'))
metadata=message.get()
print(metadata.topic)
print(metadata.partition)