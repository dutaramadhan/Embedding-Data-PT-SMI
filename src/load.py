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
  query = "SELECT content, source_title, source_name, data.id FROM data INNER JOIN source_metadata ON data.source_id = source_metadata.id WHERE header_embedding is NULL LIMIT 1"
  cursor.execute(query)

  # Fetch the first row from the result set
  [content, source_title, source_name, id] = cursor.fetchone()
  content = source_title + '\n' + content
  

  cursor.close()
  conn.close()
  return [content, id, source_title, source_name]

def storeEmbedding(id, embedding):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()
  update_query = "UPDATE data SET header_embedding = %s WHERE id = %s;"

  # Execute the update query
  cursor.execute(update_query, (embedding, id))

  # Commit the changes
  conn.commit()
  cursor.close()
  conn.close()

