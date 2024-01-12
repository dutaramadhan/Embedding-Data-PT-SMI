import embedding
import load
import time

while True:
    [content, id] = load.selectOne()
    embedding = embedding.getEmbeddings(content)['data'][0]['embedding']
    print(id, embedding)
    load.storeEmbedding(id, embedding)
    time.sleep(20)