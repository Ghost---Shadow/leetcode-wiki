"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared converge() engine in algorithm.py.
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
    "q012_container_with_most_water.py": [
        (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        (([1, 1],), 1),
        (([4, 3, 2, 1, 4],), 16),
        (([1, 2, 1],), 2),
    ],
    "q010_trapping_rain_water.py": [
        (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
        (([4, 2, 0, 3, 2, 5],), 9),
        (([],), 0),
        (([1, 1, 1],), 0),
        (([5, 4, 1, 2],), 1),
    ],
    "q016_3sum.py": [
        (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
        (([0, 1, 1],), []),
        (([0, 0, 0],), [[0, 0, 0]]),
        (([],), []),
        (([0, 0, 0, 0],), [[0, 0, 0]]),
    ],
    "q037_valid_palindrome.py": [
        (("A man, a plan, a canal: Panama",), True),
        (("race a car",), False),
        (("",), True),
        ((" ",), True),
        ((".,",), True),
        (("0P",), False),
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


def normalize(triplets):
    return sorted(sorted(t) for t in triplets)


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES.get(name, []):
            # q012/q010 take a list that some adapters mutate/consume;
            # q016 sorts internally too. Pass a fresh copy each time.
            call_args = tuple(list(a) if isinstance(a, list) else a for a in args)
            result = module.solve(*call_args)
            if name == "q016_3sum.py":
                ok = normalize(result) == normalize(expected)
            else:
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
