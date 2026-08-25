"""Reshaper for questions/q046_text_justification.

Converts this question's (words, maxWidth) -> list[str] I/O into a call to
the shared justify_lines(): this question *is* the general routine (greedy
line packing + padding), so the reshaper is a pure pass-through.
"""
from .. import algorithm as _algorithm
justify_lines = _algorithm.justify_lines


def solve(words, maxWidth):
    return justify_lines(words, maxWidth)
