from __future__ import print_function
from flask import Flask, request, session, g, redirect, url_for, render_template
import psycopg2       
import time
import simplejson as json

app =Flask(__name__)

# Rendering templates, home template
@app.route("/")
@app.route("/home")
def home():
    return render_template ("home.html")

# Gallery template
@app.route("/gallery")
def gallery():
    return render_template ("gallery.html")
    
# GPS template which contains map and script responsible for update the coordinates 
@app.route("/gps")
def gps():
    # Getting and passing the acces mapbox key to gos template
    return render_template ("gps.html", ACCESS_KEY="pk.eyJ1IjoicXVldHRvIiwiYSI6ImNrNDFqa3pxazAxczIzZWtreTVjNDBuZ2cifQ.VHuHd6J5QU_99i-maIYhzg")

#Template responisble for connecting to the data base and storing the newset records from the table
@app.route("/json")
def todo():
    # Connecting to local postgres database and table inside it
    connection = psycopg2.connect(user="postgres",
                        password="7319",
                        host="127.0.0.1",
                        port="5432",
                        database="postgres")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from zadanie where id=(select max(id) from zadanie)"
    # Pulling the newste record from the table 
    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchall()
    for row in mobile_records:
        ID = row[0]
        x = row[1]
        y = row[2]
    # json which stroes and returnes the newset records from the table
    records = {'ID': ID, 'X': str(x), 'Y': str(y)}
    return records

# line responsible for turing on the server
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
   


        