import time
import ttn           
import re
import psycopg2        


#CONNECTING TO POSTGRESQL PART!
##########################################################
connection = psycopg2.connect(user = "postgres",        #CHANGE TO YOUR LOGGING DATA!             
                             password = "7319",     #CHANGE TO YOUR LOGGING DATA! 
                             host = "127.0.0.1",        #CHANGE TO YOUR LOGGING DATA! 
                             port = "5432",             #CHANGE TO YOUR LOGGING DATA! 
                             database = "postgres")        #CHANGE TO YOUR LOGGING DATA! 
cursor = connection.cursor()
# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print('----------------------------------------------')
print("You are connected to - ", record,"\n")
print('----------------------------------------------')
###########################################################

#DON'T CHANGE!
###########################################################
app_id = "28683468"
access_key = "ttn-account-v2.SfH5EtWotwNXsQurNVGwe7NZzvVLGaPQL48DsLO65Ik"
print("Waiting for the message...")
def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print('----------------------------------------------')
  sms=str(msg.payload_fields)
  print(sms)
  print('----------------------------------------------')

  coordinates = []

  for i in range(2):
    coordinates.append(float(re.findall("\d+\.\d+", sms)[i]))

  latitude = coordinates[0]
  longitude = coordinates[1]

  postgres_insert_query = """ INSERT INTO zadanie (x, y) VALUES (%s,%s)"""
  record_to_insert = (latitude, longitude)
  cursor.execute(postgres_insert_query, record_to_insert)

  connection.commit()
  count = cursor.rowcount
  


  print("Latitude:", latitude)
  print("Longitude:", longitude)
  print('----------------------------------------------')
  print (count, "Record inserted successfully into mobile table")
  print('----------------------------------------------')
  print("Waiting for the message...")
  
  ###########################################################


  


handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(250)
mqtt_client.close()

#using application manager client
app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)