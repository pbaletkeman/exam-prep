@echo off
REM ============================================================================
REM quick-quiz.bat - Quick launch for Databricks Spark Questions
REM ============================================================================
REM Purpose: Fast launcher for loading and starting quiz session
REM Usage:   quick-quiz.bat [question_file]
REM ============================================================================

setlocal enabledelayedexpansion

set WORKSPACE_ROOT=%~dp0
set QUESTIONS_FILE=%~1

if "!QUESTIONS_FILE!"=="" (
    set QUESTIONS_FILE=!WORKSPACE_ROOT!databricks\learning\questions\spark-databricks-iteration-1.md
)

if not exist "!WORKSPACE_ROOT!quiz_loader.py" (
    echo ERROR: quiz_loader.py not found
    pause
    exit /b 1
)

python "!WORKSPACE_ROOT!quiz_loader.py" "!QUESTIONS_FILE!"
pause

endlocal
