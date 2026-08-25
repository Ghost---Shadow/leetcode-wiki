"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(s) -> str

Multiple longest palindromic substrings can be valid for the same input, so
tests check the *length* against the expected length, plus that the result
actually is a palindromic substring of the input.
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
    (("babad",), 3),   # "bab" or "aba"
    (("cbbd",), 2),    # "bb"
    (("a",), 1),
    (("",), 0),
    (("ac",), 1),
    (("racecar",), 7),
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
