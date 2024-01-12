import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_params = {
    'host': os.getenv('DB_HOST'),
    'database':  os.getenv('DB_DATABASE'),
    'user':  os.getenv('DB_USER'),
    'password':  os.getenv('DB_PASSWORD'),
    'port':  os.getenv('DB_PORT'),
}

def selectOne():
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()

  # Execute a SELECT query to fetch one row
  query = "SELECT content, id FROM data WHERE source_id=35 AND embedding is NULL LIMIT 1"
  cursor.execute(query)

  # Fetch the first row from the result set
  [content, id] = cursor.fetchone()

  cursor.close()
  conn.close()
  return [content, id]

def storeEmbedding(id, embedding):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()
  update_query = "UPDATE data SET embedding = %s WHERE id = %s;"

  # Execute the update query
  cursor.execute(update_query, (embedding, id))

  # Commit the changes
  conn.commit()
  cursor.close()
  conn.close()

