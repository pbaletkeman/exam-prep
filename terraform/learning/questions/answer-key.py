def make_answer_key() -> None:

  with open("C:\\Users\\Pete\\Desktop\\exam-prep-1\\terraform\\learning\\questions\\tf-associate-iter1-batch1.md", "r", encoding="utf-8") as file:
    num: int = 0
    lines = file.read()
    questions = lines.split("---")
    rewritten = []
    source: str = ""
    for question in questions:
        if '**Answer**' in question:

          question_lines = question.split("**Answer**")
          question_text = question_lines[0].replace("\n\n### Question ","")[2:].strip()[1:].strip()
          answer_text = question_lines[1]
          difficulty = question_text.split("**Difficulty**:")[1].strip().split("\n")[0]
          source = question_text.split("**Topic**:")[1].strip().split("\n")[0]
          answer_type = question_text.split("**Answer Type**:")[1].strip().split("\n")[0]
          a = answer_text.split("**Explanation**")
          answer_value = a[0][1:].strip()
          answer_explain = a[1].strip()[2:].strip()
          num += 1
          rewritten.append({"num":num, "question": question_text, "answer": answer_value[0], "explanation": answer_explain, "difficulty":difficulty, "source":source, "answer_type":answer_type})

    for item in rewritten:
      print(f"{item['num']}: {item['question']}\n")



    print(f"""
    ## Answer Key

    | Q# | Answer(s) | Explanation | Source | Difficulty |
    |----|-----------|-------------|--------|------------|
    """)
    for item in rewritten:
      if int(item["num"]) > 5:
        return
      print(f"{item['num']} | {item['answer']} | {item['explanation']} | {item['source']} | {item['difficulty']} |")
      print("\n")


if __name__ == "__main__":
  make_answer_key()
