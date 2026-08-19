"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(nums, k) -> list[int]

The order of the returned elements does not matter, so tests check the
returned set (and that it has the right size) rather than exact order.
"""
import glob
import importlib.util
import os
import sys
from collections import Counter

TEST_CASES = [
    (([1, 1, 1, 2, 2, 3], 2), {1, 2}),
    (([1], 1), {1}),
    (([1, 2], 2), {1, 2}),
    (([4, 4, 4, 6, 6, 7, 7, 7, 7], 1), {7}),
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
