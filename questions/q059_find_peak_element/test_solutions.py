"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(nums) -> int

Multiple valid peak indices can exist for the same input, so tests verify the
*property* that the returned index is a peak, rather than an exact index.
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
    ([1, 2, 3, 1],),
    ([1, 2, 1, 3, 5, 6, 4],),
    ([1],),
    ([1, 2],),
    ([2, 1],),
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
