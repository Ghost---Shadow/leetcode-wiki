"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared next_dominant_index() routine in
algorithm.py.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = {
    "065-largest-rectangle-in-histogram.py": [
        (([2, 1, 5, 6, 2, 3],), 10),
        (([2, 4],), 4),
        (([],), 0),
        (([5],), 5),
    ],
    "067-daily-temperatures.py": [
        (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
        (([30, 40, 50, 60],), [1, 1, 1, 0]),
        (([30, 60, 90],), [1, 1, 0]),
    ],
}


def load_question_modules():
    dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions")
    modules = {}
    for filepath in sorted(glob.glob(os.path.join(dir_path, "*.py"))):
        name = os.path.basename(filepath)
        spec = importlib.util.spec_from_file_location(name[:-3], filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules[name] = module
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
