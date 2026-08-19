"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(numCourses, prerequisites) -> list[int]
(any valid topological order is acceptable; [] means no valid order exists)
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    ((2, [[1, 0]]), 2, []),
    ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), 4, []),
    ((1, []), 1, []),
    ((2, [[1, 0], [0, 1]]), 0, []),
]


def load_solution_modules():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    modules = {}
    for filepath in sorted(glob.glob(os.path.join(dir_path, "*.py"))):
        name = os.path.basename(filepath)
        if name.startswith("test_"):
            continue
        spec = importlib.util.spec_from_file_location(name[:-3], filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "solve"):
            modules[name] = module
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
