"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(equations, values, queries) -> list[float]
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
    modules = {}
    for info in pkgutil.iter_modules([str(Path(__file__).resolve().parent)]):
        if info.name.startswith("test_") or info.name == "__init__":
            continue
        module = importlib.import_module(f".{info.name}", package=__package__)
        if hasattr(module, "solve"):
            modules[f"{info.name}.py"] = module
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
