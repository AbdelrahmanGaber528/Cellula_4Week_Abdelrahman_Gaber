from core.classifier import classify
from handlers.base import Handler, Response


class Router:
    def __init__(self, handlers: dict[str, Handler]):
        self.handlers = handlers

    def route(self, query: str, history: list) -> Response:
        intent = classify(query)
        return self.handlers[intent].handle(query, history)