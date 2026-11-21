Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Starting Learnix AI Backend & Frontend..." -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

Start-Process cmd.exe -ArgumentList "/k cd /d `"$PSScriptRoot\backend`" && python main.py"
Start-Process cmd.exe -ArgumentList "/k cd /d `"$PSScriptRoot\frontend`" && npm run dev"

Write-Host ""
Write-Host "Servers launched in separate windows:" -ForegroundColor Green
Write-Host "  Frontend: http://localhost:5173" -ForegroundColor Yellow
Write-Host "  Backend:  http://localhost:8000" -ForegroundColor Yellow
Write-Host ""
