"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(operations, arguments) -> list
following the LeetCode-judge replay format, e.g.:
    operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    arguments  = [[], [1], [2], [], [3], []]
"""
import glob
import importlib.util
import os
import sys

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
