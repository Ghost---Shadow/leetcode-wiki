"""Lists questions in questions/ that no technique in solutions/ covers yet,
and writes a coverage report to solutions/COVERAGE.md to track progress.

Reads solutions/inverted_index.json (regenerate first with build_index.py if
it's stale) and diffs its covered question ids against every questions/q<id>
package, sorted by rank.
"""
import json
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")
QUESTIONS_DIR = os.path.join(REPO_ROOT, "questions")
REPORT_PATH = os.path.join(SOLUTIONS_DIR, "COVERAGE.md")


def all_question_ids():
    ids = []
    for name in os.listdir(QUESTIONS_DIR):
        if os.path.isdir(os.path.join(QUESTIONS_DIR, name)) and re.match(r"^q\d+_", name):
            ids.append(name)
    return sorted(ids, key=lambda qid: int(qid[1:qid.index("_")]))


def technique_by_question_id():
    index_path = os.path.join(SOLUTIONS_DIR, "inverted_index.json")
    with open(index_path, encoding="utf-8") as f:
        index = json.load(f)
    technique_of = {}
    for technique, entries in index.items():
        for entry in entries:
            technique_of[entry["id"]] = technique
    return technique_of


def question_title(question_id):
    path = os.path.join(QUESTIONS_DIR, question_id, "questions.txt")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("Title:"):
                return line[len("Title:"):].strip()
    return None


def write_report(covered, uncovered, technique_of):
    total = len(covered) + len(uncovered)
    lines = [
        "# Coverage: solutions/ techniques vs. questions/",
        "",
        f"**{len(covered)}/{total} covered, {len(uncovered)} uncovered.**",
        "",
        "Regenerate with `python solutions/build_index.py && python solutions/find_uncovered.py`.",
        "",
        "## Covered",
        "",
    ]
    for qid in covered:
        title = question_title(qid) or "(no title found)"
        lines.append(f"- [x] {qid}: {title} -- `{technique_of[qid]}`")
    lines += ["", "## Uncovered", ""]
    for qid in uncovered:
        title = question_title(qid) or "(no title found)"
        lines.append(f"- [ ] {qid}: {title}")
    lines.append("")

    with open(REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def main():
    technique_of = technique_by_question_id()
    all_ids = all_question_ids()
    covered = [qid for qid in all_ids if qid in technique_of]
    uncovered = [qid for qid in all_ids if qid not in technique_of]

    write_report(covered, uncovered, technique_of)

    total = len(all_ids)
    print(f"{len(covered)}/{total} questions covered, {len(uncovered)} uncovered")
    print(f"Report written to {REPORT_PATH}\n")
    for qid in uncovered:
        title = question_title(qid) or "(no title found)"
        print(f"  - {qid}: {title}")


if __name__ == "__main__":
    main()
