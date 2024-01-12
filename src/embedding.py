import os
from openai import OpenAI
from scipy.spatial import distance
import plotly.express as px
from sklearn.cluster import KMeans
from umap import UMAP
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv('API_KEY'))

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding


print(get_embedding("Test Doang"))

