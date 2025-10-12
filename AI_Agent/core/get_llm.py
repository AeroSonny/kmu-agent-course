import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def get_chat_model(model_name: str = 'gpt-4.1-nano', 
                   max_tokens: int = 4000, 
                   temperature: float = 0.4, 
                   top_p: float = 1.0):
    """
    사용자가 지정한 모델, max_token, temperature, top_p를 작성할 수있는 곳
    Args:
        model_name(str): 사용할 모델 이름, "gpt-4o" 또는 "gpt_4o-mini"가 사용가능하며, default는 gpt-4o-mini로 사용
        max_tokens(int): 생성할 최대 토큰 수
        temparature(float): 모델 생성시 사용되는 temparature.
        top_p (float): nucleus sampling에 사용할 확률 분포 커팅 값 (0~1 사이).
    return:
        ChatOpenAI: 선택된 모델의 인스턴스
    """
    return ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p
    )

CHAT_MODEL = get_chat_model(model_name='gpt-4.1-nano', max_tokens=2000, temperature=0.3)

def model_test(chatmodel):
    response = CHAT_MODEL.invoke('너는 누구니???')
    print(response.content)

if __name__ == "__main__":
    model_test(CHAT_MODEL)