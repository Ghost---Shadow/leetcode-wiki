"""Reshaper for questions/q081_valid_sudoku.

Converts this question's (board) -> bool I/O into a call to the shared
all_groups_unique(): each filled cell is one entry whose group ids are its
row, its column, and its 3x3 box; the board is valid iff no value repeats
within any of those groups.
"""
from .. import algorithm as _algorithm
all_groups_unique = _algorithm.all_groups_unique


def solve(board):
    rows = len(board)
    cols = len(board[0]) if rows else 0

    entries = []
    for r in range(rows):
        for c in range(cols):
            val = board[r][c]
            if val == ".":
                continue
            group_ids = (("row", r), ("col", c), ("box", (r // 3, c // 3)))
            entries.append((val, group_ids))

    return all_groups_unique(entries)
