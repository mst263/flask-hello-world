import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def hello_world():
    conn = psycopg2.connect("postgres://mstdata_user:dmHp2k2RlRARbjkj5pFR3BMpjzd0KltZ@dpg-cgm4v1o7oslael757erg-a/mstdata")
    conn.close()
    return 'Database Connection Successful'