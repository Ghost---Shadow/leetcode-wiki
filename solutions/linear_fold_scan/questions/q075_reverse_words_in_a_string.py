"""Reshaper for questions/q075_reverse_words_in_a_string.

Converts this question's (s) -> str I/O into a call to the shared
linear_fold(): folds over the whitespace-split words, prepending each to
the accumulator -- a left fold with cons-to-front reverses the sequence.
"""
from .. import algorithm as _algorithm
linear_fold = _algorithm.linear_fold


def solve(s):
    words = s.split()

    def step(acc, word):
        return [word] + acc

    reversed_words = linear_fold(words, [], step)
    return " ".join(reversed_words)
