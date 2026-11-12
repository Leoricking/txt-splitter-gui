@echo off
title Python Runner
echo Starting script...
python txt_splitter_gui.py
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python failed to start. 
    echo Please check if Python is installed and added to PATH.
    pause
)