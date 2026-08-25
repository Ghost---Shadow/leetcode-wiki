"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(s, t) -> str

The minimum window is unique in length for these test cases, so tests check the
result's length plus that it is a substring of s containing all characters of t.
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
from collections import Counter

TEST_CASES = [
    (("ADOBECODEBANC", "ABC"), 4),   # "BANC"
    (("a", "a"), 1),                 # "a"
    (("a", "aa"), 0),                # impossible -> ""
    (("", "a"), 0),
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


def check(s, t, result, expected_len):
    if len(result) != expected_len:
        return False
    if expected_len == 0:
        return result == ""
    if result not in s:
        return False
    need = Counter(t)
    have = Counter(result)
    return all(have[ch] >= cnt for ch, cnt in need.items())


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected_len in TEST_CASES:
            s, t = args
            result = module.solve(s, t)
            ok = check(s, t, result, expected_len)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({s!r}, {t!r}) -> {result!r} (expected length {expected_len})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
