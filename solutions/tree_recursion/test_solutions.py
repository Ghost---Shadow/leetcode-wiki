"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared post_order_fold() /
preorder_serialize() / preorder_deserialize() routines in algorithm.py.
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
    "q085_binary_tree_maximum_path_sum.py": [
        (([1, 2, 3],), 6),
        (([-10, 9, 20, None, None, 15, 7],), 42),
        (([-3],), -3),
        (([2, -1],), 2),
        (([1, -2, -3, 1, 3, -2, None, -1],), 3),
    ],
    "q092_lowest_common_ancestor_of_a_binary_tree.py": [
        (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1), 3),
        (([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4), 5),
        (([1, 2], 1, 2), 1),
    ],
    "q097_serialize_and_deserialize_binary_tree.py": [
        (([1, 2, 3, None, None, 4, 5],), [1, 2, 3, None, None, 4, 5]),
        (([],), []),
        (([1],), [1]),
        (([1, 2],), [1, 2]),
        (([5, 4, 7, 3, None, 2, None, -1, None, 9],), [5, 4, 7, 3, None, 2, None, -1, None, 9]),
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
