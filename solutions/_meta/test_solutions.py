"""Direct tests for the _meta explore() engine itself (frontier disciplines
and the degenerate single-successor chain), independent of any question.
"""
import importlib.util
import os
import sys

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("meta_algorithm", os.path.join(_here, "algorithm.py"))
_meta = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_meta)
explore = _meta.explore

CHILDREN = {0: [1, 2], 1: [3, 4], 2: [5, 6]}


def tree_transition(n):
    return CHILDREN.get(n, [])


def run():
    failures = 0

    def check(name, actual, expected):
        nonlocal failures
        ok = actual == expected
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {actual} (expected {expected})")
        if not ok:
            failures += 1

    check(
        "lifo is depth-first",
        list(explore([0], tree_transition, order="lifo")),
        [0, 2, 6, 5, 1, 4, 3],
    )
    check(
        "fifo is breadth-first",
        list(explore([0], tree_transition, order="fifo")),
        [0, 1, 2, 3, 4, 5, 6],
    )
    check(
        "priority is best-first",
        list(explore(
            [10],
            lambda n: [7, 12, 3] if n == 10 else [],
            order="priority",
            priority=lambda s: s,
        )),
        [10, 3, 7, 12],
    )
    check(
        "single-successor chain is a fold",
        list(explore([0], lambda i: [i + 1] if i < 4 else [])),
        [0, 1, 2, 3, 4],
    )

    try:
        list(explore([0], tree_transition, order="bogus"))
        check("unknown order raises", "no error", "ValueError")
    except ValueError:
        check("unknown order raises", "ValueError", "ValueError")

    try:
        list(explore([0], tree_transition, order="priority"))
        check("priority requires a key", "no error", "ValueError")
    except ValueError:
        check("priority requires a key", "ValueError", "ValueError")

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
