# Quiz Loader - Quick Start Guide

## What Was Created

You now have **3 files** in your exam-prep workspace to easily load questions into your Python quiz engine:

### 1. **load-question.bat** — Full-Featured Loader ⭐ RECOMMENDED
**Use this for detailed validation and diagnostics**

```batch
load-question.bat                                    # Load default Databricks questions
load-question.bat "path\to\custom-questions.md"    # Load custom question file
```

**Features:**
- ✅ Validates Python 3.9+ installation
- ✅ Confirms loader script exists
- ✅ Parses and counts all questions
- ✅ Displays difficulty breakdown (Easy/Medium/Hard)
- ✅ Shows answer type split (one/many)
- ✅ Comprehensive error checking with helpful messages
- ✅ Displays file path for easy copying

**Output Example:**
```
============================================================================
Quiz Loader - Python Quiz Engine
============================================================================

[1/3] Checking Python installation...
[OK] Found: Python 3.14.3

[2/3] Validating loader script...
[OK] Loader script found

[3/3] Loading questions...

[SUCCESS] Loaded 100 questions from spark-databricks-iteration-1.md

Question Summary:
  Total: 100
  Difficulty Split:
    Easy: 20
    Hard: 20
    Medium: 60
  Answer Types:
    many: 23
    one: 77

File Path: c:\Users\Pete\Desktop\exam-prep-1\databricks\learning\questions\spark-databricks-iteration-1.md

Questions loaded successfully!
```

### 2. **quick-quiz.bat** — Fast Launcher
**Use this for quick access to your default question file**

```batch
quick-quiz.bat                                      # Load default questions
quick-quiz.bat "path\to\custom-questions.md"      # Load custom file
```

**Features:**
- ✅ Instant launch without full validation
- ✅ Same output as full loader
- ✅ Perfect for daily quiz sessions

### 3. **quiz_loader.py** — Python Module
**Core Python script that parses markdown questions**

This is called by the batch files. You can also use it directly:

```batch
python quiz_loader.py
python quiz_loader.py "c:\path\to\questions.md"
```

---

## How to Use

### Option 1: Double-Click (Easiest)
1. Open Windows Explorer
2. Navigate to `c:\Users\Pete\Desktop\exam-prep-1`
3. **Double-click `load-question.bat`**
4. Review the output
5. Press any key when done

### Option 2: Command Line
1. Open Command Prompt (Win+R, type `cmd`)
2. Run:
   ```batch
   cd c:\Users\Pete\Desktop\exam-prep-1
   load-question.bat
   ```

### Option 3: With Custom Question File
```batch
load-question.bat "c:\Users\Pete\Desktop\exam-prep-1\databricks\learning\questions\spark-databricks-iteration-1.md"
```

---

## Default Question File

By default, the loaders use:
```
c:\Users\Pete\Desktop\exam-prep-1\databricks\learning\questions\spark-databricks-iteration-1.md
```

This file contains:
- **100 Databricks Spark Questions**
- **Iteration 1** of the question bank
- **Topics:** Architecture, SQL, DataFrames, Troubleshooting, Streaming, Spark Connect, Pandas API

---

## Requirements

### ✅ Already Installed
- Python 3.14.3 (or newer)
- All required dependencies (sqlite3, re, pathlib - all built-in)

### If Python is Missing
1. Download from: https://www.python.org/downloads/
2. Run installer and **CHECK** "Add Python to PATH"
3. Restart your computer
4. Try again

---

## Troubleshooting

### "Python is not installed or not in PATH"
```batch
REM Verify Python installation:
python --version

REM If this fails, reinstall Python with "Add Python to PATH" checked
```

### "quiz_loader.py not found"
Make sure you're running from the correct directory:
```batch
REM Correct:
cd c:\Users\Pete\Desktop\exam-prep-1
load-question.bat

REM Wrong (won't work):
cd c:\Users\Pete\Desktop
load-question.bat
```

### Question file shows 0 questions
- Verify the markdown file exists and has proper format
- Check that headers follow pattern: `### Question 1 — Topic`
- Review the file in VS Code to confirm structure

---

## File Structure

```
exam-prep-1/
├── load-question.bat           ← Full-featured loader
├── quick-quiz.bat              ← Quick launcher
├── quiz_loader.py              ← Python question parser
├── QUIZ_LOADER_README.md       ← Full documentation
├── databricks/
│   └── learning/
│       └── questions/
│           └── spark-databricks-iteration-1.md  ← Your questions
└── engine/
    └── [quiz engine files]
```

---

## Next Steps

1. **Run the loader:**
   ```batch
   load-question.bat
   ```

2. **Copy the file path** shown in the output

3. **Load into your quiz engine:**
   - Use the file path to point your quiz engine to the questions
   - Start taking quizzes on Databricks Spark topics

4. **Track your progress:**
   - Review missed questions
   - Focus on weak areas
   - Retake quizzes on specific topics

---

## Pro Tips

✅ **Create Shortcuts**
- Right-click `load-question.bat` → Send to → Desktop (create shortcut)
- Double-click shortcut to load questions anytime

✅ **Load Different Question Files**
```batch
REM Create custom batch files:
@echo off
load-question.bat "databricks\learning\questions\your-questions.md"
pause
```

✅ **Automate with Windows Task Scheduler**
- Schedule daily reminders to quiz
- Set time when you want to study

✅ **Use in PowerShell**
```powershell
cd C:\Users\Pete\Desktop\exam-prep-1
& ".\load-question.bat"
```

---

## Summary

| File | Purpose | When to Use |
|------|---------|-----------|
| **load-question.bat** | Full validation + loading | First time, or when troubleshooting |
| **quick-quiz.bat** | Fast launch | Daily quizzes, quick access |
| **quiz_loader.py** | Python core | Direct Python usage |

---

**You're all set! Happy studying! 🚀**
