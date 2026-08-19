"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(nums, target) -> list[int]
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
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


def check(nums, target, result, expected):
    if len(result) != 2:
        return False
    i, j = result
    if i == j:
        return False
    if nums[i] + nums[j] != target:
        return False
    return sorted(result) == sorted(expected)


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            nums, target = args
            result = module.solve(list(nums), target)
            ok = check(nums, target, result, expected)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({nums}, {target}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
