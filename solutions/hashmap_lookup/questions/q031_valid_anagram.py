"""Reshaper for questions/q031_valid_anagram.

Converts this question's (s, t) -> bool I/O into two calls to the shared
hashmap_pass(): the first pass over `s` builds a running character-
frequency table (never short-circuits); the second pass over `t` consumes
that same table, short-circuiting with a mismatch signal the moment a
character is missing or over-consumed. `s` and `t` are anagrams iff the
second pass runs to completion (every count lands back at exactly zero).
"""
from .. import algorithm as _algorithm
hashmap_pass = _algorithm.hashmap_pass


def solve(s, t):
    if len(s) != len(t):
        return False

    def build_step(table, i, ch):
        table[ch] = table.get(ch, 0) + 1
        return None

    _result, counts = hashmap_pass(s, build_step)

    def consume_step(table, i, ch):
        if table.get(ch, 0) <= 0:
            return "mismatch"
        table[ch] -= 1
        return None

    result, _table = hashmap_pass(t, consume_step, table=counts)
    return result is None
