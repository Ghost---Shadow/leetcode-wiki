"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared grid_dp() routine in algorithm.py.
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
    "q088_edit_distance.py": [
        (("horse", "ros"), 3),
        (("intention", "execution"), 5),
        (("", ""), 0),
        (("a", ""), 1),
        (("", "a"), 1),
        (("abc", "abc"), 0),
    ],
    "q072_maximal_square.py": [
        (([
            list("10100"),
            list("10111"),
            list("11111"),
            list("10010"),
        ],), 4),
        (([
            list("01"),
            list("10"),
        ],), 1),
        (([list("0")],), 0),
        (([],), 0),
    ],
    "q094_regular_expression_matching.py": [
        (("aa", "a"), False),
        (("aa", "a*"), True),
        (("ab", ".*"), True),
        (("aab", "c*a*b"), True),
        (("mississippi", "mis*is*p*."), False),
        (("", ""), True),
        (("", "a*"), True),
    ],
    "q077_palindromic_substrings.py": [
        (("abc",), 3),
        (("aaa",), 6),
        (("",), 0),
        (("a",), 1),
        (("racecar",), 10),
    ],
}

# q009_longest_palindromic_substring.py returns any valid longest
# palindromic substring, so it's checked by length/validity below instead
# of exact equality.
PALINDROME_LENGTH_CASES = [
    (("babad",), 3),
    (("cbbd",), 2),
    (("a",), 1),
    (("",), 0),
    (("ac",), 1),
    (("racecar",), 7),
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


def check_palindrome(s, result, expected_len):
    if len(result) != expected_len:
        return False
    if result != result[::-1]:
        return False
    return result in s


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        if name == "q009_longest_palindromic_substring.py":
            for args, expected_len in PALINDROME_LENGTH_CASES:
                (s,) = args
                result = module.solve(s)
                ok = check_palindrome(s, result, expected_len)
                status = "PASS" if ok else "FAIL"
                print(f"[{status}] {name}: solve({s!r}) -> {result!r} (expected length {expected_len})")
                if not ok:
                    failures += 1
        else:
            for args, expected in TEST_CASES.get(name, []):
                if name == "q072_maximal_square.py":
                    (matrix,) = args
                    args = ([row[:] for row in matrix],)
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
