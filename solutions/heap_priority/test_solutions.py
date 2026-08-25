"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared priority_pop_stream() routine in
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
    "q017_merge_k_sorted_lists.py": [
        (([[1, 4, 5], [1, 3, 4], [2, 6]],), [1, 1, 2, 3, 4, 4, 5, 6]),
        (([],), []),
        (([[]],), []),
        (([[1], [], [0]],), [0, 1]),
    ],
    # Top K Frequent Elements: order among the k returned elements does not
    # matter, so this is checked by set equality (+ size), not exact equality.
    "q015_top_k_frequent_elements.py": [
        ((([1, 1, 1, 2, 2, 3], 2)), {1, 2}),
        (([1], 1), {1}),
        (([1, 2], 2), {1, 2}),
        (([4, 4, 4, 6, 6, 7, 7, 7, 7], 1), {7}),
    ],
    "q027_kth_largest_element_in_an_array.py": [
        (([3, 2, 1, 5, 6, 4], 2), 5),
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
        (([1], 1), 1),
        (([2, 1], 2), 1),
        (([7, 6, 5, 4, 3, 2, 1], 1), 7),
    ],
    "q026_meeting_rooms_ii.py": [
        (([[0, 30], [5, 10], [15, 20]],), 2),
        (([[7, 10], [2, 4]],), 1),
        (([],), 0),
        (([[1, 5]],), 1),
        (([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]],), 4),
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
    if name == "q015_top_k_frequent_elements.py":
        k = len(expected)
        return len(result) == k and len(set(result)) == len(result) and set(result) == expected
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
            print(f"[{status}] {name}: solve{args} -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
