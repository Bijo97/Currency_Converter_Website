#!/usr/bin/python
import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()
#cursor.execute('''
#    CREATE TABLE users(id INTEGER PRIMARY KEY,
#	username text unique, password text, email text unique)
#''')
cursor.execute('''
    CREATE TABLE currency (id INTEGER PRIMARY KEY,
	dates date, idr float, jpy float,eur float)
''')
print "Table created successfully"; 
db.commit()

