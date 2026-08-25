"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(operations, arguments) -> list
following the LeetCode-judge replay format, e.g.:
    operations = ["RandomizedSet", "insert", "remove", "insert", "getRandom"]
    arguments  = [[], [1], [2], [2], []]

getRandom() results are nondeterministic, so instead of exact equality we
track the expected *contents* of the set after each deterministic operation
and just assert that any returned getRandom() value is currently a member.
"""
import importlib
import pkgutil
import sys
from pathlib import Path

if __package__ in (None, ""):
    _file = Path(__file__).resolve()
    _repo_root = _file.parents[2]
    sys.path.insert(0, str(_repo_root))
    __package__ = ".".join(_file.parent.relative_to(_repo_root).parts)
    importlib.import_module(__package__)

TEST_CASES = [
    (
        ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
        [[], [1], [2], [2], [], [1], [2], []],
        [None, True, False, True, "RANDOM", True, False, "RANDOM"],
    ),
    (
        ["RandomizedSet", "insert", "insert", "insert", "remove", "getRandom", "insert", "getRandom"],
        [[], [1], [2], [3], [2], [], [4], []],
        [None, True, True, True, True, "RANDOM", True, "RANDOM"],
    ),
]


def load_solution_modules():
    modules = {}
    for info in pkgutil.iter_modules([str(Path(__file__).resolve().parent)]):
        if info.name.startswith("test_") or info.name == "__init__":
            continue
        module = importlib.import_module(f".{info.name}", package=__package__)
        if hasattr(module, "solve"):
            modules[f"{info.name}.py"] = module
    return modules


def check(operations, arguments, results, expected):
    """Validate deterministic ops exactly; validate getRandom() results by
    membership in the current contents of the set at that point."""
    contents = set()
    for op, args, result, exp in zip(operations, arguments, results, expected):
        if op == "RandomizedSet":
            continue
        elif op == "insert":
            (val,) = args
            should_add = val not in contents
            if result != exp:
                return False
            if should_add:
                contents.add(val)
        elif op == "remove":
            (val,) = args
            should_remove = val in contents
            if result != exp:
                return False
            if should_remove:
                contents.discard(val)
        elif op == "getRandom":
            if result not in contents:
                return False
    return True


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for operations, arguments, expected in TEST_CASES:
            result = module.solve(list(operations), [list(a) for a in arguments])
            ok = len(result) == len(expected) and check(operations, arguments, result, expected)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve(...) -> {result} (expected shape {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
