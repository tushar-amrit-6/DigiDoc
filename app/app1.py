#import os
import random
#import secrets
#from app import app
#from xray import xray_predict
from flask import Flask , render_template, url_for, flash, redirect, request, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['SECRET_KEY'] = 'TeamBeta30'
app.config['MYSQL_HOST'] =  'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12373814'
app.config['MYSQL_PASSWORD'] = 'iAWCUSSvB1'
app.config['MYSQL_DB'] = 'sql12373814'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def def_index():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE USERS (name VARCHAR(30) , email VARCHAR(100), password VARCHAR(100), familyid INTEGER, mobile VARCHAR(20),age INTEGER,height INTEGER,weight INTEGER, blood_grp VARCHAR(20) , PRIMARY KEY (email) )''')
    #cur.execute('''CREATE TABLE DETAILS (name VARCHAR(30), email VARCHAR(100) , xraystatus VARCHAR(100), pulserate INTEGER , familyid INTEGER, mobile VARCHAR(20),age INTEGER,height INTEGER,weight INTEGER, blood_grp VARCHAR(20) ,status VARCHAR(100),disease VARCHAR(30), PRIMARY KEY (email), FOREIGN KEY (email) REFERENCES USERS(email) )''')
    #cur.execute('''DROP TABLE USERS''')
    #cur.execute('''INSERT INTO USERS VALUES ('shubham','shubham@gmail.com','qwerty', 11,'1234567890' ,21, 61,171,'B+')''')
    #cur.execute('''INSERT INTO DETAILS VALUES ('shubham@gmail.com' ,'normal',90, 11,'1234567890' ,21, 61,171,'B+','healthy','no disease')''')
    #mysql.connection.commit()
    #cur.execute('''SELECT * from USERS''')
    #results = cur.fetchall()
    #print(results)
    #cur.execute('''SELECT * from DETAILS''')
    #results = cur.fetchall()
    #print(results)
    return "Done"
