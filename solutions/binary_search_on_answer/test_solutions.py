"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared binary_search_converge() routine in
algorithm.py.
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

TEST_CASES = {
    "q018_search_in_rotated_sorted_array.py": [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 0), -1),
        (([1], 1), 0),
        (([5, 1, 3], 5), 0),
        (([], 5), -1),
    ],
    "q021_median_of_two_sorted_arrays.py": [
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5),
        (([], [1]), 1.0),
        (([2], []), 2.0),
        (([0, 0], [0, 0]), 0.0),
    ],
    "q025_koko_eating_bananas.py": [
        (([3, 6, 7, 11], 8), 4),
        (([30, 11, 23, 4, 20], 5), 30),
        (([30, 11, 23, 4, 20], 6), 23),
        (([1], 1), 1),
        (([312884470], 968709470), 1),
    ],
    "q064_find_first_and_last_position_of_element_in_sorted_array.py": [
        (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
        (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
        (([], 0), [-1, -1]),
        (([1], 1), [0, 0]),
        (([2, 2, 2, 2], 2), [0, 3]),
    ],
    # find_peak_element: multiple valid peak indices can exist for the same
    # input, so this is checked by validity below, not exact equality.
    "q059_find_peak_element.py": [
        ([1, 2, 3, 1],),
        ([1, 2, 1, 3, 5, 6, 4],),
        ([1],),
        ([1, 2],),
        ([2, 1],),
    ],
}


def load_question_modules():
    modules = {}
    questions_dir = Path(__file__).resolve().parent / "questions"
    for info in pkgutil.iter_modules([str(questions_dir)]):
        if info.name == "__init__":
            continue
        module = importlib.import_module(f".questions.{info.name}", package=__package__)
        modules[f"{info.name}.py"] = module
    return modules


def is_peak(nums, result):
    n = len(nums)
    if result < 0 or result >= n:
        return False
    left = nums[result - 1] if result - 1 >= 0 else float("-inf")
    right = nums[result + 1] if result + 1 < n else float("-inf")
    return nums[result] > left and nums[result] > right


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        if name == "q059_find_peak_element.py":
            for args in TEST_CASES.get(name, []):
                (nums,) = args
                result = module.solve(list(nums))
                ok = is_peak(nums, result)
                status = "PASS" if ok else "FAIL"
                print(f"[{status}] {name}: solve({nums}) -> {result}")
                if not ok:
                    failures += 1
        elif name == "q021_median_of_two_sorted_arrays.py":
            for args, expected in TEST_CASES.get(name, []):
                nums1, nums2 = args
                result = module.solve(list(nums1), list(nums2))
                ok = abs(result - expected) < 1e-9
                status = "PASS" if ok else "FAIL"
                print(f"[{status}] {name}: solve({nums1}, {nums2}) -> {result} (expected {expected})")
                if not ok:
                    failures += 1
        else:
            for args, expected in TEST_CASES.get(name, []):
                result = module.solve(*[list(a) if isinstance(a, list) else a for a in args])
                ok = result == expected
                status = "PASS" if ok else "FAIL"
                print(f"[{status}] {name}: solve{args} -> {result} (expected {expected})")
                if not ok:
                    failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
