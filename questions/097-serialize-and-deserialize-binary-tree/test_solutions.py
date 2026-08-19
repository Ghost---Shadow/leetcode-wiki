"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(tree_list) -> list
tree_list is a LeetCode-style level-order list (None for missing children);
the result should be an equivalent level-order list (trailing Nones trimmed)
produced by serializing then deserializing the tree.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (([1, 2, 3, None, None, 4, 5],), [1, 2, 3, None, None, 4, 5]),
    (([],), []),
    (([1],), [1]),
    (([1, 2],), [1, 2]),
    (([5, 4, 7, 3, None, 2, None, -1, None, 9],), [5, 4, 7, 3, None, 2, None, -1, None, 9]),
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
            (tree_list,) = args
            result = module.solve(list(tree_list))
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({tree_list}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
