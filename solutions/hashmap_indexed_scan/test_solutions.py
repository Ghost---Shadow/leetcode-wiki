"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared hashmap-indexed routines in
algorithm.py (running_fold_sum, longest_chain_from_seeds).
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
    "q024_subarray_sum_equals_k.py": [
        (([1, 1, 1], 2), 2),
        (([1, 2, 3], 3), 2),
        (([1], 0), 0),
        (([1, -1, 0], 0), 3),
        (([], 0), 0),
    ],
    "q029_longest_consecutive_sequence.py": [
        (([100, 4, 200, 1, 3, 2],), 4),
        (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
        (([],), 0),
        (([1, 2, 0, 1],), 3),
        (([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],), 7),
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
