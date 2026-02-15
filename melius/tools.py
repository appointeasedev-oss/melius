import os
import shutil
import subprocess
from playwright.sync_api import sync_playwright

class Tool:
    name = ""
    description = ""
    def execute(self, **kwargs):
        pass

class WriteFileTool(Tool):
    name = "write_file"
    description = "Write content to a file in the workspace. Params: path, content"
    def execute(self, path, content):
        workspace_path = os.path.join("workspace", path)
        os.makedirs(os.path.dirname(workspace_path), exist_ok=True)
        with open(workspace_path, "w") as f:
            f.write(content)
        return f"File written to {path}"

class ReadFileTool(Tool):
    name = "read_file"
    description = "Read content from a file in the workspace. Params: path"
    def execute(self, path):
        workspace_path = os.path.join("workspace", path)
        if not os.path.exists(workspace_path):
            return f"Error: File {path} not found."
        with open(workspace_path, "r") as f:
            return f.read()

class ShellCommandTool(Tool):
    name = "shell_command"
    description = "Execute a shell command. Params: command"
    def execute(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        except Exception as e:
            return f"Error executing command: {str(e)}"

class BrowserTool(Tool):
    name = "browser_search"
    description = "Search the web using a browser. Params: url"
    def execute(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            content = page.content()
            browser.close()
            return content[:2000] # Return first 2000 chars for context

class ToolRegistry:
    def __init__(self):
        self.tools = {
            "write_file": WriteFileTool(),
            "read_file": ReadFileTool(),
            "shell_command": ShellCommandTool(),
            "browser_search": BrowserTool()
        }

    def get_tool_definitions(self):
        return [
            {"name": t.name, "description": t.description}
            for t in self.tools.values()
        ]

    def call_tool(self, name, **kwargs):
        if name in self.tools:
            return self.tools[name].execute(**kwargs)
        return f"Error: Tool {name} not found."
