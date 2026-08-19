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

## Inverted index

`solutions/` inverts the mapping: each technique directory holds one general algorithm (`algorithm.py`), per-question I/O reshapers (`questions/<id>.py`), and its own `test_solutions.py`. All techniques are instantiations of a single meta-engine in `solutions/_meta/algorithm.py` — see [solutions/README.md](solutions/README.md) for the taxonomy.

```bash
for d in solutions/*/; do [ -f "$d/test_solutions.py" ] && python "$d/test_solutions.py"; done
```

Recompute `solutions/inverted_index.json` with:

```bash
python solutions/build_index.py
```
