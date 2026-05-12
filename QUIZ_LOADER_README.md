# Quiz Loader - Batch Files Guide

## Overview
These batch files make it easy to load your Databricks Spark certification questions into your Python quiz engine.

## Files Created

### 1. `load-question.bat` - Full-Featured Loader
**Purpose:** Comprehensive question loader with validation and diagnostics

**Usage:**
```batch
load-question.bat                                    REM Uses default Databricks iteration 1
load-question.bat "path\to\questions.md"            REM Load specific question file
load-question.bat "path\to\questions.md" python     REM Specify engine type
```

**Features:**
- ✅ Validates Python installation (3.9+)
- ✅ Verifies question file exists and counts questions
- ✅ Checks quiz engine directory
- ✅ Validates Python dependencies
- ✅ Parses markdown and extracts question metadata
- ✅ Displays question summary (difficulty, answer types)
- ✅ Color-coded output with progress indicators
- ✅ Helpful error messages

**Example Output:**
```
============================================================================
Quiz Loader - Python Quiz Engine
============================================================================

[1/5] Checking Python installation...
[OK] Found: Python 3.11.0

[2/5] Validating question file...
[OK] Found question file with ~100 questions
     File: c:\Users\Pete\Desktop\exam-prep-1\databricks\learning\questions\spark-databricks-iteration-1.md

[3/5] Checking quiz engine installation...
[OK] Quiz engine found

[4/5] Checking Python dependencies...
[OK] Dependencies ready

[5/5] Loading questions...

[SUCCESS] Loaded 100 questions from spark-databricks-iteration-1.md

Question Summary:
  - Total: 100
  - Difficulty split:
      Easy: 20
      Hard: 20
      Medium: 60
  - Answer Types:
      many: 23
      one: 77

You can now use these questions in your quiz engine!
```

### 2. `quick-quiz.bat` - Quick Launcher
**Purpose:** Fast way to get the question file path and launch

**Usage:**
```batch
quick-quiz.bat
```

**Features:**
- ✅ Instant question file path display
- ✅ Quick question count
- ✅ Minimal validation
- ✅ Ready-to-copy file path

---

## How to Use

### Method 1: Full Validation (Recommended)
1. Open Command Prompt (Win+R, type `cmd`)
2. Navigate to your exam-prep folder:
   ```batch
   cd c:\Users\Pete\Desktop\exam-prep-1
   ```
3. Run the loader:
   ```batch
   load-question.bat
   ```
4. Follow the progress and next steps shown

### Method 2: Quick Launch
1. Open Command Prompt
2. Navigate to exam-prep folder
3. Run:
   ```batch
   quick-quiz.bat
   ```
4. Copy the file path shown

### Method 3: Command Line with Custom File
```batch
load-question.bat "c:\path\to\custom-questions.md" python
```

---

## Requirements

### Python Installation
- **Minimum:** Python 3.9+
- **Check Installation:** Open cmd and run:
  ```batch
  python --version
  ```
- **Install if Missing:** Download from https://www.python.org/downloads/
  - ⚠️ **Important:** Check "Add Python to PATH" during installation

### Question File Format
Your markdown file should have:
```markdown
### Question 1 — Topic

**Difficulty**: Easy
**Answer Type**: one
**Topic**: specific topic

**Question**:
What is the primary responsibility of...

- A) Option A
- B) Option B
- C) Option C
- D) Option D
```

---

## Troubleshooting

### "Python is not installed or not in PATH"
**Solution:**
1. Install Python from https://www.python.org/downloads/
2. Check "Add Python to PATH" during installation
3. Restart Command Prompt
4. Run `load-question.bat` again

### "Question file not found"
**Solution:**
1. Verify file path exists: `dir "path\to\file.md"`
2. Use full absolute path or relative path from batch file location
3. Use `load-question.bat "c:\full\path\to\file.md"`

### "Quiz engine directory not found"
**Solution:**
1. Ensure you're running from the exam-prep root folder
2. Check that the `engine` folder exists
3. Directory structure should be:
   ```
   exam-prep-1/
   ├── load-question.bat  (this file)
   ├── engine/
   └── databricks/
       └── learning/
           └── questions/
               └── spark-databricks-iteration-1.md
   ```

### Script runs but no output
**Solution:**
1. Ensure Command Prompt window is large enough
2. Try running with explicit python path:
   ```batch
   "C:\Python311\python.exe" -c "print('test')"
   ```
3. Check if Python is actually installed: `python --version`

---

## Customization

### Load Different Question Files
Create a custom batch file:
```batch
@echo off
load-question.bat "databricks\learning\questions\terraform-questions.md" python
pause
```

### Add to Windows Context Menu
To right-click and load a file:
1. Save as `.reg` file:
   ```
   Windows Registry Editor Version 5.00

   [HKEY_CLASSES_ROOT\.md\shell\Load in Quiz Engine\command]
   @="cmd /k \"c:\\path\\to\\exam-prep-1\\load-question.bat\" \"%1\""
   ```
2. Double-click to apply

### Schedule Regular Quiz Sessions
Create a Windows Task Scheduler entry to remind you:
```batch
REM In Task Scheduler, set action to:
REM Program: cmd.exe
REM Arguments: /k "C:\path\to\exam-prep-1\quick-quiz.bat"
```

---

## File Structure

```
exam-prep-1/
├── load-question.bat              ← Full-featured loader
├── quick-quiz.bat                 ← Quick launcher
├── QUIZ_LOADER_README.md          ← This file
├── engine/
│   └── [quiz engine files]
├── databricks/
│   └── learning/
│       └── questions/
│           ├── spark-databricks-iteration-1.md
│           └── [other question files]
└── [other folders]
```

---

## Next Steps

After loading questions, you can:

1. **Start Quiz Session**
   - Point your quiz engine to the loaded question file
   - Select difficulty level (Easy, Medium, Hard)
   - Choose single questions or mixed batches

2. **Track Progress**
   - Use the quiz engine's scoring system
   - Review missed questions
   - Focus on weak areas

3. **Add More Questions**
   - Create additional markdown files
   - Use `load-question.bat` with different files
   - Merge multiple files using tools in the workspace

---

## Tips & Best Practices

✅ **DO:**
- Run from the exam-prep-1 root directory
- Use full paths for question files
- Check Python version regularly (run updates)
- Keep batch files in sync if you modify them

❌ **DON'T:**
- Modify question markdown structure
- Run from deep subdirectories
- Assume paths work from different locations
- Move batch files without updating paths

---

## Support & Contributing

- **Issue:** Questions not loading? Check error messages carefully
- **Bug:** Found a problem? Check the troubleshooting section
- **Enhancement:** Want to add features? Edit the batch files as needed

---

## Version History

- **v1.0** (2026-05-11) - Initial release
  - `load-question.bat` - Full validation and loading
  - `quick-quiz.bat` - Quick launcher
  - Supports Databricks Spark questions by default
  - Python-based question parser

---

**Happy studying! 🚀**
