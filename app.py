from flask import Flask, render_template, request, jsonify
import socket
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def fetchAddressDetail():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route('/')
def home():
    hostname,ip = fetchAddressDetail()
    return render_template('index.html', HOSTNAME = hostname, IP = ip, MAXCALORIES=1000,MINCALORIES=300, TOTALALIMENTE=10)

@app.route('/check_api')
def check_api():
    api_url = "https://jsonplaceholder.typicode.com/users"
    return jsonify({'message': 'API is up at this moment'}), 200

@app.route('/liveness')
def liveness():
    hostname,ip = fetchAddressDetail()

    api_url = "https://jsonplaceholder.typicode.com/users"
    responseSTR = "Hello, i'm alive"
    color = "#c8e6c9"
    return render_template('liveness.html', COLOR = color,RESPONSE = responseSTR,HOSTNAME = hostname, IP = ip, MAXCALORIES=1000,MINCALORIES=300, TOTALALIMENTE=10)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
