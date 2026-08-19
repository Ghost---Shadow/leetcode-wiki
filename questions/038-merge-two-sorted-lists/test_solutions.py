"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(list1, list2) -> list[int]
where list1/list2 are plain Python lists representing the linked lists
(solution files build/tear down their own ListNode chains internally).
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    (([], []), []),
    (([], [0]), [0]),
    (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
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
            list1, list2 = args
            result = module.solve(list(list1), list(list2))
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({list1}, {list2}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
