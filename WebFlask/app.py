from flask import Flask, flash, redirect,render_template,request,session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key='super secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route("/simpan_register", methods = ['POST', 'GET'])
def simpan_register():
    NIK = request.form['NIK']
    nama = request.form['nama']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO users(NIK,nama) VALUES(%s,%s)''',(NIK,nama))
    mysql.connection.commit()
    cursor.close()
    return f"Done!!"

@app.route("/simpan_catatan", methods = ['POST', 'GET'])
def simpan_catatan():
    tanggal = request.form['tanggal']
    waktu = request.form['waktu']
    lokasi = request.form['lokasi']
    suhu = request.form['suhu']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO catatan(tanggal,waktu,lokasi,suhu) VALUES(%s,%s,%s,%s)''',(tanggal,waktu,lokasi,suhu))
    mysql.connection.commit()
    cursor.close()
    return render_template("isi.html",name="WzMyThx" )
   

@app.route("/register")
def register():
    return render_template("regis.html",name="WzMyThx")

@app.route("/")
def Login():
     if session.get('NIK'):
        return "done bang"
     else:
      if request.method == 'POST':
        NIK = request.form['NIK']
        nama = request.form['nama']
        cursor = mysql.connection.cursor()
        cursor.execute("select * from users WHERE NIK=%s and nama=%s",(NIK,nama))
        data=cursor.fetchone()
        if data:
            session['NIK'] = data[0]
            session['nama'] = data[1]
            return redirect('/beranda')
        else:
            flash("LOGIN LU GAGAL KOCAK")
            return redirect('/')
      return render_template('login.html',name="WzMyThx")

    

@app.route("/beranda")
def Beranda():
    if 'NIK' in session and 'nama' in session:  
         NIK = session['NIK']
         nama = session['nama']
         return render_template('beranda.html',nama=nama)  
    else:
         return render_template('login.html')
    # return render_template("beranda.html",name="WzMyThx")

@app.route("/catatan")
def Catatan():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from catatan")
    mysql.connection.commit()
    data = cursor.fetchall()
    return render_template("catatan.html",name="WzMyThx",data=data )

@app.route("/isi")
def Isi():
    return render_template("isi.html", name="WzMyThx")


# from flask import Flask, render_template,request, session, redirect
# from flask_mysqldb import MySQL

# app = Flask(__name__)
# app.secret_key = 'super secret key'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'

# mysql = MySQL(app)

# @app.route("/simpan_register", methods = ['POST', 'GET'])
# def simpan_register():
#     nama = request.form['nama']
#     NIK = request.form['NIK']   
#     cursor = mysql.connection.cursor()
#     cursor.execute(''' INSERT INTO users(NIK,nama) VALUES(%s,%s)''',(NIK,nama,))
#     mysql.connection.commit()
#     cursor.close()
#     return render_template('login.html') 

# @app.route("/simpan_catatan", methods = ['POST', 'GET'])
# def catatan():
#     if request.method == 'POST' :
#         tanggal = request.form['tanggal']   
#         waktu = request.form['waktu']   
#         lokasi = request.form['lokasi']   
#         suhu = request.form['suhu']   
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO catatan(tanggal,waktu,lokasi,suhu) VALUES(%s,%s,%s,%s)''',(tanggal,waktu,lokasi,suhu))
#         mysql.connection.commit()
#         cursor.close()
#     return render_template('catatan.html') 

# @app.route("/register")
# def regis():
#     return render_template("regis.html")

# @app.route("/", methods = ['POST', 'GET'])
# def index():
#     if request.method == 'POST' :
#         nama = request.form['nama']
#         NIK = request.form['NIK']   
#         cursor = mysql.connection.cursor()
#         cursor.execute("select * from users where NIK=%s AND nama=%s",(NIK,nama))
#         data = cursor.fetchone()
#         mysql.connection.commit()
#         cursor.close()
#         if data :
#             session['NIK'] = NIK
#             session['nama'] = nama
#             return redirect('/beranda')
#         else :
#             return render_template('/')
#     return render_template('login.html')

# @app.route("/beranda")
# def beranda():
#     if 'NIK' in session and 'nama' in session:  
#         NIK = session['NIK']  
#         nama = session['nama']
#         return render_template('beranda.html',nama=nama)  
#     else:
#         return render_template('login.html')

# @app.route("/catatan", methods = ['POST', 'GET'])
# def Catatan():
#    cursor = mysql.connection.cursor()
#    cursor.execute("select * from catatan")
#    data = cursor.fetchall()
#    return render_template('catatan.html', data=data)

# @app.route("/isi", methods = ['POST', 'GET'])
# def isi():
#    return render_template("isi.html")

if __name__ == '__main__':

    app.run()

