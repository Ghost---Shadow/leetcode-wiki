"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared multi_source_bfs()/count_components()
engine in algorithm.py.
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
    "q007_number_of_islands.py": [
        (
            ([
                list("11110"),
                list("11010"),
                list("11000"),
                list("00000"),
            ],),
            1,
        ),
        (
            ([
                list("11000"),
                list("11000"),
                list("00100"),
                list("00011"),
            ],),
            3,
        ),
        (([],), 0),
    ],
    "q014_rotting_oranges.py": [
        (
            ([
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1],
            ],),
            4,
        ),
        (
            ([
                [2, 1, 1],
                [0, 1, 1],
                [1, 0, 1],
            ],),
            -1,
        ),
        (([[0, 2]],), 0),
        (([[0]],), 0),
        (([],), 0),
    ],
    "q032_word_ladder.py": [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
        (("a", "c", ["a", "b", "c"]), 2),
        (("hot", "dog", ["hot", "dog"]), 0),
        (("hot", "hot", ["hot"]), 1),
    ],
    "q093_evaluate_division.py": [
        (
            (
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ),
            [6.0, 0.5, -1.0, 1.0, -1.0],
        ),
        (
            (
                [["a", "b"], ["b", "c"], ["bc", "cd"]],
                [1.5, 2.5, 5.0],
                [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            ),
            [3.75, 0.4, 5.0, 0.2],
        ),
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


def check(result, expected):
    if isinstance(expected, list) and expected and isinstance(expected[0], float):
        return len(result) == len(expected) and all(
            abs(r - e) < 1e-4 for r, e in zip(result, expected)
        )
    return result == expected


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES.get(name, []):
            if name == "q007_number_of_islands.py":
                (grid,) = args
                result = module.solve([row[:] for row in grid])
            elif name == "q014_rotting_oranges.py":
                (grid,) = args
                result = module.solve([row[:] for row in grid])
            elif name == "q093_evaluate_division.py":
                equations, values, queries = args
                result = module.solve(
                    [list(e) for e in equations], list(values), [list(q) for q in queries]
                )
            else:
                result = module.solve(*args)
            ok = check(result, expected)
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
