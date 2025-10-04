@echo off
echo Starter Git-push...

REM Aktiverer virtuell miljø (valgfritt)
REM call venv\Scripts\activate.bat

REM Legger til alle endringer
git add .

REM Commit med standardmelding
git commit -m "Oppdatering via batch"

REM Pusher til GitHub
git push origin main

echo Ferdig!
pause
