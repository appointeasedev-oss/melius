# Melius 🌟

Melius is a headless, local-first AI agent CLI system. It runs entirely on your local machine using **Ollama**, giving you full control and privacy.

## Features

- 🤖 **Local-First**: Powered by Ollama models (llama3, mistral, etc.)
- 💻 **Headless CLI**: No GUI, just pure logic and terminal interaction.
- 📅 **Task Scheduler**: Schedule jobs (e.g., "commit to repo at 5 PM").
- 🛠️ **Self-Improving**: Agent can edit its own tools and acquire new skills.
- 📂 **File Mastery**: Read, edit, and modify files in its dedicated `/workspace`.
- 🧠 **Memory**: Short-term and long-term memory persistence.
- 🌐 **Internet Access**: Integrated browser operations.
- 📱 **Telegram Remote**: Control your agent via Telegram bot.
- 🪟 **Windows Optimized**: Designed for Windows command line environments.

## Installation

1. **Install Ollama**: Download and install from [ollama.com](https://ollama.com).
2. **Clone the Repo**:
   ```bash
   git clone https://github.com/appointeasedev-oss/melius.git
   cd melius
   ```
3. **Setup Environment**:
   ```bash
   pip install -e .
   melius setup
   ```

## Usage

### Start Interactive Mode
```bash
melius start --model llama3
```

### Manage Models
```bash
melius list-models
melius download llama3
```

### Scheduling Tasks
You can ask Melius to schedule tasks in natural language:
> "Schedule a git commit for all changes in the workspace today at 5 PM."

## Architecture

- `/melius/`: Core engine and logic.
- `/workspace/`: The agent's playground for file operations.
- `/tools/`: Expandable toolset for the agent.
- `/memory/`: Persistent memory storage.

## License
MIT
