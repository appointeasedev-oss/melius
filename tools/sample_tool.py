from melius.tools import BaseTool

class EchoTool(BaseTool):
    name = "echo_custom"
    description = "A sample dynamic tool that echoes back the input."
    parameters = {"text": "The text to echo"}

    def execute(self, text: str) -> str:
        return f"Dynamic Echo: {text}"
