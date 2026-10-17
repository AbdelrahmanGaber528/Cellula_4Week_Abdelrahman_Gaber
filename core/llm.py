from langchain_openai import ChatOpenAI
from config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL_NAME , TEMPERATURE


def get_model() -> ChatOpenAI:
    
    return ChatOpenAI(model=MODEL_NAME , api_key=OPENROUTER_API_KEY , base_url=OPENROUTER_BASE_URL , temperature=TEMPERATURE)