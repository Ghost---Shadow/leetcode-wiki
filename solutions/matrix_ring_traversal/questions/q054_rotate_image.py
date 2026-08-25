"""Reshaper for questions/q054_rotate_image.

Converts this question's (matrix,) -> list[list[int]] I/O into a call to
the shared ring_layers(): rotate each concentric ring 90 degrees clockwise
in place by cycling four elements at a time around the ring's border,
working outermost ring first.
"""
from .. import algorithm as _algorithm
ring_layers = _algorithm.ring_layers


def solve(matrix):
    for top, bottom, left, right in ring_layers(len(matrix), len(matrix[0]) if matrix else 0):
        span = right - left
        for i in range(span):
            temp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = temp

    return matrix
