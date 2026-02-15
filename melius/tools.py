import os
import shutil
import subprocess
import importlib
import sys
from playwright.sync_api import sync_playwright

class Tool:
    name = ""
    description = ""
    def execute(self, **kwargs):
        pass

class GitHubTool(Tool):
    name = "github_operation"
    description = "Perform GitHub operations using 'gh' CLI. Params: command (e.g., 'repo view', 'issue list')"
    def execute(self, command):
        try:
            result = subprocess.run(f"gh {command}", shell=True, capture_output=True, text=True)
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        except Exception as e:
            return f"Error: {str(e)}"

class BrowserSearchTool(Tool):
    name = "browser_search"
    description = "Search and extract info from a URL. Params: url"
    def execute(self, url):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url, timeout=60000)
                content = page.content()
                browser.close()
                return content[:5000] # Increased context limit
        except Exception as e:
            return f"Error: {str(e)}"

class ToolCreatorTool(Tool):
    name = "create_tool"
    description = "Dynamically create a new tool. Params: tool_name, code"
    def execute(self, tool_name, code):
        try:
            tool_path = f"tools/{tool_name}.py"
            os.makedirs("tools", exist_ok=True)
            with open(tool_path, "w") as f:
                f.write(code)
            return f"Successfully created tool {tool_name} at {tool_path}"
        except Exception as e:
            return f"Error: {str(e)}"

class ToolRegistry:
    def __init__(self):
        self.tools = {
            "github": GitHubTool(),
            "browser": BrowserSearchTool(),
            "create_tool": ToolCreatorTool()
        }
        self._load_dynamic_tools()

    def _load_dynamic_tools(self):
        if not os.path.exists("tools"):
            return
        for filename in os.listdir("tools"):
            if filename.endswith(".py"):
                tool_name = filename[:-3]
                # Dynamic loading logic would go here in a full implementation
                pass

    def get_tool_definitions(self):
        return [
            {"name": t.name, "description": t.description}
            for t in self.tools.values()
        ]

    def call_tool(self, name, **kwargs):
        if name in self.tools:
            return self.tools[name].execute(**kwargs)
        return f"Error: Tool {name} not found."
