from flask import Flask
from flask import request
from flask import render_template

import psycopg2

app = Flask(__name__)

@app.route("/result")
def input():
  conn = psycopg2.connect("dbname=voting user=www host=db")
  cur = conn.cursor()
  cur.execute("SELECT vote, COUNT(*) AS count FROM votes GROUP BY vote ORDER BY vote")
  rows = cur.fetchall()
  counts = [rows[0][1], rows[1][1], rows[2][1]]
  cur.close()
  conn.close()
  return render_template('result.html', counts=counts)

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0")
