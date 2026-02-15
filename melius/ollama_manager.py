import requests
import json
import subprocess
import shutil

class OllamaManager:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    def check_ollama(self):
        """Check if Ollama is installed and running."""
        if not shutil.which("ollama"):
            return False, "Ollama not found in PATH."
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            return response.status_code == 200, "Ollama is running."
        except requests.exceptions.ConnectionError:
            return False, "Ollama is installed but not running."

    def list_models(self):
        """List available local models."""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            if response.status_code == 200:
                return [m['name'] for m in response.json().get('models', [])]
            return []
        except:
            return []

    def pull_model(self, model_name):
        """Pull a model from Ollama library."""
        try:
            response = requests.post(
                f"{self.base_url}/api/pull",
                json={"name": model_name, "stream": False}
            )
            return response.status_code == 200
        except:
            return False

    def chat(self, model, messages):
        """Send a chat request to Ollama."""
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": model,
                    "messages": messages,
                    "stream": False
                }
            )
            if response.status_code == 200:
                return response.json().get('message', {}).get('content', '')
            return "Error: Failed to get response from Ollama."
        except Exception as e:
            return f"Error: {str(e)}"
