"""Reshaper for questions/040-letter-combinations-of-a-phone-number.

Converts this question's (digits) -> list[str] I/O into the state shape the
shared generate_all() engine understands, and reshapes the result back.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
generate_all = _algorithm.generate_all

DIGIT_MAP = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}


def solve(digits):
    if not digits:
        return []

    def expand(state):
        combo, idx = state
        letters = DIGIT_MAP[digits[idx]]
        is_complete = idx + 1 == len(digits)
        return [((combo + ch, idx + 1), is_complete) for ch in letters]

    results = generate_all(("", 0), expand)
    return [combo for combo, _ in results]
