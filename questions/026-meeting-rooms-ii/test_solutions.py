"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(intervals) -> int
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (([[0, 30], [5, 10], [15, 20]],), 2),
    (([[7, 10], [2, 4]],), 1),
    (([],), 0),
    (([[1, 5]],), 1),
    (([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]],), 4),
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
            (intervals,) = args
            result = module.solve([list(iv) for iv in intervals])
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({intervals}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
