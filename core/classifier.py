from .llm import get_model
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


VALID_INTENTS = ("explain", "generate")

prompt = (Path(__file__).parent.parent / "prompts" / "classifier.txt").read_text()
chain = ChatPromptTemplate.from_template(prompt) | get_model() | StrOutputParser()


# this is because if model respond with word other "explain" or "generate" , who know
def heuristic(user_query):
    
    q = user_query.lower()
    
    if any(w in q for w in ("explain", "what does", "why does", "how does", "how")):
        
        return "explain"
    
    return "generate"




def classify(user_query):
    
    try:
        out = chain.invoke({"user_query": user_query}).strip().lower()
    
        for intent in VALID_INTENTS:
            if intent in out:
                return intent
    
    except Exception:
        pass
    
    return heuristic(user_query)