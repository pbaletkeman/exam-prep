@echo off
REM ============================================================================
REM load-question.bat - Load Databricks questions into Python Quiz Engine
REM ============================================================================
REM Purpose: Parse markdown question file and load into Python quiz engine
REM Usage:   load-question.bat [question_file]
REM ============================================================================

setlocal enabledelayedexpansion

REM Set defaults
set QUESTIONS_FILE=%~1
set WORKSPACE_ROOT=%~dp0

REM If no file provided, use default (script handles it)
if "!QUESTIONS_FILE!"=="" (
    set QUESTIONS_FILE=
)

REM Display banner
cls
echo.
echo ============================================================================
echo Quiz Loader - Python Quiz Engine
echo ============================================================================
echo.

REM Validate Python installation
echo [1/3] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [OK] Found: !PYTHON_VERSION!
echo.

REM Check that loader script exists
echo [2/3] Validating loader script...
if not exist "!WORKSPACE_ROOT!quiz_loader.py" (
    echo ERROR: quiz_loader.py not found at !WORKSPACE_ROOT!
    echo.
    pause
    exit /b 1
)
echo [OK] Loader script found
echo.

REM Run Python loader
echo [3/3] Loading questions...
echo.

if "!QUESTIONS_FILE!"=="" (
    python "!WORKSPACE_ROOT!quiz_loader.py"
) else (
    python "!WORKSPACE_ROOT!quiz_loader.py" "!QUESTIONS_FILE!"
)

set LOAD_STATUS=!errorlevel!

echo.
echo ============================================================================
echo.

if !LOAD_STATUS! equ 0 (
    echo Questions loaded successfully!
    echo.
    echo Next Steps:
    echo   1. Start the quiz engine and point it to the question file above
    echo   2. Select the questions you want to quiz on
    echo   3. Begin studying!
    echo.
) else (
    echo Failed to load questions. Check the error message above.
)

pause
endlocal
exit /b !LOAD_STATUS!
