import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama3")
    WORKSPACE_DIR = os.getenv("WORKSPACE_DIR", "workspace")
    MEMORY_DIR = os.getenv("MEMORY_DIR", "memory")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
    
    @classmethod
    def ensure_dirs(cls):
        dirs = [cls.WORKSPACE_DIR, cls.MEMORY_DIR, "tools", "agents", "models"]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

Config.ensure_dirs()
