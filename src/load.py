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
  query = "SELECT content, source_title, data.id FROM data INNER JOIN source_metadata ON data.source_id = source_metadata.id WHERE embedding is NULL LIMIT 1"
  cursor.execute(query)

  # Fetch the first row from the result set
  [content, source_title, id] = cursor.fetchone()
  content = source_title + '\n' + content

  cursor.close()
  conn.close()
  return [content , id]

def storeEmbedding(id, embedding, total_tokens):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()
  update_query = "UPDATE data SET embedding = %s, total_tokens = %s WHERE id = %s;"

  # Execute the update query
  cursor.execute(update_query, (embedding, total_tokens, id))

  # Commit the changes
  conn.commit()
  cursor.close()
  conn.close()

