"""Reshaper for questions/078-permutations.

Converts this question's (nums) -> list[list[int]] I/O into the state shape
the shared generate_all() engine understands, and reshapes the result back.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
generate_all = _algorithm.generate_all


def solve(nums):
    if not nums:
        return [[]]

    def expand(state):
        remaining, path = state
        options = []
        for i in range(len(remaining)):
            new_remaining = remaining[:i] + remaining[i + 1:]
            new_path = path + (remaining[i],)
            options.append(((new_remaining, new_path), len(new_remaining) == 0))
        return options

    results = generate_all((tuple(nums), ()), expand)
    return [list(path) for _, path in results]
