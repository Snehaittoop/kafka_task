from kafka import KafkaConsumer
import sys
topic="tempMonitoringSystem"
server="localhost:9092"
consumer=KafkaConsumer(topic,bootstrap_servers=server,auto_offset_reset = 'earliest')
try:
    for i in consumer:
        partition=i.partition
        print(i.value)
except KeyboardInterrupt:
    sys.exit()