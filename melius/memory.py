import json
import os
from datetime import datetime
from typing import List, Dict, Any

class Memory:
    def __init__(self, agent_name: str, base_dir: str = "memory"):
        self.agent_name = agent_name
        self.base_dir = base_dir
        self.short_term_limit = 20
        self.storage_file = os.path.join(base_dir, f"{agent_name}_memory.json")
        self._ensure_storage()
        self.data = self._load()

    def _ensure_storage(self):
        os.makedirs(self.base_dir, exist_ok=True)
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({"short_term": [], "long_term": {}, "history": []}, f)

    def _load(self) -> Dict[str, Any]:
        with open(self.storage_file, 'r') as f:
            return json.load(f)

    def save(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_interaction(self, role: str, content: str):
        entry = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.data["short_term"].append(entry)
        self.data["history"].append(entry)
        
        # Maintain sliding window for short-term memory
        if len(self.data["short_term"]) > self.short_term_limit:
            self.data["short_term"].pop(0)
        self.save()

    def store_fact(self, key: str, value: Any):
        self.data["long_term"][key] = value
        self.save()

    def get_context(self) -> List[Dict[str, str]]:
        """Returns the formatted context for the LLM."""
        context = []
        # Add long-term facts as system-level context if needed
        if self.data["long_term"]:
            facts = json.dumps(self.data["long_term"])
            context.append({"role": "system", "content": f"Relevant long-term knowledge: {facts}"})
        
        for entry in self.data["short_term"]:
            context.append({"role": entry["role"], "content": entry["content"]})
        return context
