import time
import redis
redisClient = redis.StrictRedis(host='redis', port=6379, db=0)

import psycopg2

longTime = 1
shortTime = 0.001
sleepTime = longTime

while 1:
  time.sleep(sleepTime)
  count = redisClient.llen('votes')
  if count == 0:
    sleepTime = longTime
  else:
    sleepTime = shortTime
    item = redisClient.lpop('votes')
    connection = psycopg2.connect("dbname=voting user=www host=db port=5432")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO votes (vote) VALUES (%s)", (item))
    connection.commit()
    cursor.close()
    connection.close()
