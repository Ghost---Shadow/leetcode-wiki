"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared streaming_scan() engine in algorithm.py.
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

from collections import Counter

TEST_CASES = {
    "q005_longest_substring_without_repeating_characters.py": [
        (("abcabcbb",), 3),
        (("bbbbb",), 1),
        (("pwwkew",), 3),
        (("",), 0),
        ((" ",), 1),
        (("dvdf",), 3),
    ],
    "q020_sliding_window_maximum.py": [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (([1], 1), [1]),
        (([1, -1], 1), [1, -1]),
        (([9, 11], 2), [11]),
        (([4, -2], 2), [4]),
    ],
}

# Minimum window substring's answer isn't unique in general, so its cases
# carry the expected length and are checked via `check_min_window` below,
# rather than the exact-equality path used for the other adapters.
MIN_WINDOW_CASES = [
    (("ADOBECODEBANC", "ABC"), 4),   # "BANC"
    (("a", "a"), 1),                 # "a"
    (("a", "aa"), 0),                # impossible -> ""
    (("", "a"), 0),
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


def check_min_window(s, t, result, expected_len):
    if len(result) != expected_len:
        return False
    if expected_len == 0:
        return result == ""
    if result not in s:
        return False
    need = Counter(t)
    have = Counter(result)
    return all(have[ch] >= cnt for ch, cnt in need.items())


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

    min_window_name = "q041_minimum_window_substring.py"
    if min_window_name in modules:
        module = modules[min_window_name]
        for (s, t), expected_len in MIN_WINDOW_CASES:
            result = module.solve(s, t)
            ok = check_min_window(s, t, result, expected_len)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {min_window_name}: solve({s!r}, {t!r}) -> {result!r} (expected length {expected_len})")
            if not ok:
                failures += 1
    else:
        print(f"No question adapter found for {min_window_name}.")
        failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
