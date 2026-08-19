"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared find_cycle_meeting_point() routine in
algorithm.py.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = {
    "080-happy-number.py": [
        ((19,), True),
        ((2,), False),
        ((1,), True),
        ((7,), True),
    ],
    "087-linked-list-cycle.py": [
        (([3, 2, 0, -4], 1), True),
        (([1, 2], 0), True),
        (([1], -1), False),
        (([], -1), False),
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
