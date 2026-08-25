"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(numCourses, prerequisites) -> list[int]
(any valid topological order is acceptable; [] means no valid order exists)
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
    ((2, [[1, 0]]), 2, []),
    ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), 4, []),
    ((1, []), 1, []),
    ((2, [[1, 0], [0, 1]]), 0, []),
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


def check(num_courses, prerequisites, result, expected_len):
    if expected_len == 0:
        return result == []
    if sorted(result) != list(range(num_courses)):
        return False
    position = {course: i for i, course in enumerate(result)}
    for course, pre in prerequisites:
        if position[pre] > position[course]:
            return False
    return True


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected_len, _ in TEST_CASES:
            num_courses, prerequisites = args
            result = module.solve(num_courses, [list(p) for p in prerequisites])
            ok = check(num_courses, prerequisites, result, expected_len)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({num_courses}, {prerequisites}) -> {result}")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
