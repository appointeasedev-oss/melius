# Melius Architecture

Melius is a headless, local-first AI agent CLI designed for Windows. It leverages local LLMs via Ollama and provides a suite of tools for file manipulation, scheduling, and automation.

## Core Components

1.  **CLI Interface**: Entry point for user interaction via command line.
2.  **Agent Engine**: Orchestrates the loop (Think -> Act -> Observe).
3.  **Local LLM Manager**: Interfaces with Ollama for model management and inference.
4.  **Toolbox**: A set of default tools (file operations, browser, git) and a mechanism for the agent to create/modify tools.
5.  **Memory System**: 
    *   **Short-term**: Context window management.
    *   **Long-term**: Local vector store or JSON-based persistent storage.
6.  **Scheduler**: Manages one-time or recurring tasks using a local job queue.
7.  **Integrations**:
    *   **Telegram Bot**: Remote control and notifications.
    *   **Browser**: Playwright/Selenium for web tasks.

## Directory Structure

- `/melius/` (Core logic)
- `/tools/` (Individual tool definitions)
- `/workspace/` (Agent's working directory)
- `/memory/` (Persistent data)
- `/agents/` (Sub-agent definitions)
- `/models/` (Model configuration)
