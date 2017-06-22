#!/usr/bin/python

import json
import urllib2
import sqlite3
import subprocess

db = sqlite3.connect('database.db')
cursor=db.cursor()

response = urllib2.urlopen('http://api.fixer.io/latest?base=USD')
data = response.read()
rdata = json.loads(data, parse_float=float)
temp = rdata['rates']

temp2=rdata['date']
print temp2
print temp['IDR'],temp['EUR'],temp['JPY']


cursor.execute('''INSERT INTO currency(dates,idr, jpy, eur)
   VALUES(?,?,?,?)''', (temp2,float(temp['IDR']), float(temp['JPY']), float(temp['EUR'])))

db.commit()
db.close()


