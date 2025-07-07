import os
import re

README_FILE = "README.md"
PROGRESS_HEADER = "## 📈 My LeetCode Progress"

def extract_problems():
    problems = []
    for filename in os.listdir():
        if filename.endswith(".py") and filename[0].isdigit():
            match = re.match(r"(\d+)\.\s(.+)\.py", filename)
            if match:
                number, title = match.groups()
                problems.append((int(number), title.strip()))
    return sorted(problems)

def generate_table(problems):
    header = "| Problem # | Title | Difficulty | Status |\n"
    header += "|-----------|-------|------------|--------|\n"
    rows = [f"| {num} | {title} | Unknown | ✅ Solved |" for num, title in problems]
    return header + "\n".join(rows)

def update_readme(problems):
    if not os.path.exists(README_FILE):
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write("# LeetCode Problems – Python Solutions 🐍\n\n")

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    new_table = f"{PROGRESS_HEADER}\n\n" + generate_table(problems)

    if PROGRESS_HEADER in content:
        content = re.sub(f"{PROGRESS_HEADER}(.|\n)*", new_table, content)
    else:
        content += "\n\n" + new_table

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md updated with LeetCode progress.")

if __name__ == "__main__":
    problems = extract_problems()
    update_readme(problems)
