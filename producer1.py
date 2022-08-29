from email import message
from importlib.metadata import metadata
from kafka import KafkaProducer

import datetime
from time import sleep
import random
topic="tempMonitoringSystem"
server="localhost:9092"
while True:

  period = datetime.datetime.now()
  if((period.second % 5) == 0):
      temp = random.randrange(10, 40, 3)
      print(temp)
      producer=KafkaProducer(bootstrap_servers =[server])

      message=producer.send(topic, bytes(str(temp), encoding='utf-8'))
      metadata=message.get()
      print(metadata.topic)
      print(metadata.partition)
      sleep(1)
