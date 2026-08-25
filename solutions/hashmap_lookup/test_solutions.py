"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific I/O onto the shared hashmap_pass() routine in
algorithm.py.
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
    "q001_two_sum.py": [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ],
    "q008_group_anagrams.py": [
        (
            (["eat", "tea", "tan", "ate", "nat", "bat"],),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ((([""]),), [[""]]),
        ((["a"],), [["a"]]),
    ],
    "q031_valid_anagram.py": [
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
        (("", ""), True),
        (("a", "ab"), False),
        (("aacc", "ccac"), False),
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


def check_two_sum(nums, target, result, expected):
    if len(result) != 2:
        return False
    i, j = result
    if i == j:
        return False
    if nums[i] + nums[j] != target:
        return False
    return sorted(result) == sorted(expected)


def normalize_groups(groups):
    return sorted(sorted(g) for g in groups)


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES.get(name, []):
            result = module.solve(*[list(a) if isinstance(a, list) else a for a in args])

            if name == "q001_two_sum.py":
                nums, target = args
                ok = check_two_sum(nums, target, result, expected)
            elif name == "q008_group_anagrams.py":
                ok = normalize_groups(result) == normalize_groups(expected)
            else:
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
