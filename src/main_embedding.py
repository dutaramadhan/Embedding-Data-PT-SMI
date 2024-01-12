import embedding
import load
import time

while True:
    [content, id] = load.selectOne()
    response_embedding = embedding.get_embedding(content)
    embedding = response_embedding.data[0].embedding
    token = response_embedding.usage.total_tokens
    print(id, embedding)
    load.storeEmbedding(id, embedding)
    time.sleep(20)