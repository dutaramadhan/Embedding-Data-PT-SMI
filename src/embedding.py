import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv('API_KEY'))

def get_embedding(text):
   response = client.embeddings.create(
    text,
    model="text-embedding-ada-002"
    )
   return response

