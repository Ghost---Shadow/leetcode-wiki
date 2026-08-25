"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared scan_compact() engine in algorithm.py.
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
    "q030_move_zeroes.py": [
        (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
        (([0],), [0]),
        (([1, 2, 3],), [1, 2, 3]),
        (([0, 0, 1],), [1, 0, 0]),
        (([],), []),
    ],
}

# String Compression mutates `chars` in place and returns the new length;
# handled separately below since the result also needs to check the
# mutated prefix of the list, mirroring questions/q035.../test_solutions.py.
STRING_COMPRESSION_CASES = [
    ((["a", "a", "b", "b", "c", "c", "c"],), 6, ["a", "2", "b", "2", "c", "3"]),
    ((["a"],), 1, ["a"]),
    ((["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],), 4, ["a", "b", "1", "2"]),
    ((["a", "a", "a", "b", "b", "a", "a"],), 6, ["a", "3", "b", "2", "a", "2"]),
]


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
            (nums,) = args
            result = module.solve(list(nums))
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({nums}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    compress_name = "q035_string_compression.py"
    if compress_name in modules:
        module = modules[compress_name]
        for args, expected_len, expected_chars in STRING_COMPRESSION_CASES:
            (chars,) = args
            chars_copy = list(chars)
            result_len = module.solve(chars_copy)
            result_chars = chars_copy[:result_len]
            ok = result_len == expected_len and result_chars == expected_chars
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {compress_name}: solve({chars}) -> ({result_len}, {result_chars}) (expected ({expected_len}, {expected_chars}))")
            if not ok:
                failures += 1
    else:
        print(f"No question adapter found for {compress_name}.")
        failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
