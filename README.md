# leetcode-wiki
Inverted Index for Leetcode Problems

## Structure

Each problem lives in `questions/q<rank>_<slug>/` (a Python package, e.g. `questions/q001_two_sum/`) and contains:
- `__init__.py` — makes the directory a package
- `questions.txt` — problem metadata (title, difficulty, topics, companies, link)
- One or more solution files (e.g. `brute_force.py`), each exposing a `solve(...)` function
- `test_solutions.py` — discovers and runs every solution file in that same package via `importlib`

## Running tests

Run tests for a single problem (either form works):

```bash
python questions/q001_two_sum/test_solutions.py
python -m questions.q001_two_sum.test_solutions
```

Run tests for every problem:

```bash
for d in questions/*/; do python "$d/test_solutions.py" || echo "FAILED: $d"; done
```

(PowerShell equivalent):

```powershell
Get-ChildItem questions -Directory | ForEach-Object { python "$($_.FullName)\test_solutions.py" }
```

Adding a new solution file (e.g. `optimal.py`) to a problem's package is picked up automatically by that package's `test_solutions.py` — no changes needed to the test file itself.

## Inverted index

`solutions/` inverts the mapping: each technique package holds one general algorithm (`algorithm.py`), per-question I/O reshapers (`questions/q<id>.py`), and its own `test_solutions.py`. All techniques are instantiations of a single meta-engine in `solutions/_meta/algorithm.py` — see [solutions/README.md](solutions/README.md) for the taxonomy.

```bash
for d in solutions/*/; do [ -f "$d/test_solutions.py" ] && python "$d/test_solutions.py"; done
```

Recompute `solutions/inverted_index.json` with:

```bash
python solutions/build_index.py
```

All 100 questions are currently covered by some technique. Track coverage
(and regenerate `solutions/COVERAGE.md`) with:

```bash
python solutions/find_uncovered.py
```
