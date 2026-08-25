"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared stack_scan() routine in algorithm.py.
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
    "q004_valid_parentheses.py": [
        (("()",), True),
        (("()[]{}",), True),
        (("(]",), False),
        (("([)]",), False),
        (("{[]}",), True),
        (("",), True),
        ((")",), False),
    ],
    "q028_decode_string.py": [
        (("3[a]2[bc]",), "aaabcbc"),
        (("3[a2[c]]",), "accaccacc"),
        (("2[abc]3[cd]ef",), "abcabccdcdcdef"),
        (("abc",), "abc"),
        (("2[a]",), "aa"),
    ],
    "q095_simplify_path.py": [
        (("/home/",), "/home"),
        (("/../",), "/"),
        (("/home//foo/",), "/home/foo"),
        (("/a/./b/../../c/",), "/c"),
        (("/a/../../b/../c//.//",), "/c"),
        (("/a//b////c/d//././/..",), "/a/b/c"),
    ],
    "q051_asteroid_collision.py": [
        (([5, 10, -5],), [5, 10]),
        (([8, -8],), []),
        (([10, 2, -5],), [10]),
        (([-2, -1, 1, 2],), [-2, -1, 1, 2]),
    ],
    "q069_basic_calculator_ii.py": [
        (("3+2*2",), 7),
        ((" 3/2 ",), 1),
        ((" 3+5 / 2 ",), 5),
        (("1",), 1),
        (("14-3/2",), 13),
        (("0*2",), 0),
    ],
    "q100_basic_calculator.py": [
        (("1 + 1",), 2),
        ((" 2-1 + 2 ",), 3),
        (("(1+(4+5+2)-3)+(6+8)",), 23),
        (("2-(5-6)",), 3),
        (("(7)-(0)+(4)",), 11),
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
            result = module.solve(*args)
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
