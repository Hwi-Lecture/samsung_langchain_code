import requests
import json
import os
import uuid
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

rag_credential_key=os.getenv("rag_credential_key") # DS API Hub에서 발급받은 키
rag_api_key=os.getenv("rag_api_key") # Ragaas Portal에서 발급받은 키

url = "http://apigw.samsungds.net:8000/ds_llm_rag/2/dsllmrag/elastic/v2/retrieve-rrf"

headers = {
    "Content-Type":  'application/json',
    "x-dep-ticket": rag_credential_key,  # DS API HUB key
    "api-key": rag_api_key,  # RAG Portal key
}

fields = {
    "index_name": "rp-261008-test123", # 내 인덱스 이름
    "permission_groups" :['rag-public'],
    "query_text" : '삼성전자 1분기 경영실적은?',
    "num_result_doc":5,
    "fields_exclude": [ "v_merge_title_content"],
}

json_data = json.dumps(fields)

response = requests.request("POST", url, data=json_data, headers=headers)
result = response.json()
print(result['hits'])
