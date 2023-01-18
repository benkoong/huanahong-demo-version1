from flask_bootstrap import Bootstrap
from flask import Flask,render_template
import json
import pymysql

app = Flask(__name__)
#Connection กับ Database 
#conn=pymysql.connect(host='localhost',port=8889,user='root',password='root',database='huanahongdemo')

bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    # ดึงข้อมูลจาก Database
    #with conn:
        #cur=conn.cursor()
        #cur.execute("select * from student")
        #rows = cur.fetchall()
    return render_template('index.html',data='5')

@app.route("/student")
def show():
    return render_template("testbootstrap.html")

if __name__ == "__main__":
    app.run(debug = True)