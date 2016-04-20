from flask import Flask
from flask import request
from flask import render_template

import redis
redisClient = redis.StrictRedis(host='redis', port=6379, db=0)

app = Flask(__name__)

@app.route("/input", methods=['GET', 'POST'])
def input():
  if request.method == 'GET':
    return render_template('input.html')
  else:
    redisClient.rpush('votes', request.form['vote'])    
    return render_template('confirm.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
