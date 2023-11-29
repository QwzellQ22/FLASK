from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route("/")
def hello_world():
    cursor = mysql.connection.cursor()
    NIK = "62823"   
    cursor.execute("select * from users where NIK=%s",(NIK,))
    data = cursor.fetchall()
    return render_template("test.html",data=data)


# if __name__ == '__main__':
#     app.run();