import requests
import json
from tqdm import tqdm

uri = "10.20.12.170"
indice = "andina_apa_translations_20231107_fer"
url = f"http://{uri}:9200/{indice}/_search"

headers = {'Content-Type': 'application/json'}

query = {
    "_source" : "appkey",
    "size" : 9999999,
    "query": {
        "match_all": {}
    }
}

response = (requests.get(url, json=query, headers=headers))
json_response = json.loads(response.content)['hits']['hits']

appkey_set = set()
for hit in json_response:
    appkey = hit['_source']['appkey']
    appkey_set.add(appkey)
    appkey_str = ','.join(appkey_set)    
appkey_str = appkey_str.lstrip(',')

with open('todas las keys.txt', 'w') as file:
    file.write(appkey_str)
