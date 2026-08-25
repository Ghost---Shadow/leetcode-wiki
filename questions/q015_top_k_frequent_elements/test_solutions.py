"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(nums, k) -> list[int]

The order of the returned elements does not matter, so tests check the
returned set (and that it has the right size) rather than exact order.
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
from collections import Counter

TEST_CASES = [
    (([1, 1, 1, 2, 2, 3], 2), {1, 2}),
    (([1], 1), {1}),
    (([1, 2], 2), {1, 2}),
    (([4, 4, 4, 6, 6, 7, 7, 7, 7], 1), {7}),
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


def check(nums, k, result, expected_set):
    if len(result) != k:
        return False
    if len(set(result)) != len(result):
        return False
    return set(result) == expected_set


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            nums, k = args
            result = module.solve(list(nums), k)
            ok = check(nums, k, result, expected)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({nums}, {k}) -> {result} (expected set {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
