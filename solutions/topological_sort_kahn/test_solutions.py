"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared kahn_topological_order() routine in
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
    "q022_course_schedule.py": [
        ((2, [[1, 0]]), True),
        ((2, [[1, 0], [0, 1]]), False),
        ((1, []), True),
        ((3, [[1, 0], [2, 1]]), True),
    ],
    # (num_courses, prerequisites) -> any valid topological order is
    # acceptable, so these are checked by validity, not exact equality.
    "q047_course_schedule_ii.py": [
        (2, [[1, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        (1, []),
        (2, [[1, 0], [0, 1]]),  # cycle -> expect []
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


def is_valid_order(order, num_courses, prerequisites):
    # Detect whether a cycle exists among prerequisites (reference check).
    graph = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1
    queue = [i for i in range(num_courses) if indegree[i] == 0]
    seen = 0
    while queue:
        node = queue.pop()
        seen += 1
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    has_cycle_expected = seen != num_courses

    if has_cycle_expected:
        return order == []

    if sorted(order) != list(range(num_courses)):
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[pre] < position[course] for course, pre in prerequisites)


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        if name == "q047_course_schedule_ii.py":
            for num_courses, prerequisites in TEST_CASES.get(name, []):
                result = module.solve(num_courses, prerequisites)
                ok = is_valid_order(result, num_courses, prerequisites)
                status = "PASS" if ok else "FAIL"
                print(f"[{status}] {name}: solve({num_courses}, {prerequisites}) -> {result}")
                if not ok:
                    failures += 1
        else:
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
