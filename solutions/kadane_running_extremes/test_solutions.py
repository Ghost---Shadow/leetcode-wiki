"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared running_fold_best() routine in
algorithm.py.
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

TEST_CASES = {
    "q011_maximum_subarray.py": [
        (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
        (([1],), 1),
        (([5, 4, -1, 7, 8],), 23),
        (([-1],), -1),
    ],
    "q098_maximum_product_subarray.py": [
        (([2, 3, -2, 4],), 6),
        (([-2, 0, -1],), 0),
        (([-2, 3, -4],), 24),
        (([-2],), -2),
    ],
    "q006_best_time_to_buy_and_sell_stock.py": [
        (([7, 1, 5, 3, 6, 4],), 5),
        (([7, 6, 4, 3, 1],), 0),
        (([1, 2],), 1),
        (([2, 1],), 0),
        (([],), 0),
    ],
    "q063_best_time_to_buy_and_sell_stock_ii.py": [
        (([7, 1, 5, 3, 6, 4],), 7),
        (([1, 2, 3, 4, 5],), 4),
        (([7, 6, 4, 3, 1],), 0),
        (([],), 0),
        (([1],), 0),
        (([1, 2],), 1),
    ],
    "q071_gas_station.py": [
        (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
        (([2, 3, 4], [3, 4, 3]), -1),
        (([5], [4]), 0),
        (([3, 1, 1], [1, 2, 2]), 0),
    ],
}


def load_question_modules():
    modules = {}
    questions_dir = Path(__file__).resolve().parent / "questions"
    for info in pkgutil.iter_modules([str(questions_dir)]):
        if info.name == "__init__":
            continue
        module = importlib.import_module(f".questions.{info.name}", package=__package__)
        modules[f"{info.name}.py"] = module
    return modules


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES.get(name, []):
            result = module.solve(*args)
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve{args} -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
