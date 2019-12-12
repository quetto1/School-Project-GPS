from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
from flask_sqlalchemy import SQLAlchemy

import psycopg2        #CMD: pip install psycopg2
import time

#from sqlalchemy.types import Integer
# from models import Tabelka



app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7319@localhost/postgres'
db = SQLAlchemy(app)



##############READING FROM DATABASE AND SIGNING INTO VARIABLES X AND Y!#################
connection = psycopg2.connect(user="postgres",
                              password="7319",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres")

print("Using Python variable in PostgreSQL select Query")
cursor = connection.cursor()
postgreSQL_select_Query = "select * from zadanie where id=(select max(id) from zadanie)"

cursor.execute(postgreSQL_select_Query)
mobile_records = cursor.fetchall()
for row in mobile_records:
    ID = row[0]
    x = row[1]
    y = row[2]
    
# print(ID)
# print(x)
# print(y)
##########################################################################################


# records = db.query(zadanie).all()

animal = 'dog'


@app.route("/")
@app.route("/gps")
def home():
    return render_template ("gps.html",zmienna=animal,id=ID,x=x,y=y, ACCESS_KEY="pk.eyJ1IjoicXVldHRvIiwiYSI6ImNrNDFqa3pxazAxczIzZWtreTVjNDBuZ2cifQ.VHuHd6J5QU_99i-maIYhzg")



if __name__ == "__main__":
    app.run()