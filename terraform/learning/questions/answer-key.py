def make_answer_key(input_file_path: str) -> None:
  output_file_path: str = input_file_path + ".output.md"
  with open(input_file_path, "r", encoding="utf-8") as file:
    num: int = 0
    lines = file.read()
    questions = lines.split("---")
    print(f"\n[DEBUG] Processing: {input_file_path}")
    print(f"[DEBUG] Total sections after split: {len(questions)}")

    rewritten = []
    for i, question in enumerate(questions):
        # Only process sections that are actual questions
        if '### Question' not in question:
          continue

        # Find the **Answer field (not **Answer Type)
        # We need to locate the line that has **Answer**: or **Answer:**
        answer_value = None
        answer_explanation = None
        difficulty = "N/A"
        source = "N/A"
        answer_type = "N/A"
        question_text = ""

        found_answer = False
        for line_num, line in enumerate(question.split('\n')):
          stripped = line.strip()

          # Capture metadata fields
          if stripped.startswith('**Difficulty'):
            if ':' in stripped:
              difficulty = stripped.split(':', 1)[1].strip()
          elif stripped.startswith('**Topic'):
            if ':' in stripped:
              source = stripped.split(':', 1)[1].strip()
          elif stripped.startswith('**Answer Type'):
            if ':' in stripped:
              answer_type = stripped.split(':', 1)[1].strip()

          # Find the actual **Answer field (check that 'Type' is not after **Answer)
          elif stripped.startswith('**Answer') and 'Type' not in stripped[:14]:
            found_answer = True
            if ':' in stripped:
              # Everything after the colon is the answer
              raw_answer = stripped.split(':', 1)[1].strip()
              # Strip leading asterisks (handles Unicode variants)
              answer_value = raw_answer.lstrip('*').strip()
            break
          elif stripped.startswith('**Question'):
            # Capture question text
            if line_num > 0:
              question_text = '\n'.join(question.split('\n')[max(0, line_num-5):line_num])

        if not found_answer or not answer_value:
          continue

        print(f"[DEBUG]   Section {i}: Found answer: {repr(answer_value[:40])}")

        # Extract explanation if present
        if '**Explanation' in question:
          exp_start = question.find('**Explanation')
          exp_text = question[exp_start:].split('\n')[0]
          if ':' in exp_text:
            answer_explanation = exp_text.split(':', 1)[1].strip()

        if not answer_explanation:
          answer_explanation = "N/A"

        # Build question text: everything from the start through all metadata and question body
        # We need to find the ACTUAL **Answer field (not **Answer Type)
        # Search line-by-line for the correct **Answer line
        all_text_lines = []
        for line in question.split('\n'):
          if line.strip().startswith('**Answer') and 'Type' not in line[:line.find(':')]:
            # This is the actual **Answer field, stop here
            break
          all_text_lines.append(line)

        all_text = '\n'.join(all_text_lines)

        num += 1
        try:
          print(f"[DEBUG]     Question #{num}: answer='{answer_value}', difficulty='{difficulty}'")
        except UnicodeEncodeError:
          # Fallback for Unicode errors in console output
          print(f"[DEBUG]     Question #{num}: answer extracted, difficulty='{difficulty}'")
        rewritten.append({
          "num": num,
          "question": all_text.strip(),
          "answer": answer_value,
          "explanation": answer_explanation,
          "difficulty": difficulty,
          "source": source,
          "answer_type": answer_type
        })

    print(f"[DEBUG] Total questions extracted: {len(rewritten)}")

    if rewritten:
      with open(output_file_path, "w", encoding="utf-8") as f:
        f.write("# Terraform Associate Exam Questions\n")
        for item in rewritten:
          f.write(f"\n---\n\n{item['question']}\n")
        f.write("\n## Answer Key\n\n| Q# | Answer(s) | Explanation | Source | Difficulty |\n")
        f.write("|----|-----------|-----------:|--------|------------|\n")
        for item in rewritten:
          f.write(f"| {item['num']} | {item['answer']} | {item['explanation']} | {item['source']} | {item['difficulty']} |\n")
      print(f"[DEBUG] Output created: {output_file_path}")
    else:
      print(f"[DEBUG] No questions processed")


def get_batch_files(path: str) -> list:
  import os
  files = []
  for file in os.listdir(path):
    if file.endswith(".md") and not file.endswith(".output.md"):
      files.append(os.path.join(path, file))
  return sorted(files)


def create_answers(path: str) -> None:
  for file in get_batch_files(path):
    make_answer_key(file)


if __name__ == "__main__":
  import os
  base_path = os.path.dirname(os.path.abspath(__file__))
  create_answers(base_path)
