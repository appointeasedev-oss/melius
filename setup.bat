@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo    Melius AI Agent - Ultimate Setup
echo ==========================================

:: Check for Ollama
where ollama >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Ollama not found. Starting automated installation...
    echo [i] Downloading Ollama installer for Windows...
    powershell -Command "Invoke-WebRequest -Uri 'https://ollama.com/download/OllamaSetup.exe' -OutFile 'OllamaSetup.exe'"
    if exist OllamaSetup.exe (
        echo [i] Running Ollama installer... Please follow the prompts.
        start /wait OllamaSetup.exe
        del OllamaSetup.exe
        echo [OK] Ollama installation initiated.
    ) else (
        echo [!] Failed to download Ollama. Please install it manually from https://ollama.com
        pause
        exit /b 1
    )
) else (
    echo [OK] Ollama is already installed.
)

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

:: Setup Virtual Environment
if not exist venv (
    echo [i] Creating virtual environment...
    python -m venv venv
)

echo [i] Activating virtual environment and installing Melius...
call venv\Scripts\activate
pip install -e .

:: Initialize Melius
echo [i] Initializing Melius folders and configuration...
melius setup

echo.
echo ==========================================
echo    SETUP COMPLETE!
echo ==========================================
echo To start your agent, run:
echo   melius start
echo.
pause
