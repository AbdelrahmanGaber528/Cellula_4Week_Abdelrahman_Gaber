from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from config import MAX_HISTORY_TURNS


class Memory:
    
    def __init__(self, max_turns: int = MAX_HISTORY_TURNS):
        self.messages: list[BaseMessage] = []
        self.max_turns = max_turns

    def add_user(self, text: str):
        self.messages.append(HumanMessage(content=text))

    def add_ai(self, text: str):
        self.messages.append(AIMessage(content=text))

    def get_history(self) -> list[BaseMessage]:
        return self.messages[-self.max_turns * 2:]

    def clear(self):
        self.messages = []