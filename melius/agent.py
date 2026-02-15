import json
from typing import List, Dict, Any, Optional
from .ollama_manager import OllamaManager
from .tools import ToolRegistry, BaseTool
from .memory import Memory

class Agent:
    def __init__(self, name: str, role: str, model: str = "llama3"):
        self.name = name
        self.role = role
        self.model = model
        self.ollama = OllamaManager()
        self.tools = ToolRegistry()
        self.memory = Memory(name)
        
        self.system_prompt = f"""You are {self.name}, an advanced AI agent.
Role: {self.role}
System: Melius (Headless, Local, Self-Improving)

Capabilities:
1. Use existing tools (listed below).
2. Propose new tools if a capability is missing.
3. Spawn sub-agents for specialized tasks.
4. Maintain long-term and short-term memory.

Available Tools:
{json.dumps(self.tools.get_definitions(), indent=2)}

Guidelines:
- Before creating a tool, CHECK if one already exists.
- If you need a sub-agent, define its name and specific role.
- Respond with a 'thought' and an 'action' (tool_use, create_agent, or create_tool).
"""

    def think(self, user_input: str) -> Dict[str, Any]:
        self.memory.add_interaction("user", user_input)
        context = self.memory.get_context()
        context.insert(0, {"role": "system", "content": self.system_prompt})
        
        raw_response = self.ollama.chat(self.model, context)
        self.memory.add_interaction("assistant", raw_response)
        
        # In a production system, we'd use structured output (JSON mode)
        # Here we simulate parsing the response
        return {"response": raw_response}

class Orchestrator:
    def __init__(self, model: str = "llama3"):
        self.main_agent = Agent("Melius-Prime", "Orchestrator", model)
        self.sub_agents: Dict[str, Agent] = {}

    def handle_task(self, task: str):
        # Initial thought process
        result = self.main_agent.think(task)
        return result["response"]

    def create_sub_agent(self, name: str, role: str, model: Optional[str] = None):
        if name in self.sub_agents:
            return f"Agent {name} already exists."
        new_agent = Agent(name, role, model or self.main_agent.model)
        self.sub_agents[name] = new_agent
        return f"Sub-agent {name} initialized as {role}."
