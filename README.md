# Melius 🌟

**Melius** is a high-performance, headless, local-first AI agent system designed to run entirely on your machine. Built for power users and developers, it serves as a self-improving "workforce" that operates via command line, leveraging local LLMs through Ollama.

> "Melius is more than just a chatbot; it's an autonomous system that thinks, acts, and evolves locally."

---

## 🚀 Key Capabilities

- **🤖 Multi-Agent Orchestration**: Melius-Prime (the Orchestrator) can spawn specialized sub-agents to handle complex, multi-threaded tasks.
- **🛠️ Dynamic Self-Improvement**: The system can analyze its own limitations, write new Python-based tools, and register them to its `/tools` directory at runtime.
- **🧠 Advanced Dual-Memory**: 
    - **Short-Term**: Maintains context through a sliding-window interaction history.
    - **Long-Term**: Persists critical facts and learned knowledge in structured storage.
- **🐙 GitHub Mastery**: Deep integration with the GitHub CLI (`gh`) for repo management, PR reviews, and automated commits.
- **🌐 Deep Research**: Full browser automation using Playwright for scraping, searching, and navigating the web.
- **📅 Smart Scheduling**: Built-in task scheduler for one-time or recurring autonomous jobs.
- **📱 Remote Control**: Optional Telegram bot integration to interact with your agent from anywhere.

---

## 🛠️ Installation Guide

### 1. Prerequisites
- **Python 3.10+**: [Download here](https://www.python.org/downloads/)
- **Ollama**: Required for local LLM inference. [Download here](https://ollama.com/)
- **GitHub CLI (Optional)**: For GitHub-related tools. [Download here](https://cli.github.com/)

### 2. Setup
Clone the repository and run the automated setup:

```bash
git clone https://github.com/appointeasedev-oss/melius.git
cd melius
```

**On Windows:**
```bash
./setup.bat
```

**On Linux/macOS:**
```bash
pip install -e .
melius setup
```

### 3. Initialize Models
Ensure you have a model downloaded in Ollama:
```bash
melius download llama3
```

---

## 📖 Usage Instructions

### Start Interactive Mode
Launch the main orchestrator:
```bash
melius start
```

### Command Line Operations
Melius comes with a suite of management commands:
- `melius list-tools`: View all currently registered skills and tools.
- `melius list-models`: See which Ollama models are available.
- `melius setup`: Run a full environment and dependency check.

### Example Tasks
You can give Melius complex instructions in natural language:
- *"Search for the latest news on AI agents and write a summary to workspace/research.md"*
- *"Create a sub-agent to monitor my GitHub repo for new issues and alert me via Telegram."*
- *"Build a tool that can resize images in the workspace folder."*

---

## 📂 Project Architecture

- **`/melius/`**: The engine room. Contains the orchestrator, memory managers, and core logic.
- **`/tools/`**: The skill vault. This is where both built-in and agent-created tools reside.
- **`/workspace/`**: The agent's playground. All file operations happen here.
- **`/memory/`**: Persistent storage for agent knowledge and identity.
- **`/agents/`**: Configurations for specialized sub-agents.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Built with ❤️ for the local AI community.*
