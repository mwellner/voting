import psycopg2

def get_counts():
  counts = [0, 0, 0]
  try:
    connection = psycopg2.connect("dbname=voting user=www host=db")
    counts = get_counts_internal(connection)
  except psycopg2.Error as e:
    print e
  finally:
    connection.close()
  return counts

def get_counts_internal(connection):
  try:
    cursor = connection.cursor()
    cursor.execute("SELECT vote, COUNT(*) AS count FROM votes GROUP BY vote ORDER BY vote")
    rows = cursor.fetchall()
    return [rows[0][1], rows[1][1], rows[2][1]]
  except psycopg2.Error as e:
    print e
  finally:
    cursor.close()

  
