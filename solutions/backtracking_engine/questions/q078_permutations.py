"""Reshaper for questions/q078_permutations.

Converts this question's (nums) -> list[list[int]] I/O into the state shape
the shared generate_all() engine understands, and reshapes the result back.
"""
from .. import algorithm as _algorithm
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
