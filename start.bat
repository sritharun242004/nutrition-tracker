@echo off
title FoodHealth AI - Setup and Start
color 0A

echo.
echo  ================================================
echo    FoodHealth AI - Food Detection ^& Health System
echo    Final Year Project
echo  ================================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  [ERROR] Python is not installed!
    echo  Please download and install Python 3.10+ from:
    echo  https://www.python.org/downloads/
    echo  Make sure to check "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)

echo  [OK] Python found.

:: Create virtual environment if not exists
if not exist "venv" (
    echo  [INFO] Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
echo  [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

:: Upgrade pip silently
echo  [INFO] Upgrading pip...
python -m pip install --upgrade pip --quiet

:: Install dependencies
echo  [INFO] Installing dependencies (this may take a minute)...
pip install -r requirements.txt --quiet

if %errorlevel% neq 0 (
    echo.
    echo  [ERROR] Failed to install dependencies.
    echo  Please check your internet connection and try again.
    pause
    exit /b 1
)

echo  [OK] All dependencies installed.
echo.
echo  ================================================
echo    Starting server at http://localhost:5001
echo    Open your browser and go to:
echo    http://localhost:5001
echo.
echo    Demo Login:
echo    Email   : demo@foodhealth.com
echo    Password: demo123
echo.
echo    Press Ctrl+C to stop the server
echo  ================================================
echo.

:: Start the app
python run.py

pause
