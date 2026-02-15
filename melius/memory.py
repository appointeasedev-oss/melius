import json
import os

class MemoryManager:
    def __init__(self, storage_path="memory/storage.json"):
        self.storage_path = storage_path
        self.memory = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                return json.load(f)
        return {"short_term": [], "long_term": {}}

    def save_memory(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, "w") as f:
            json.dump(self.memory, f, indent=4)

    def add_to_short_term(self, interaction):
        self.memory["short_term"].append(interaction)
        if len(self.memory["short_term"]) > 50:
            self.memory["short_term"].pop(0)
        self.save_memory()

    def store_fact(self, key, value):
        self.memory["long_term"][key] = value
        self.save_memory()

    def get_fact(self, key):
        return self.memory["long_term"].get(key)
