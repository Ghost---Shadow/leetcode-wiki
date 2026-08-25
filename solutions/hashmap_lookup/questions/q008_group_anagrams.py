"""Reshaper for questions/q008_group_anagrams.

Converts this question's strs -> list[list[str]] I/O into a call to the
shared hashmap_pass(): the table maps each string's 26-length character-
count signature to the list of strings sharing that signature; the step
never short-circuits, it just wants the whole table at the end.
"""
from .. import algorithm as _algorithm
hashmap_pass = _algorithm.hashmap_pass


def solve(strs):
    def step(table, i, s):
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        table.setdefault(tuple(counts), []).append(s)
        return None

    _result, table = hashmap_pass(strs, step)
    return list(table.values())
