"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(s) -> str

Multiple longest palindromic substrings can be valid for the same input, so
tests check the *length* against the expected length, plus that the result
actually is a palindromic substring of the input.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (("babad",), 3),   # "bab" or "aba"
    (("cbbd",), 2),    # "bb"
    (("a",), 1),
    (("",), 0),
    (("ac",), 1),
    (("racecar",), 7),
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


def check(s, result, expected_len):
    if len(result) != expected_len:
        return False
    if result != result[::-1]:
        return False
    return result in s


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected_len in TEST_CASES:
            (s,) = args
            result = module.solve(s)
            ok = check(s, result, expected_len)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({s!r}) -> {result!r} (expected length {expected_len})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
