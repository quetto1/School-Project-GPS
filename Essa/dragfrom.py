import psycopg2        #CMD: pip install psycopg2
import time


##############READING FROM DATABASE AND SIGNING INTO VARIABLES X AND Y!#################
connection = psycopg2.connect(user="postgres",
                              password="12345678",
                              host="127.0.0.1",
                              port="5432",
                              database="data1")

print("Using Python variable in PostgreSQL select Query")
cursor = connection.cursor()
postgreSQL_select_Query = "select * from gps where id=(select max(id) from gps)"

cursor.execute(postgreSQL_select_Query)
mobile_records = cursor.fetchall()
for row in mobile_records:
    ID = row[0]
    x = row[1]
    y = row[2]
    
print(ID)
print(x)
print(y)
##########################################################################################