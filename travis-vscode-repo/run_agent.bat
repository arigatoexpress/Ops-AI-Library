@echo off
setlocal enabledelayedexpansion

:: ============================================================================
:: NRXX Peak Staffing Automated Agent Runner (Windows 11 & UTF-8 Compatible)
:: ============================================================================

:: 1. Force UTF-8 Encoding to prevent UnicodeEncodeError with emojis/symbols
chcp 65001 >nul
set PYTHONIOENCODING=utf-8

:: 2. Define Paths & Set Working Directory
set "PROJECT_DIR=%~dp0"
cd /d "%PROJECT_DIR%"

:: Create logs folder if it doesn't exist
if not exist "logs" mkdir "logs"

:: 3. Create timestamp for log naming (WMIC-free, Windows 11 compatible)
for /f "usebackq tokens=*" %%i in (`powershell -NoProfile -Command "Get-Date -Format 'yyyyMMdd_HHmmss'"`) do set "DATETIME=%%i"
set "LOG_FILE=%PROJECT_DIR%logs\agent_run_%DATETIME%.log"

echo ======================================================= >> "%LOG_FILE%"
echo NRXX Staffing Agent Run Initiated: %DATE% %TIME% >> "%LOG_FILE%"
echo Working Directory: %CD% >> "%LOG_FILE%"
echo ======================================================= >> "%LOG_FILE%"

:: 4. Identify Python Binary
set "PYTHON_EXE=python"
if exist "C:\Users\3159391\AppData\Local\Programs\Python\Python312\python.exe" (
    set "PYTHON_EXE=C:\Users\3159391\AppData\Local\Programs\Python\Python312\python.exe"
)

:: 5. Execute Pipeline with UTF-8 Stream
echo Executing build_weekly_staffing_data.py... >> "%LOG_FILE%" 2>&1
"%PYTHON_EXE%" build_weekly_staffing_data.py >> "%LOG_FILE%" 2>&1

set EXIT_CODE=%ERRORLEVEL%

if %EXIT_CODE% EQU 0 (
    echo [SUCCESS] Pipeline completed successfully at %TIME%. >> "%LOG_FILE%"
) else (
    echo [ERROR] Pipeline failed with exit code %EXIT_CODE% at %TIME%. >> "%LOG_FILE%"
)

echo ======================================================= >> "%LOG_FILE%"
exit /b %EXIT_CODE%