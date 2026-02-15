@echo off
echo Setting up Melius AI Agent...

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.10 or higher.
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
echo Installing dependencies...
pip install -e .

:: Run Melius setup
echo Initializing Melius folders...
melius setup

echo.
echo Melius setup complete! 
echo To start, run: melius start
pause
