"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(board) -> bool
where board is a 9x9 list of lists of single-character strings ('1'-'9' or '.').
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

VALID_BOARD = [
    list("53..7...."),
    list("6..195..."),
    list(".98....6."),
    list("8...6...3"),
    list("4..8.3..1"),
    list("7...2...6"),
    list(".6....28."),
    list("...419..5"),
    list("....8..79"),
]
# fix row lengths to 9 (the strings above are already length 9)
VALID_BOARD = [row[:9] for row in VALID_BOARD]

INVALID_BOARD = [
    list("83..7...."),
    list("6..195..."),
    list(".98....6."),
    list("8...6...3"),
    list("4..8.3..1"),
    list("7...2...6"),
    list(".6....28."),
    list("...419..5"),
    list("....8..79"),
]
INVALID_BOARD = [row[:9] for row in INVALID_BOARD]

TEST_CASES = [
    ((VALID_BOARD,), True),
    ((INVALID_BOARD,), False),
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
            (board,) = args
            board_copy = [row[:] for row in board]
            result = module.solve(board_copy)
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve(board) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
