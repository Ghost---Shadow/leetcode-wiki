"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(matrix) -> int
where matrix is a list of lists of single-character strings ('0' or '1').
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
        ([
            list("10100"),
            list("10111"),
            list("11111"),
            list("10010"),
        ],),
        4,
    ),
    (
        ([
            list("01"),
            list("10"),
        ],),
        1,
    ),
    ((
        [list("0")],
    ), 0),
    (([],), 0),
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
        for args, expected in TEST_CASES:
            (matrix,) = args
            matrix_copy = [row[:] for row in matrix]
            result = module.solve(matrix_copy)
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve(matrix) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
