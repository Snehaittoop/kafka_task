import mysql.connector
from kafka import KafkaConsumer
import sys
server="localhost:9092"

server_name="localhost"
db_username="root"
db_password=""
db_name="iotdb"
connection=mysql.connector.connect(
host=server_name,user=db_username,password=db_password,database=db_name
)
my_c=connection.cursor()
topic="tempMonitoringSystem"
consumer=KafkaConsumer(topic,bootstrap_servers=server,auto_offset_reset = 'earliest')
try :
    for num in consumer:
        num=str(input("enter the value"))

        print(num)
        my_c.execute("INSERT INTO `temprature`(`temprature`) VALUES (%s)",(num,))
        connection.commit()
        print("data inserted successfully")
        
except KeyboardInterrupt :
    sys.exit()


