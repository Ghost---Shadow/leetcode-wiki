"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared heap-backed running-state routines in
algorithm.py (TwoHeapMedian, schedule_with_cooldown).
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
    "q023_find_median_from_data_stream.py": [
        (
            (
                ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
                [[], [1], [2], [], [3], []],
            ),
            [None, None, None, 1.5, None, 2.0],
        ),
        (
            (
                ["MedianFinder", "addNum", "findMedian"],
                [[], [5], []],
            ),
            [None, None, 5.0],
        ),
    ],
    "q090_task_scheduler.py": [
        ((["A", "A", "A", "B", "B", "B"], 2), 8),
        ((["A", "A", "A", "B", "B", "B"], 0), 6),
        ((["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2), 16),
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


def check(name, result, expected):
    if name == "q023_find_median_from_data_stream.py":
        if len(result) != len(expected):
            return False
        for got, want in zip(result, expected):
            if want is None:
                if got is not None:
                    return False
            else:
                if got is None or abs(got - want) > 1e-9:
                    return False
        return True
    return result == expected


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES.get(name, []):
            result = module.solve(*args)
            ok = check(name, result, expected)
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
