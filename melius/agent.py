import json
from typing import List, Dict, Any, Optional
from .ollama_manager import OllamaManager
from .tools import ToolRegistry

class Agent:
    def __init__(self, name: str, role: str, model: str = "llama3", parent=None):
        self.name = name
        self.role = role
        self.model = model
        self.parent = parent
        self.ollama = OllamaManager()
        self.tools = ToolRegistry()
        self.memory = []
        self.sub_agents: Dict[str, 'Agent'] = {}
        
        self.system_prompt = f"""You are {self.name}, an AI agent with the role: {self.role}.
You are part of the Melius system, a headless local AI agent.
You can use tools, coordinate with sub-agents, and perform tasks in the /workspace folder.
Always respond in JSON format when calling tools or creating sub-agents.
"""
        self.memory.append({"role": "system", "content": self.system_prompt})

    def create_sub_agent(self, name: str, role: str):
        """Create a new sub-agent to handle specific tasks."""
        agent = Agent(name=name, role=role, model=self.model, parent=self)
        self.sub_agents[name] = agent
        return f"Sub-agent {name} created with role: {role}"

    def run(self, task: str) -> str:
        """Main loop for the agent to process a task."""
        self.memory.append({"role": "user", "content": task})
        
        # In a real production system, this would be a loop of Think -> Act -> Observe
        # For now, we simulate the LLM call and tool execution
        response = self.ollama.chat(self.model, self.memory)
        self.memory.append({"role": "assistant", "content": response})
        
        # Logic to parse tool calls or sub-agent creation from response would go here
        return response

class MainAgent(Agent):
    def __init__(self, model: str = "llama3"):
        super().__init__(name="Melius-Main", role="Orchestrator", model=model)
        self.system_prompt += "\nYou are the primary interface for the user. You can delegate complex tasks to sub-agents."
