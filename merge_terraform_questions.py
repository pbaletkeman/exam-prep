#!/usr/bin/env python3
"""
Merge Terraform Associate Learning Questions

Merges all tf-associate-iter10-batch*.md.output.md files into a single markdown file,
renumbering questions sequentially and consolidating the answer key at the end.
"""

import glob
import re
from pathlib import Path
from typing import List, Dict, Tuple


def sort_batch_files(files: List[str]) -> List[str]:
    """Sort files numerically by batch number (batch1, batch2, ..., batch8)."""
    def extract_batch_num(filepath: str) -> int:
        match = re.search(r'batch(\d+)', filepath)
        if match:
            return int(match.group(1))
        raise ValueError(f"Cannot extract batch number from {filepath}")

    return sorted(files, key=extract_batch_num)


def split_questions_and_answers(content: str) -> Tuple[str, str]:
    """Split file content into questions section and answer key section."""
    if "## Answer Key" not in content:
        raise ValueError("File does not contain '## Answer Key' section")

    parts = content.split("## Answer Key", 1)
    questions = parts[0].strip()
    answer_key = parts[1].strip()

    return questions, answer_key


def extract_questions(questions_text: str) -> List[str]:
    """Extract individual questions separated by --- delimiters."""
    # Remove header if present
    lines = questions_text.split('\n')

    # Skip header line(s) at the beginning
    question_lines = []
    skip_header = True
    for line in lines:
        if skip_header:
            if line.startswith('### Question'):
                skip_header = False
            else:
                continue
        question_lines.append(line)

    # Split by horizontal rules
    raw_questions = '\n'.join(question_lines).split('---')

    # Clean and filter
    questions = []
    for q in raw_questions:
        q = q.strip()
        if q and q.startswith('### Question'):
            questions.append(q)

    return questions


def extract_answer_key_rows(answer_key_text: str) -> List[Dict[str, str]]:
    """Parse markdown table into list of dictionaries."""
    lines = answer_key_text.split('\n')

    # Find table start (after "## Answer Key" which is already split)
    table_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('|'):
            table_start = i
            break

    if table_start == 0 and not lines[0].strip().startswith('|'):
        raise ValueError("Cannot find answer key table start")

    # Parse header
    header_line = lines[table_start].strip()
    headers = [h.strip() for h in header_line.split('|')[1:-1]]  # Remove empty edges

    if 'Q#' not in headers:
        raise ValueError(f"Answer key table missing 'Q#' column. Headers: {headers}")

    rows = []
    for line in lines[table_start + 2:]:  # Skip header and separator
        line = line.strip()
        if not line or not line.startswith('|'):
            break

        cells = [c.strip() for c in line.split('|')[1:-1]]  # Remove empty edges

        if len(cells) == len(headers):
            row = dict(zip(headers, cells))
            rows.append(row)

    return rows, headers


def renumber_question(question_text: str, new_num: int) -> str:
    """Replace question number with new global number."""
    # Match ### Question N — or ### Question NN —
    pattern = r'### Question \d+ —'
    replacement = f'### Question {new_num} —'

    return re.sub(pattern, replacement, question_text, count=1)


def update_answer_key_table(rows: List[Dict[str, str]], headers: List[str], offset: int) -> List[Dict[str, str]]:
    """Update Q# column in answer key rows with new global question numbers."""
    updated_rows = []
    for idx, row in enumerate(rows, start=1):
        new_row = row.copy()
        new_row['Q#'] = str(offset + idx)
        updated_rows.append(new_row)

    return updated_rows, offset + len(rows)


def format_answer_key_table(headers: List[str], rows: List[Dict[str, str]]) -> str:
    """Format answer key rows back into markdown table format."""
    # Build header
    table = "| " + " | ".join(headers) + " |\n"
    table += "|" + "|".join(["---"] * len(headers)) + "|\n"

    # Build rows
    for row in rows:
        cells = [row.get(h, '') for h in headers]
        table += "| " + " | ".join(cells) + " |\n"

    return table


def merge_files(input_dir: Path, output_file: Path):
    """Main merge function."""
    print(f"[*] Searching for batch files in {input_dir}...")

    # Find all batch files
    pattern = str(input_dir / "tf-associate-iter10-batch*.md.output.md")
    batch_files = glob.glob(pattern)

    if not batch_files:
        raise FileNotFoundError(f"No batch files found matching pattern: {pattern}")

    batch_files = sort_batch_files(batch_files)
    print(f"[+] Found {len(batch_files)} batch files")
    for f in batch_files:
        print(f"    - {Path(f).name}")

    # Validate we have exactly 8 files
    if len(batch_files) != 8:
        raise ValueError(f"Expected 8 batch files, found {len(batch_files)}")

    # Parse all files
    all_questions = []
    all_answer_rows = []
    answer_headers = None
    global_question_num = 1

    for batch_file in batch_files:
        print(f"\n[*] Processing {Path(batch_file).name}...")

        with open(batch_file, 'r', encoding='utf-8') as f:
            content = f.read()

        try:
            questions_text, answer_key_text = split_questions_and_answers(content)
        except ValueError as e:
            raise ValueError(f"Error parsing {Path(batch_file).name}: {e}")

        # Extract questions
        questions = extract_questions(questions_text)
        print(f"    Found {len(questions)} questions")

        # Extract answer key
        try:
            answer_rows, headers = extract_answer_key_rows(answer_key_text)
        except ValueError as e:
            raise ValueError(f"Error parsing answer key in {Path(batch_file).name}: {e}")

        if answer_headers is None:
            answer_headers = headers
        elif answer_headers != headers:
            raise ValueError(f"Answer key column mismatch in {Path(batch_file).name}")

        # Renumber questions
        renumbered_questions = []
        for q in questions:
            renumbered = renumber_question(q, global_question_num)
            renumbered_questions.append(renumbered)
            global_question_num += 1

        all_questions.extend(renumbered_questions)

        # Update answer key
        updated_answer_rows, global_question_num = update_answer_key_table(
            answer_rows, answer_headers, global_question_num - len(questions)
        )
        all_answer_rows.extend(updated_answer_rows)

        print(f"    ✓ Renumbered to global questions {global_question_num - len(questions)} - {global_question_num - 1}")

    # Build output
    print(f"\n[*] Building merged output file...")
    output_lines = []

    # Header
    output_lines.append("# Terraform Associate Exam Questions\n")

    # All questions
    output_lines.append("\n\n".join(all_questions))
    output_lines.append("\n")

    # Answer key section
    output_lines.append("\n## Answer Key\n")
    answer_table = format_answer_key_table(answer_headers, all_answer_rows)
    output_lines.append(answer_table)

    merged_content = "\n".join(output_lines)

    # Write output
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(merged_content)

    # Verification
    final_q_count = sum(1 for line in merged_content.split('\n') if line.startswith('### Question'))
    answer_key_q_count = len(all_answer_rows)

    print(f"\n[+] Merge complete!")
    print(f"    Total questions: {final_q_count}")
    print(f"    Answer key rows: {answer_key_q_count}")

    if final_q_count != answer_key_q_count:
        raise ValueError(
            f"Mismatch: {final_q_count} questions but {answer_key_q_count} answer rows"
        )

    print(f"    ✓ Output: {output_file}")


if __name__ == '__main__':
    workspace_root = Path(__file__).parent
    input_dir = workspace_root / "terraform" / "learning" / "questions"
    output_file = input_dir / "tf-associate-iter10-merged.md"

    try:
        merge_files(input_dir, output_file)
        print(f"\n[SUCCESS] Merged file created: {output_file}")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        exit(1)
