"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(list1, list2) -> list[int]
where list1/list2 are plain Python lists representing the linked lists
(solution files build/tear down their own ListNode chains internally).
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
    (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    (([], []), []),
    (([], [0]), [0]),
    (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
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
            list1, list2 = args
            result = module.solve(list(list1), list(list2))
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({list1}, {list2}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
