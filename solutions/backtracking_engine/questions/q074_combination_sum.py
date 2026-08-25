"""Reshaper for questions/q074_combination_sum.

Converts this question's (candidates, target) -> list[list[int]] I/O into
the state shape the shared generate_all() engine understands, and reshapes
the result back.
"""
from .. import algorithm as _algorithm
generate_all = _algorithm.generate_all


def solve(candidates, target):
    candidates = sorted(candidates)

    def expand(state):
        start, remaining, path = state
        options = []
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break
            new_remaining = remaining - c
            new_path = path + (c,)
            options.append(((i, new_remaining, new_path), new_remaining == 0))
        return options

    results = generate_all((0, target, ()), expand)
    return [list(path) for _, _, path in results]
