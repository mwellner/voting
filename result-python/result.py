from flask import Flask
from flask import request
from flask import render_template

from db import get_counts

app = Flask(__name__)

@app.route("/result")
def input():
  counts = get_counts()
  return render_template('result.html', counts=counts)

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.debug = True
  app.run(host="0.0.0.0")
