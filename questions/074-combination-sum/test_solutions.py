"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(candidates, target) -> list[list[int]]
(order of combinations and order within each combination does not matter)
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
    (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    (([2], 1), []),
    (([1], 1), [[1]]),
    (([1], 2), [[1, 1]]),
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


def normalize(combos):
    return sorted(sorted(c) for c in combos)


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            candidates, target = args
            result = module.solve(list(candidates), target)
            ok = normalize(result) == normalize(expected)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({candidates}, {target}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
