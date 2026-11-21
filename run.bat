@echo off
echo ========================================================
echo Starting Learnix AI Backend and Frontend...
echo ========================================================

start "Learnix AI Backend (Port 8000)" cmd /k "cd /d %~dp0backend && python main.py"
start "Learnix AI Frontend (Port 5173)" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo Servers have been launched in separate windows:
echo - Frontend: http://localhost:5173
echo - Backend:  http://localhost:8000 (API and Docs at /docs)
echo.
