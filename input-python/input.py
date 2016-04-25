from flask import Flask
from flask import request
from flask import render_template
import random
import redis
import json

redisClient = redis.StrictRedis(host='redis', port=6379, db=0)

app = Flask(__name__)

@app.route("/input", methods=['GET', 'POST'])
def input():
  if request.method == 'GET':
    return render_template('input.html')
  else:
    voter_id = hex(random.getrandbits(64))[2:-1]
    data = json.dumps({'voter_id': voter_id, 'vote': request.form['vote']})
    redisClient.rpush('votes', data) 
    return render_template('confirm.html')

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
