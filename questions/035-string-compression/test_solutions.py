"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(chars) -> int
where chars is a list of single characters, modified in place to the
compressed form; the returned int is the new length.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    ((["a", "a", "b", "b", "c", "c", "c"],), 6, ["a", "2", "b", "2", "c", "3"]),
    ((["a"],), 1, ["a"]),
    ((["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],), 4, ["a", "b", "1", "2"]),
    ((["a", "a", "a", "b", "b", "a", "a"],), 6, ["a", "3", "b", "2", "a", "2"]),
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
        for args, expected_len, expected_chars in TEST_CASES:
            (chars,) = args
            chars_copy = list(chars)
            result_len = module.solve(chars_copy)
            result_chars = chars_copy[:result_len]
            ok = result_len == expected_len and result_chars == expected_chars
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({chars}) -> ({result_len}, {result_chars}) (expected ({expected_len}, {expected_chars}))")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
