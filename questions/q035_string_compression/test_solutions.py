"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(chars) -> int
where chars is a list of single characters, modified in place to the
compressed form; the returned int is the new length.
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
    ((["a", "a", "b", "b", "c", "c", "c"],), 6, ["a", "2", "b", "2", "c", "3"]),
    ((["a"],), 1, ["a"]),
    ((["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],), 4, ["a", "b", "1", "2"]),
    ((["a", "a", "a", "b", "b", "a", "a"],), 6, ["a", "3", "b", "2", "a", "2"]),
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
