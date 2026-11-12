@echo off
title EXE Builder
echo Checking for PyInstaller...
pip install pyinstaller

echo Building EXE...
pyinstaller -F -w --clean txt_splitter_gui.py

echo.
echo ==========================================
echo Done! Your EXE is in the "dist" folder.
echo ==========================================
pause