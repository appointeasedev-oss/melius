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
        
        self.system_prompt = f"""You are {self.name}, an autonomous AI agent within the Melius system.
Your Role: {self.role}

OPERATIONAL GUIDELINES:
1. THINK before acting. Plan your steps in a 'Thought' block.
2. USE TOOLS whenever possible to interact with the world.
3. SELF-IMPROVE: If a task requires a tool you don't have, check the /tools folder. If missing, propose creating a new tool.
4. MULTI-AGENT: You can delegate complex sub-tasks to specialized sub-agents.
5. MEMORY: You have access to short-term context and long-term facts. Use them to maintain consistency.

AVAILABLE TOOLS:
{json.dumps(self.tools.get_definitions(), indent=2)}

RESPONSE FORMAT:
Always structure your response as:
Thought: [Your reasoning]
Action: [tool_use | create_agent | create_tool | final_answer]
Parameters: [JSON parameters for the action]
"""

    def think(self, user_input: str) -> str:
        self.memory.add_interaction("user", user_input)
        context = self.memory.get_context()
        context.insert(0, {"role": "system", "content": self.system_prompt})
        
        response = self.ollama.chat(self.model, context)
        self.memory.add_interaction("assistant", response)
        return response

class Orchestrator:
    def __init__(self, model: str = "llama3"):
        self.main_agent = Agent("Melius-Prime", "Orchestrator", model)
        self.sub_agents: Dict[str, Agent] = {}

    def handle_task(self, task: str) -> str:
        return self.main_agent.think(task)
