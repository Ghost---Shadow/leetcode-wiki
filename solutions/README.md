# Inverted index: solution technique -> questions

The forward index (`questions/`) maps each question to its solutions. This
directory inverts it: each technique holds **one** general algorithm plus a
thin reshaper per question that converts that question's I/O into the
algorithm's shape and back.

## Layout

```
solutions/
  _meta/                      # the meta engine every technique instantiates
    algorithm.py              #   explore(seeds, transition, order)
    test_solutions.py         #   direct tests of the engine itself
  <technique>/
    algorithm.py              # one general routine, built on _meta explore()
    questions/<id>.py         # reshaper: question I/O -> algorithm shape -> back
    test_solutions.py         # runs every reshaper against real test cases
  build_index.py              # scans this tree -> inverted_index.json
  inverted_index.json         # the computed index (generated, don't hand-edit)
```

## The meta-algorithm

Every technique in this tree is the same program:

```
answer = fold(explore(seeds, transition, order))
```

`explore` (in `_meta/algorithm.py`) lazily **unfolds** an implicit state
graph: pop a state from the frontier, yield it, push its successors. The
caller **folds** the stream of yielded states into the answer. (In
recursion-scheme terms: explore is the anamorphism, the fold is the
catamorphism, and a full solution is their composition — a hylomorphism.)

A technique is a choice of four knobs:

| knob | choices |
|---|---|
| state shape | index, partial solution, (slow, fast) pair, graph node, interval, window, ... |
| frontier discipline | LIFO = depth-first, FIFO = breadth-first, priority = best-first; a single-successor transition degenerates into a plain fold/iteration |
| transition | the branching rules; owns pruning, dedup and **memoization** (explore keeps no visited set on purpose) |
| fold | collect / running max / first-hit / append-in-order |

Current instantiations:

| technique | state | discipline | fold |
|---|---|---|---|
| backtracking-engine | (partial solution, is_complete) | LIFO | collect complete payloads |
| topological-sort-kahn | ready node (stateful in-degree release) | FIFO | append in pop order |
| kadane-running-extremes | index, carrying best-ending-here | chain | running max |
| monotonic-stack-next-element | index, carrying a pending stack | chain | resolve dominated indices |
| floyd-cycle-detection | (slow, fast) pointer pair | chain | first meeting pair |

Families that slot straight in as more techniques get added:

- **sliding window / two pointers / binary-search-on-answer** — chains whose
  state is a window or a shrinking interval;
- **grid/word BFS** (rotting oranges, word ladder, shortest paths) — FIFO;
- **heap problems** (merge k lists, top-k, meeting rooms) — the `priority`
  discipline, already implemented in the engine and waiting;
- **memoized DP** — same graphs as the brute forces, but the transition
  deduplicates states. The difference between a question's
  `brute_force.py` and `optimal.py` is very often *only* this knob: same
  state shape, same fold, smarter transition.

Known outliers that do **not** reduce naturally: union-find (state merging
rather than traversal), in-place partitioning (sort colors), and the
"combine" half of divide-and-conquer (needs a tree-shaped fold, not a
linear one).

## Commands

Run one technique's tests:

```bash
python solutions/backtracking-engine/test_solutions.py
```

Run everything in this tree (the engine's own tests included):

```bash
for d in solutions/*/; do [ -f "$d/test_solutions.py" ] && python "$d/test_solutions.py"; done
```

Recompute the index after adding a technique or reshaper:

```bash
python solutions/build_index.py
```

## Adding a question to the index

1. Pick (or create) `solutions/<technique>/` with the general routine in
   `algorithm.py` — expressed as an instantiation of `_meta` `explore()`.
2. Add `questions/<rank>-<slug>.py` exposing `solve(...)` with the exact
   same signature as that question's files in `questions/<rank>-<slug>/`,
   reshaping in and out of the general routine.
3. Add its cases to the technique's `test_solutions.py`, run it, then
   rerun `build_index.py`.
