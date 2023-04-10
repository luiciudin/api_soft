from flask import Flask, render_template, request, jsonify
import socket
import sqlite3
import os
#import requests
# Inițializăm aplicația Flask
app = Flask(__name__)


#DATABASE
# connection = sqlite3.connect('database.db')
#Verificam daca db/database.db este populata,daca nu, o populam
# if( os.path.isfile('database.db') and os.path.getsize('database.db') == 0 ):
#     with open('schema.sql') as f:
#         connection.executescript(f.read())

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Pentru hostname,ip section
def fetchAddressDetail():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)


# Definim ruta pentru afișarea datelor despre alimente
@app.route('/')
def home():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    #conn = get_db_connection()
    #maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    #minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    #resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    #total_foods = str(resultFoodsCounter[0])
    #maxResult = maxCalories["denumire"]
    #minResult = minCalories["denumire"]

#conn.close()

    return render_template('index.html', HOSTNAME = hostname, IP = ip, MAXCALORIES=1000,MINCALORIES=300, TOTALALIMENTE=10)

@app.route('/check_api')
def check_api():
    api_url = "https://jsonplaceholder.typicode.com/users"
    #response = requests.get(api_url)

    #if response.status_code == 200:
    return jsonify({'message': 'API is up at this moment'}), 200
    #else:
     #   return jsonify({'message': 'API is down'}), 500

@app.route('/liveness')
def liveness():
    #MAIN BARS
    hostname,ip = fetchAddressDetail()

    #conn = get_db_connection()
    #maxCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii DESC LIMIT 1').fetchone()
    #minCalories = conn.execute('SELECT denumire FROM foods ORDER BY calorii ASC LIMIT 1').fetchone()
    #resultFoodsCounter = conn.execute('SELECT COUNT(*) FROM foods').fetchone()
    #total_foods = str(resultFoodsCounter[0])
    #maxResult = maxCalories["denumire"]
    #minResult = minCalories["denumire"]

    #conn.close()

    api_url = "https://jsonplaceholder.typicode.com/users"
    #response = requests.get(api_url)
    #if response.status_code == 200:
    responseSTR = "Hello, i'm alive"
    color = "#c8e6c9"
    #else:
     #   responseSTR = "Hello, i'm down"
      #  color = "red"
    return render_template('liveness.html', COLOR = color,RESPONSE = responseSTR,HOSTNAME = hostname, IP = ip, MAXCALORIES=1000,MINCALORIES=300, TOTALALIMENTE=10)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
