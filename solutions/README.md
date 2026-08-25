# Inverted index: solution technique -> questions

The forward index (`questions/`) maps each question to its solutions. This
directory inverts it: each technique holds **one** general algorithm plus a
thin reshaper per question that converts that question's I/O into the
algorithm's shape and back.

## Layout

```
solutions/
  __init__.py
  _meta/                      # the meta engine every technique instantiates
    __init__.py
    algorithm.py              #   explore(seeds, transition, order)
    test_solutions.py         #   direct tests of the engine itself
  <technique>/                # valid package name, e.g. backtracking_engine
    __init__.py
    algorithm.py              # one general routine, built on _meta explore()
    questions/
      __init__.py
      q<id>.py                # reshaper: question I/O -> algorithm shape -> back
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

All 100 questions are covered across 28 techniques. Instantiations built
directly on `_meta.explore()`:

| technique | state | discipline | fold |
|---|---|---|---|
| backtracking_engine | (partial solution, is_complete) | LIFO | collect complete payloads |
| topological_sort_kahn | ready node (stateful in-degree release) | FIFO | append in pop order |
| kadane_running_extremes | index, carrying best-ending-here | chain | running max |
| monotonic_stack_next_element | index, carrying a pending stack | chain | resolve dominated indices |
| floyd_cycle_detection | (slow, fast) pointer pair | chain | first meeting pair |
| grid_bfs | grid/graph node | FIFO | layer count / component count |
| heap_priority | arbitrary, ranked by a priority key | priority | drain in best-first order |
| binary_search_on_answer | shrinking (lo, hi) interval | chain | converged bound |
| sliding_window | index, carrying window bookkeeping | chain | emitted-value stream |
| two_pointer_converge | (left, right) pointer pair | chain | values seen while converging |
| linear_fold_scan | item, carrying an accumulator | chain | final accumulator |
| hashmap_lookup | item, carrying a hashmap | chain | early-exit or full table |
| hashmap_indexed_scan | index/seed, carrying running state | chain | running sum / longest chain |
| interval_sweep | sorted item, carrying a fold state | chain | merged intervals / DP table |
| stack_scan_fold | item, carrying an explicit stack | chain | final stack / derived value |
| single_pass_accumulator_scan | item, carrying an accumulator | chain (FIFO) | final accumulator |
| memoized_index_chain | index 0..n, memoized | chain | filled 1-D DP table |
| memoized_two_index_dp | (i, j) in caller-supplied order, memoized | chain | filled 2-D DP table |

Techniques with an honest standalone `algorithm.py` (the shared routine
exists and is real, but doesn't reduce to `explore` — see "known outliers"
below): `design_operation_log`, `greedy_line_packing`,
`grid_constraint_check`, `heap_stream_state`, `inplace_pointer_rewrite`,
`inplace_write_pointer_compaction`, `linked_list_group_reversal`,
`linked_list_pairwise_walk`, `matrix_ring_traversal`, `tree_recursion`.

Known outliers that do **not** reduce naturally to `explore`: data-structure
design / operation-log replay (state persists across calls, not unfolded
from seeds), in-place array/pointer rewriting (sort colors, cyclic sort,
matrix rotation — direct index manipulation, not a graph search), linked-list
pointer surgery, and tree recursion that needs a combine-on-return
("hylomorphism" fold) rather than a linear one. Union-find (state merging)
never ended up needed by any of the 100 questions here.

## Commands

Run one technique's tests:

```bash
python solutions/backtracking_engine/test_solutions.py
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

1. Pick (or create) `solutions/<technique>/` (a package — add `__init__.py`)
   with the general routine in `algorithm.py` — expressed as an
   instantiation of `_meta` `explore()`.
2. Add `questions/q<rank>_<slug>.py` exposing `solve(...)` with the exact
   same signature as that question's files in `questions/q<rank>_<slug>/`,
   reshaping in and out of the general routine.
3. Add its cases to the technique's `test_solutions.py`, run it, then
   rerun `build_index.py`.
