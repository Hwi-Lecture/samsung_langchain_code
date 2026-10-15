from langchain_openai import ChatOpenAI

import os
import uuid
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

credential_key=os.getenv("credential_key") # DS API Hub API key
send_system_name=os.getenv("send_system_name") # 구독 서비스 명
model_name=os.getenv("model") # 신청 모델 이름
api_base_url=os.getenv("api_base_url") # 모델 url (끝에 v1까지만 입력하면 나머진 자동 완성)
user_id=os.getenv("user_id") # 내 AD 계정

os.environ["OPENAI_API_KEY"] = 'api_key'

llm = ChatOpenAI(
    model=model_name,
    base_url=api_base_url,
    default_headers={
        'x-dep-ticket': credential_key,
        'Send-System-Name': send_system_name,
        'User-Id': user_id,
        'User-Type': "AD_ID",
        'Prompt-Msg-Id': str(uuid.uuid4()),
        'Completion-Msg-Id': str(uuid.uuid4())
    },
    temperature=0.7,
)

output = llm.invoke("안녕? 넌 이름이 뭐야?")
print(output.content)
