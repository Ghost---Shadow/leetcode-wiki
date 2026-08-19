"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(operations, arguments) -> list
following the LeetCode-judge replay format, e.g.:
    operations = ["RandomizedSet", "insert", "remove", "insert", "getRandom"]
    arguments  = [[], [1], [2], [2], []]

getRandom() results are nondeterministic, so instead of exact equality we
track the expected *contents* of the set after each deterministic operation
and just assert that any returned getRandom() value is currently a member.
"""
import glob
import importlib.util
import os
import sys

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
    dir_path = os.path.dirname(os.path.abspath(__file__))
    modules = {}
    for filepath in sorted(glob.glob(os.path.join(dir_path, "*.py"))):
        name = os.path.basename(filepath)
        if name.startswith("test_"):
            continue
        spec = importlib.util.spec_from_file_location(name[:-3], filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "solve"):
            modules[name] = module
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
