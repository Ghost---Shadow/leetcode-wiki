# leetcode-wiki
Inverted Index for Leetcode Problems

## Structure

Each problem lives in `questions/<rank>-<slug>/` and contains:
- `questions.txt` — problem metadata (title, difficulty, topics, companies, link)
- One or more solution files (e.g. `brute_force.py`), each exposing a `solve(...)` function
- `test_solutions.py` — discovers and runs every solution file in that same directory

## Running tests

Run tests for a single problem:

```bash
python questions/001-two-sum/test_solutions.py
```

Run tests for every problem:

```bash
for d in questions/*/; do python "$d/test_solutions.py" || echo "FAILED: $d"; done
```

(PowerShell equivalent):

```powershell
Get-ChildItem questions -Directory | ForEach-Object { python "$($_.FullName)\test_solutions.py" }
```

Adding a new solution file (e.g. `optimal.py`) to a problem's directory is picked up automatically by that directory's `test_solutions.py` — no changes needed to the test file itself.
