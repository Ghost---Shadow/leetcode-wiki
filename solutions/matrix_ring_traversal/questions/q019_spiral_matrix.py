"""Reshaper for questions/q019_spiral_matrix.

Converts this question's (matrix,) -> list[int] I/O into a call to the
shared ring_layers(): walk each ring outermost-first and append its top
row, right column, (if more than one row) bottom row, and (if more than
one column) left column, in that order.
"""
from .. import algorithm as _algorithm
ring_layers = _algorithm.ring_layers


def solve(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []

    for top, bottom, left, right in ring_layers(rows, cols):
        for c in range(left, right + 1):
            result.append(matrix[top][c])

        for r in range(top + 1, bottom + 1):
            result.append(matrix[r][right])

        if top < bottom:
            for c in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][c])

        if left < right:
            bottom_for_left = bottom - 1 if top < bottom else bottom
            for r in range(bottom_for_left, top, -1):
                result.append(matrix[r][left])

    return result
