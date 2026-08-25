"""Reshaper for questions/q032_word_ladder.

Converts this question's (begin_word, end_word, word_list) -> int I/O into a
call to the shared multi_source_bfs(): a single seed at step 1, spreading to
every one-letter-different dictionary word reachable from it, one BFS layer
per transformation step.
"""
from .. import algorithm as _algorithm
multi_source_bfs = _algorithm.multi_source_bfs

_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def solve(begin_word, end_word, word_list):
    words = set(word_list)
    if end_word not in words:
        return 0
    if begin_word == end_word:
        return 1

    length = len(begin_word)

    def neighbors(state):
        word, steps = state
        for i in range(length):
            prefix, suffix = word[:i], word[i + 1:]
            for letter in _ALPHABET:
                if letter == word[i]:
                    continue
                candidate = prefix + letter + suffix
                if candidate in words:
                    yield (candidate, steps + 1)

    for word, steps in multi_source_bfs([(begin_word, 1)], neighbors, key=lambda s: s[0]):
        if word == end_word:
            return steps
    return 0
