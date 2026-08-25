"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared linear_fold() engine in algorithm.py.
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
    "q042_roman_to_integer.py": [
        (("III",), 3),
        (("LVIII",), 58),
        (("MCMXCIV",), 1994),
        (("IV",), 4),
        (("IX",), 9),
    ],
    "q061_integer_to_roman.py": [
        ((3,), "III"),
        ((4,), "IV"),
        ((9,), "IX"),
        ((58,), "LVIII"),
        ((1994,), "MCMXCIV"),
        ((3999,), "MMMCMXCIX"),
    ],
    "q060_palindrome_number.py": [
        ((121,), True),
        ((-121,), False),
        ((10,), False),
        ((0,), True),
        ((1,), True),
        ((12321,), True),
    ],
    "q013_longest_common_prefix.py": [
        ((["flower", "flow", "flight"],), "fl"),
        ((["dog", "racecar", "car"],), ""),
        ((["a"],), "a"),
        ((["ab", "a"],), "a"),
        (([],), ""),
        ((["", "b"],), ""),
    ],
    "q075_reverse_words_in_a_string.py": [
        (("the sky is blue",), "blue is sky the"),
        (("  hello world  ",), "world hello"),
        (("a good   example",), "example good a"),
        (("  Bob    Loves  Alice   ",), "Alice Loves Bob"),
        (("single",), "single"),
    ],
    "q089_first_unique_character_in_a_string.py": [
        (("leetcode",), 0),
        (("loveleetcode",), 2),
        (("aabb",), -1),
        (("",), -1),
        (("z",), 0),
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


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES.get(name, []):
            call_args = tuple(list(a) if isinstance(a, list) else a for a in args)
            result = module.solve(*call_args)
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve{args} -> {result!r} (expected {expected!r})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
