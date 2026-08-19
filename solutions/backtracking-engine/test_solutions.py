"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared generate_all() engine in algorithm.py.
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = {
    "040-letter-combinations-of-a-phone-number.py": [
        ((("23",)), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ((("",)), []),
        ((("2",)), ["a", "b", "c"]),
    ],
    "048-generate-parentheses.py": [
        ((3,), ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        ((1,), ["()"]),
    ],
    "074-combination-sum.py": [
        (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
        (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ],
    "078-permutations.py": [
        (([1, 2, 3],), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        (([0, 1],), [[0, 1], [1, 0]]),
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


def normalize(groups):
    return sorted(sorted(g) if isinstance(g, list) else g for g in groups)


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES.get(name, []):
            result = module.solve(*args)
            ok = normalize(result) == normalize(expected)
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
