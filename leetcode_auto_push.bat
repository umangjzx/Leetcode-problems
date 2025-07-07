@echo off
:: LeetCode Auto Git Push with File Check + README updater

set /p filename=Enter the filename (e.g. 1353. Problem Title.py): 

:: Check if file exists
if not exist "%filename%" (
    echo ❌ File not found: %filename%
    pause
    exit /b
)

:: Check if file is empty
for %%A in ("%filename%") do (
    if %%~zA==0 (
        echo ❌ ERROR: The file "%filename%" is empty!
        pause
        exit /b
    )
)

:: Ask for commit message
set /p message=Enter commit message: 

:: Stage + commit solution file
git add "%filename%"
git commit -m "%message%"

:: 🔄 Run Python script to update README.md
python update_readme.py

:: Stage and commit updated README.md
git add README.md
git commit -m "📊 Auto-update README with latest progress"

:: Push all to GitHub
git push origin main

echo ✅ Code and README pushed to GitHub!
pause
