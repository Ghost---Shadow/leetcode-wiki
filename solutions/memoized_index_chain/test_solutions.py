"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared chain_dp() routine in algorithm.py.
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
    "q049_climbing_stairs.py": [
        ((1,), 1),
        ((2,), 2),
        ((3,), 3),
        ((5,), 8),
    ],
    "q043_house_robber.py": [
        (([1, 2, 3, 1],), 4),
        (([2, 7, 9, 3, 1],), 12),
        (([],), 0),
        (([5],), 5),
        (([2, 1, 1, 2],), 4),
    ],
    "q033_coin_change.py": [
        (([1, 2, 5], 11), 3),
        (([2], 3), -1),
        (([1], 0), 0),
        (([1], 1), 1),
        (([2, 5, 10], 12), 2),
    ],
    "q066_longest_increasing_subsequence.py": [
        (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
        (([0, 1, 0, 3, 2, 3],), 4),
        (([7, 7, 7, 7, 7, 7, 7],), 1),
        (([],), 0),
        (([1],), 1),
        (([4, 10, 4, 3, 8, 9],), 3),
    ],
    "q056_jump_game.py": [
        (([2, 3, 1, 1, 4],), True),
        (([3, 2, 1, 0, 4],), False),
        (([0],), True),
        (([1, 0, 1, 0],), False),
        (([2, 0, 0],), True),
    ],
    "q079_jump_game_ii.py": [
        (([2, 3, 1, 1, 4],), 2),
        (([2, 3, 0, 1, 4],), 2),
        (([0],), 0),
        (([1, 1, 1, 1],), 3),
        (([1, 2],), 1),
    ],
    "q068_word_break.py": [
        (("leetcode", ["leet", "code"]), True),
        (("applepenapple", ["apple", "pen"]), True),
        (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
        (("", ["a"]), True),
        (("a", ["b"]), False),
        (("aaaaaaa", ["aaaa", "aaa"]), True),
    ],
    "q076_longest_valid_parentheses.py": [
        (("(()",), 2),
        ((")()())",), 4),
        (("",), 0),
        (("()(()",), 2),
        (("()(())",), 6),
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
            print(f"[{status}] {name}: solve{args} -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
