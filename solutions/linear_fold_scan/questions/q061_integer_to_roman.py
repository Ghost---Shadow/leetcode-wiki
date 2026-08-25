"""Reshaper for questions/q061_integer_to_roman.

Converts this question's (num) -> str I/O into a call to the shared
linear_fold(): folds over the fixed value/symbol table, greedily
consuming as many of each value as fit into the amount remaining.
"""
from .. import algorithm as _algorithm
linear_fold = _algorithm.linear_fold

TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def solve(num):
    def step(state, entry):
        remaining, symbols = state
        val, sym = entry
        if remaining <= 0:
            return state
        count, remaining = divmod(remaining, val)
        if count:
            symbols = symbols + [sym * count]
        return remaining, symbols

    _, symbols = linear_fold(TABLE, (num, []), step)
    return "".join(symbols)
