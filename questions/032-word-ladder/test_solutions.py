"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(begin_word, end_word, word_list) -> int
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    (("a", "c", ["a", "b", "c"]), 2),
    (("hot", "dog", ["hot", "dog"]), 0),
    (("hot", "hot", ["hot"]), 1),
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


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            begin_word, end_word, word_list = args
            result = module.solve(begin_word, end_word, list(word_list))
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({begin_word!r}, {end_word!r}, {word_list}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
