from pathlib import Path

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from core.llm import get_model
from handlers.base import Handler, Response

_system = (Path(__file__).parent.parent / "prompts" / "explain.txt").read_text()


class ExplainHandler(Handler):
    
    def __init__(self):
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", _system),
            MessagesPlaceholder("history"),
            ("human", "{query}"),
        ])
        self.chain = prompt | get_model() | StrOutputParser()

    def handle(self, query: str, history: list) -> Response:
        
        text = self.chain.invoke({"query": query, "history": history})
        return Response(text=text, intent="explain")


    def stream(self, query: str, history: list):
        yield from self.chain.stream({"query": query, "history": history})