"""Computes the inverted index (solution/technique -> questions) by scanning
solutions/<technique>/questions/*.py and cross-referencing each question id
against questions/<rank>-<slug>/questions.txt for its title.

Writes solutions/inverted_index.json and prints a human-readable summary.
"""
import glob
import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")
QUESTIONS_DIR = os.path.join(REPO_ROOT, "questions")


def question_title(question_id):
    path = os.path.join(QUESTIONS_DIR, question_id, "questions.txt")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("Title:"):
                return line[len("Title:"):].strip()
    return None


def build_index():
    index = {}
    for technique_dir in sorted(glob.glob(os.path.join(SOLUTIONS_DIR, "*"))):
        if not os.path.isdir(technique_dir):
            continue
        technique = os.path.basename(technique_dir)
        questions_glob = os.path.join(technique_dir, "questions", "*.py")
        question_ids = sorted(
            os.path.splitext(os.path.basename(p))[0]
            for p in glob.glob(questions_glob)
            if os.path.basename(p) != "__init__.py"
        )
        if not question_ids:
            continue
        index[technique] = [
            {"id": qid, "title": question_title(qid)} for qid in question_ids
        ]
    return index


def main():
    index = build_index()

    out_path = os.path.join(SOLUTIONS_DIR, "inverted_index.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
        f.write("\n")

    total_links = sum(len(v) for v in index.values())
    print(f"{len(index)} technique(s), {total_links} question link(s) -> {out_path}\n")
    for technique, questions in index.items():
        print(f"{technique} ({len(questions)}):")
        for q in questions:
            print(f"  - {q['id']}: {q['title']}")
        print()


if __name__ == "__main__":
    main()
