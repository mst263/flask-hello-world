import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def test_db():
    conn = psycopg2.connect("postgres://mstdata_user:dmHp2k2RlRARbjkj5pFR3BMpjzd0KltZ@dpg-cgm4v1o7oslael757erg-a/mstdata")
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://mstdata_user:dmHp2k2RlRARbjkj5pFR3BMpjzd0KltZ@dpg-cgm4v1o7oslael757erg-a/mstdata")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://mstdata_user:dmHp2k2RlRARbjkj5pFR3BMpjzd0KltZ@dpg-cgm4v1o7oslael757erg-a/mstdata")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston','Celtics',0),
        ('Stephen', 'Curry', 'San Francisco','Warriors',30),
        ('Nikola', 'Jokic', 'Denver','Nuggets',15),
        ('Kawhi', 'Leonard', 'Los Angeles','Clippers',2);
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Populated'

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://mstdata_user:dmHp2k2RlRARbjkj5pFR3BMpjzd0KltZ@dpg-cgm4v1o7oslael757erg-a/mstdata")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://mstdata_user:dmHp2k2RlRARbjkj5pFR3BMpjzd0KltZ@dpg-cgm4v1o7oslael757erg-a/mstdata")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Dropped'