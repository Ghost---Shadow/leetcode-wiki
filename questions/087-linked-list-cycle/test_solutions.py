"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(values, pos) -> bool
values is the list node values in order; pos is the 0-indexed position the
tail connects back to (or -1 for no cycle), matching LeetCode's own params.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (([3, 2, 0, -4], 1), True),
    (([1, 2], 0), True),
    (([1], -1), False),
    (([], -1), False),
    (([1, 2, 3, 4, 5], -1), False),
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


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            values, pos = args
            result = module.solve(list(values), pos)
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({values}, {pos}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
