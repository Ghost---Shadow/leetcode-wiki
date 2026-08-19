"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(equations, values, queries) -> list[float]
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        ),
        [6.0, 0.5, -1.0, 1.0, -1.0],
    ),
    (
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        ),
        [3.75, 0.4, 5.0, 0.2],
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
    return all(abs(r - e) < 1e-4 for r, e in zip(result, expected))


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            equations, values, queries = args
            result = module.solve(
                [list(e) for e in equations], list(values), [list(q) for q in queries]
            )
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
