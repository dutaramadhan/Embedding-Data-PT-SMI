import embedding
import load
import time

while True:
    [content, id] = load.selectOne()
    response_embedding = embedding.get_embedding(content)
    embedding_vector = response_embedding.data[0].embedding
    token = response_embedding.usage.total_tokens
    print(id, token)
    load.storeEmbedding(int(id), embedding_vector, int(token))
    if True:
        print('success input data')
    time.sleep(60/500)