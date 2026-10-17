from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Response:
    text: str
    intent: str
    metadata: dict = field(default_factory=dict)


class Handler(ABC):
    @abstractmethod
    def handle(self, query: str, history: list) -> Response:
        """Process a query and return a Response."""