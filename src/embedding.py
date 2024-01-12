import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv('API_KEY'))

def get_embedding(text):
   response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-ada-002"
    )
   return response

