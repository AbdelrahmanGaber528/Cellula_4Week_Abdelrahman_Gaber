from handlers.base import Handler, Response


class GenerateHandler(Handler):
    def handle(self, query: str, history: list) -> Response:
        return Response(text="Code generation is coming soon.", intent="generate")