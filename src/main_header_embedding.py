import embedding
import load
import time
import re

def getHeader(source_name, source_title, content):
  try :
    [penjelasan, pasal] = re.split(r'(Pasal \d+)', content)[0:2]
    name = re.split('\.', source_name)[0]
    title = re.split(r'TENTANG', source_title)[0]

    header = name + ' ' + title + ' '

    if re.findall(r'penjelasan', penjelasan, re.IGNORECASE):
      header += penjelasan + ' '

    header += pasal
    return header

  except Exception as e:
    return None

while True:
    [content, id, source_title, source_name] = load.selectOne()
    header = getHeader(source_name, source_title, content)
    header_embedding = embedding.get_embedding(header)
    header_embedding_vector = header_embedding.data[0].embedding
    token = header_embedding.usage.total_tokens
    print(id, token)
    load.storeEmbedding(int(id), header_embedding_vector)
    if True:
        print('success input data')
    time.sleep(60/500)