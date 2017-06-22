from flask import Flask, render_template, request, redirect, Markup, url_for, session
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = "biljo"

@app.route('/')
def index():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("SELECT * FROM currency WHERE id = (SELECT MAX(id) FROM currency)")
   
   rows = cur.fetchall();
   values = []

   for row in rows:
      values.append(row['idr'])
      values.append(row['jpy'])
      values.append(row['eur'])

   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("SELECT * FROM currency ORDER BY id DESC LIMIT 5")
   
   tgl = cur.fetchall();
   return render_template('index.html', rates=values, hari=tgl)

@app.route('/convert', methods=['POST', 'GET'])
def convert():
   if request.method == 'POST':
      try:
         uang1 = request.form['uang1']
         uang2 = request.form['uang2']
         jumlah = float(request.form['jumlah'])

         with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM currency WHERE id = (SELECT MAX(id) FROM currency)")

            rows = cur.fetchall();
      			#return render_template("list.html",rows = rows)  
            msg = "Data successfully fetched"

            for row in rows:
	            if uang1 == "IDR" and uang2 == "IDR":
	              hasil = jumlah
	            elif uang1 == "IDR" and uang2 == "JPY":
	              hasil = jumlah / row['idr'] * row['jpy']
	            elif uang1 == "IDR" and uang2 == "EUR":
	              hasil = jumlah / row['idr'] * row['eur']
	            elif uang1 == "JPY" and uang2 == "IDR":
	              hasil = jumlah / row['jpy'] * row['idr']
	            elif uang1 == "JPY" and uang2 == "JPY":
	              hasil = jumlah
	            elif uang1 == "JPY" and uang2 == "EUR":
	              hasil = jumlah / row['jpy'] * row['eur']
	            elif uang1 == "EUR" and uang2 == "IDR":
	              hasil = jumlah / row['eur'] * row['idr']
	            elif uang1 == "EUR" and uang2 == "JPY":
	              hasil = jumlah / row['eur'] * row['jpy']
	            elif uang1 == "EUR" and uang2 == "EUR":
	              hasil = jumlah
	            else:
	              hasil = 0

      except:
         con.rollback()
         msg = "error in fetch operation"
      
      finally:
         con.close()
         session['hasil'] = hasil
         return redirect(url_for('index'))

if __name__ == '__main__':
   app.run('0.0.0.0', port=5058, debug=True)
