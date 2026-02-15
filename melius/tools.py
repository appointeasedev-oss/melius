import os
import subprocess
import importlib.util
import sys
from typing import Dict, Any, List, Optional
from playwright.sync_api import sync_playwright

class BaseTool:
    name: str = ""
    description: str = ""
    parameters: Dict[str, str] = {}

    def execute(self, **kwargs) -> str:
        raise NotImplementedError

class ToolRegistry:
    def __init__(self, tools_dir: str = "tools"):
        self.tools_dir = tools_dir
        self.tools: Dict[str, BaseTool] = {}
        os.makedirs(tools_dir, exist_ok=True)
        self._register_builtins()
        self.discover_tools()

    def _register_builtins(self):
        # Built-in tools are registered here
        self.register(ShellTool())
        self.register(BrowserTool())
        self.register(FileTool())
        self.register(GitHubTool())

    def register(self, tool: BaseTool):
        self.tools[tool.name] = tool

    def discover_tools(self):
        """Dynamically load tools from the tools directory."""
        for filename in os.listdir(self.tools_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                path = os.path.join(self.tools_dir, filename)
                self._load_tool_from_path(path)

    def _load_tool_from_path(self, path: str):
        try:
            module_name = os.path.basename(path)[:-3]
            spec = importlib.util.spec_from_file_location(module_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for attr in dir(module):
                cls = getattr(module, attr)
                if isinstance(cls, type) and issubclass(cls, BaseTool) and cls is not BaseTool:
                    self.register(cls())
        except Exception as e:
            print(f"Error loading tool from {path}: {e}")

    def get_definitions(self) -> List[Dict[str, Any]]:
        return [
            {"name": t.name, "description": t.description, "parameters": t.parameters}
            for t in self.tools.values()
        ]

    def has_tool(self, name: str) -> bool:
        return name in self.tools

class ShellTool(BaseTool):
    name = "shell_execute"
    description = "Execute a command in the system shell."
    parameters = {"command": "The shell command to run"}

    def execute(self, command: str) -> str:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return f"Exit Code: {result.returncode}\nOutput: {result.stdout}\nError: {result.stderr}"
        except Exception as e:
            return f"Execution failed: {str(e)}"

class BrowserTool(BaseTool):
    name = "browser_action"
    description = "Perform web research or automation."
    parameters = {"url": "Target URL", "action": "navigate/click/type", "selector": "CSS selector if needed"}

    def execute(self, url: str, action: str = "navigate", **kwargs) -> str:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url)
                if action == "navigate":
                    content = page.title() + "\n" + page.content()[:2000]
                else:
                    content = f"Action {action} performed (simulated)"
                browser.close()
                return content
        except Exception as e:
            return f"Browser error: {str(e)}"

class FileTool(BaseTool):
    name = "file_operation"
    description = "Read, write, or list files in the workspace."
    parameters = {"op": "read/write/list", "path": "File path", "content": "Content for write"}

    def execute(self, op: str, path: str, content: Optional[str] = None) -> str:
        full_path = os.path.join("workspace", path)
        try:
            if op == "write":
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as f:
                    f.write(content or "")
                return f"Successfully wrote to {path}"
            elif op == "read":
                with open(full_path, 'r') as f:
                    return f.read()
            elif op == "list":
                return "\n".join(os.listdir("workspace"))
            return "Invalid operation"
        except Exception as e:
            return f"File error: {str(e)}"

class GitHubTool(BaseTool):
    name = "github_manage"
    description = "Interact with GitHub using gh CLI."
    parameters = {"command": "The gh command to run (e.g. 'repo view')"}

    def execute(self, command: str) -> str:
        try:
            result = subprocess.run(f"gh {command}", shell=True, capture_output=True, text=True)
            return result.stdout or result.stderr
        except Exception as e:
            return f"GitHub error: {str(e)}"
