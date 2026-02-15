'''
# Melius - The Ultimate User Guide

Welcome to the official guide for **Melius**, your headless, local-first AI agent. This document provides a comprehensive overview of every command, feature, and advanced usage scenario.

---

## Table of Contents

1.  [**Core Concepts**](#1-core-concepts)
    -   The Orchestrator (Melius-Prime)
    -   Sub-Agents
    -   The Memory System
    -   The Tool System
2.  [**Installation**](#2-installation)
    -   Prerequisites
    -   Automated Windows Setup
    -   Manual Setup (Linux/macOS)
3.  [**CLI Commands**](#3-cli-commands)
    -   `melius start`
    -   `melius setup`
    -   `melius list-tools`
    -   `melius list-models`
    -   `melius download`
4.  [**Advanced Usage**](#4-advanced-usage)
    -   Interacting with the Agent
    -   Multi-Agent Workflows
    -   Self-Improvement: Creating New Tools
    -   Using the Workspace
5.  [**Configuration**](#5-configuration)
    -   Environment Variables

---

## 1. Core Concepts

Melius operates on a few key principles that make it powerful and autonomous.

### The Orchestrator (Melius-Prime)

When you run `melius start`, you are interacting with **Melius-Prime**. This is the main agent responsible for understanding your requests, planning tasks, and delegating work. It is the central "brain" of the system.

### Sub-Agents

For complex tasks, Melius-Prime can create specialized **sub-agents**. For example, if you ask it to "research a topic and write a report," it might spawn:

-   A `Researcher-Agent` to browse the web and gather information.
-   A `Writer-Agent` to compile the gathered information into a structured document.

This allows for parallel processing and more efficient task completion.

### The Memory System

Melius has a dual-layer memory:

-   **Short-Term Memory**: A sliding window of the last 20 interactions. This provides immediate context for ongoing conversations.
-   **Long-Term Memory**: A persistent JSON file (`/memory/<agent_name>_memory.json`) where the agent stores critical facts, learned knowledge, and a full history of all interactions.

### The Tool System

Tools are the agent's hands. They are Python scripts located in the `/tools` directory that allow the agent to interact with the outside world. Melius comes with a set of powerful built-in tools:

| Tool Name          | Description                                         |
| ------------------ | --------------------------------------------------- |
| `shell_execute`    | Execute any command in the system shell.            |
| `browser_action`   | Navigate websites, scrape content, and perform searches. |
| `file_operation`   | Read, write, and list files in the `/workspace` folder. |
| `github_manage`    | Interact with GitHub repositories using the `gh` CLI. |

Most importantly, Melius can **create its own tools** if it determines a capability is missing.

---

## 2. Installation

### Prerequisites

-   **Python 3.10+**
-   **Ollama**: For running local LLMs.
-   **GitHub CLI**: (Optional) For using the GitHub tool.

### Automated Windows Setup

The easiest way to install Melius on Windows is to use the provided script.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/appointeasedev-oss/melius.git
    cd melius
    ```
2.  **Run the setup script**:
    ```bash
    ./setup.bat
    ```
    This script will automatically check for and install **Ollama** if it's missing, create a virtual environment, and install all dependencies.

### Manual Setup (Linux/macOS)

1.  **Clone the repository** as shown above.
2.  **Install dependencies**:
    ```bash
    pip install -e .
    ```
3.  **Run the setup command** to verify the environment:
    ```bash
    melius setup
    ```

---

## 3. CLI Commands

Melius is controlled through a simple and powerful command-line interface.

### `melius start`

This is the main command to launch the Melius Orchestrator.

-   **Usage**: `melius start`
-   **Options**:
    -   `--model <model_name>`: Specify which Ollama model to use (e.g., `llama3`, `mistral`). Defaults to `llama3`.

### `melius setup`

Verifies that all dependencies and configurations are correctly set up.

-   **Usage**: `melius setup`
-   **Checks**: Ollama status, GitHub CLI availability, and directory structures.

### `melius list-tools`

Displays a table of all currently registered tools, both built-in and dynamically created.

-   **Usage**: `melius list-tools`

### `melius list-models`

Lists all models that are currently available in your local Ollama installation.

-   **Usage**: `melius list-models`

### `melius download <model_name>`

Downloads a new model from the Ollama library.

-   **Usage**: `melius download mistral`

---

## 4. Advanced Usage

### Interacting with the Agent

Once you run `melius start`, you can give it tasks in natural language. The key is to be clear and specific. The agent will respond with its `Thought` process and the `Action` it intends to take.

**Example Prompt**:
> "Read the contents of `project_plan.txt` in the workspace and summarize the key milestones."

### Multi-Agent Workflows

You can instruct Melius-Prime to delegate tasks.

**Example Prompt**:
> "Create a sub-agent named 'Code-Monkey' whose role is to write Python scripts. Then, ask it to create a script that lists all files in a directory."

### Self-Improvement: Creating New Tools

This is Melius's most powerful feature. If you give it a task it cannot perform, it will attempt to build the tool it needs.

**Example Prompt**:
> "I need a tool that can tell me the current weather. Create a tool named 'weather_tool' that uses an API to fetch the weather for a given city."

Melius will then write `weather_tool.py` into the `/tools` folder, and it will be available for immediate use.

### Using the Workspace

The `/workspace` directory is the agent's primary area for file-based tasks. Any files you want the agent to read, write, or modify should be placed there.

---

## 5. Configuration

Melius can be configured using a `.env` file in the root directory.

### Environment Variables

-   `OLLAMA_BASE_URL`: The URL for your Ollama instance (default: `http://localhost:11434`).
-   `DEFAULT_MODEL`: The default model to use if not specified (default: `llama3`).
-   `TELEGRAM_TOKEN`: Your Telegram bot token for remote control (optional).
'''
