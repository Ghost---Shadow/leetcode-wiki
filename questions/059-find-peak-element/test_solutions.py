"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(nums) -> int

Multiple valid peak indices can exist for the same input, so tests verify the
*property* that the returned index is a peak, rather than an exact index.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    ([1, 2, 3, 1],),
    ([1, 2, 1, 3, 5, 6, 4],),
    ([1],),
    ([1, 2],),
    ([2, 1],),
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


def check(nums, result):
    n = len(nums)
    if result < 0 or result >= n:
        return False
    left = nums[result - 1] if result - 1 >= 0 else float("-inf")
    right = nums[result + 1] if result + 1 < n else float("-inf")
    return nums[result] > left and nums[result] > right


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args in TEST_CASES:
            (nums,) = args
            result = module.solve(list(nums))
            ok = check(nums, result)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({nums}) -> {result}")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
