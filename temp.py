import mysql.connector



server_name="localhost"
db_username="root"
db_password=""
db_name="iotdb"
connection=mysql.connector.connect(
host=server_name,user=db_username,password=db_password,database=db_name
)
my_c=connection.cursor()


num=str(input("enter the value"))

print(num)
my_c.execute("INSERT INTO `temprature`(`temprature`) VALUES (%s)",(num,))
connection.commit()
print("data inserted successfully")
