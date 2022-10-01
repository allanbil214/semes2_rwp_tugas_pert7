from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect( 
    host = "localhost",
    user = "root",
    password = "",
    database = "sia_383"
)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/mhs")
def mhs():
    return render_template("apprentices.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/show", methods=["GET"])
def show():
    cur = db.cursor()
    cur.execute("select * from mhs_383")
    getall = cur.fetchall()
    res = jsonify(getall)
    res.status_code = 200
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

if __name__ == "__main__":
    app.run(debug=True)