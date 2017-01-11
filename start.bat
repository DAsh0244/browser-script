@echo off
echo starting...
setlocal EnableDelayedExpansion
SET lf=;
FOR /F "delims=" %%i IN ('where /R .\web_drivers\ *.exe') DO if ("!out!"=="") (set out=%%i) else (set out=!out!%lf%%%~pi)
rem ECHO %out%
SET PATH=%PATH%;%out%
rem echo %PATH%
python initial_test.py
echo Started!
pause
exit 0
