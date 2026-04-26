import glob
import os

def merge_batches(iter_num, directory):
    pattern = os.path.join(directory, f"tf-associate-iter{iter_num}-batch*.md")
    batch_files = sorted(glob.glob(pattern))
    output_file = os.path.join(directory, f"tf-associate-iter{iter_num}.md")

    headers = []
    bodies = []
    for batch_file in batch_files:
        with open(batch_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
            # Header: from start to first '---' line (inclusive)
            header_end = 0
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    header_end = i + 1  # include the '---' line
                    break
            headers.append(''.join(lines[:header_end]).rstrip())
            # Body: from after the header separator onward
            bodies.append(''.join(lines[header_end:]).lstrip())

    with open(output_file, "w", encoding="utf-8") as outfile:
        # Write all headers at the top
        outfile.write('\n\n'.join(headers))
        outfile.write("\n\n---\n\n")
        # Write all bodies, separated by ---
        for idx, body in enumerate(bodies):
            outfile.write(body.rstrip())
            if idx < len(bodies) - 1:
                outfile.write("\n\n---\n\n")

if __name__ == "__main__":
    # Change these as needed
    for iteration in range(1, 11):  # Assuming you have iterations 1 to 5
        # iteration = 1
        directory = "c:/Users/Pete/Desktop/exam-prep-1/terraform/learning/questions"
        merge_batches(iteration, directory)
        print(f"Merged tf-associate-iter{iteration}-batch* files into tf-associate-iter{iteration}.md")
