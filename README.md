# Melius 🌟 - The Headless, Self-Improving AI Agent

Melius is a production-ready, local-first AI agent CLI. It's designed to be a "headless" version of OpenClaw, running entirely on your local hardware using **Ollama**.

## 🚀 Key Features

- 🤖 **Multi-Agent Orchestration**: Main agent can spawn sub-agents for specialized tasks.
- 🛠️ **Dynamic Tool Creation**: Melius can write and register its own tools at runtime.
- 🐙 **GitHub Integration**: Full control over your repos using the GitHub CLI.
- 🌐 **Deep Research**: Built-in browser automation for internet-scale information gathering.
- 📅 **Smart Scheduling**: Automate tasks (e.g., "Review this PR at 9 AM tomorrow").
- 🧠 **Dual Memory**: Short-term context and long-term persistent storage.
- 🔒 **100% Local**: Your data never leaves your machine.

## 🛠️ Installation

1. **Prerequisites**:
   - [Ollama](https://ollama.com) installed and running.
   - [GitHub CLI](https://cli.github.com/) (optional, for GitHub tools).
   - Python 3.10+.

2. **Setup**:
   ```bash
   git clone https://github.com/appointeasedev-oss/melius.git
   cd melius
   ./setup.bat  # On Windows
   ```

## 📖 Usage

### Launch Melius
```bash
melius start
```

### Self-Improvement
You can tell Melius:
> "Create a tool that summarizes PDF files in the workspace and use it to analyze report.pdf"

### Multi-Agent Tasks
> "Create a sub-agent to handle the documentation while you focus on the code implementation."

## 📂 Project Structure

- `/melius/`: Core logic and agent engines.
- `/tools/`: Default and dynamically created tools.
- `/workspace/`: Agent's primary working directory.
- `/agents/`: Sub-agent definitions and states.
- `/memory/`: Persistent storage for agent knowledge.

## 📜 License
MIT
