#!/usr/bin/env python3
"""
Quiz Loader - Load markdown questions into Python quiz engine
"""

import sys
import re
from pathlib import Path
from typing import List, Dict

def parse_markdown_questions(file_path: str) -> List[Dict]:
    """Parse markdown question file and extract question metadata"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        questions = []

        # Count questions
        question_matches = list(re.finditer(r'### Question \d+', content, re.IGNORECASE))

        # Extract difficulty levels
        difficulties = {}
        for match in re.finditer(r'\*\*Difficulty\*\*:\s*(\w+)', content, re.IGNORECASE):
            difficulty = match.group(1).lower()
            difficulties[difficulty] = difficulties.get(difficulty, 0) + 1

        # Extract answer types
        answer_types = {}
        for match in re.finditer(r'\*\*Answer Type\*\*:\s*(\w+)', content, re.IGNORECASE):
            atype = match.group(1).lower()
            answer_types[atype] = answer_types.get(atype, 0) + 1

        return {
            'total': len(question_matches),
            'difficulties': difficulties,
            'answer_types': answer_types,
            'file_path': file_path,
            'file_name': Path(file_path).name
        }

    except FileNotFoundError:
        print(f"ERROR: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        # Use default file
        questions_file = Path(__file__).parent / "databricks" / "learning" / "questions" / "spark-databricks-iteration-1.md"
    else:
        questions_file = Path(sys.argv[1])

    if not questions_file.exists():
        print(f"ERROR: Question file not found: {questions_file}")
        sys.exit(1)

    print("\n" + "="*72)
    print("Quiz Loader - Python Quiz Engine")
    print("="*72 + "\n")

    result = parse_markdown_questions(str(questions_file))

    print(f"[SUCCESS] Loaded {result['total']} questions from {result['file_name']}")
    print(f"\nQuestion Summary:")
    print(f"  Total: {result['total']}")

    if result['difficulties']:
        print(f"\n  Difficulty Split:")
        for difficulty, count in sorted(result['difficulties'].items()):
            print(f"    {difficulty.capitalize()}: {count}")

    if result['answer_types']:
        print(f"\n  Answer Types:")
        for atype, count in sorted(result['answer_types'].items()):
            print(f"    {atype}: {count}")

    print(f"\n  File Path: {result['file_path']}")
    print(f"\nYou can now use these questions in your quiz engine!")
    print("="*72 + "\n")

if __name__ == '__main__':
    main()
