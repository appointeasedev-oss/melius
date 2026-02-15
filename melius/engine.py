from .ollama_manager import OllamaManager
import json

class AgentEngine:
    def __init__(self, model="llama3"):
        self.ollama = OllamaManager()
        self.model = model
        self.system_prompt = """You are Melius, a powerful headless AI agent.
You work locally using Ollama. You can read, edit, and modify files in the /workspace folder.
You have access to tools and can even create new ones to improve yourself.
Your goal is to help the user with tasks efficiently and autonomously."""
        self.history = [{"role": "system", "content": self.system_prompt}]

    def process_query(self, query):
        self.history.append({"role": "user", "content": query})
        
        # Simple loop for now: Thinking -> Acting (not implemented yet) -> Response
        response = self.ollama.chat(self.model, self.history)
        
        self.history.append({"role": "assistant", "content": response})
        return response
