"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(operations, arguments) -> list
following the LeetCode-judge replay format, e.g.:
    operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    arguments  = [[], [1], [2], [], [3], []]
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
        (
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []],
        ),
        [None, None, None, 1.5, None, 2.0],
    ),
    (
        (
            ["MedianFinder", "addNum", "findMedian"],
            [[], [5], []],
        ),
        [None, None, 5.0],
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


def check(result, expected):
    if len(result) != len(expected):
        return False
    for got, want in zip(result, expected):
        if want is None:
            if got is not None:
                return False
        else:
            if got is None or abs(got - want) > 1e-9:
                return False
    return True


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            operations, arguments = args
            result = module.solve(list(operations), [list(a) for a in arguments])
            ok = check(result, expected)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve(...) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
