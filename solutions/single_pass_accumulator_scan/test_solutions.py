"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared scan() routine in algorithm.py.
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
    "q086_remove_duplicates_from_sorted_array.py": [
        (([1, 1, 2],), [1, 2]),
        (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), [0, 1, 2, 3, 4]),
        (([1],), [1]),
        (([],), []),
        (([1, 1, 1, 1],), [1]),
    ],
    "q053_merge_sorted_array.py": [
        (([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6]),
        (([1], 1, [], 0), [1]),
        (([0], 0, [1], 1), [1]),
    ],
    "q050_product_of_array_except_self.py": [
        (([1, 2, 3, 4],), [24, 12, 8, 6]),
        (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
        (([2, 3],), [3, 2]),
    ],
    "q082_majority_element.py": [
        (([3, 2, 3],), 3),
        (([2, 2, 1, 1, 1, 2, 2],), 2),
        (([1],), 1),
        (([6, 5, 5],), 5),
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
            reshaped_args = [list(a) if isinstance(a, list) else a for a in args]
            result = module.solve(*reshaped_args)
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
