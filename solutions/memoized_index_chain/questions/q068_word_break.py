"""Reshaper for questions/q068_word_break.

Converts this question's (s, wordDict) -> bool I/O into a call to the
shared chain_dp(): segmentable(i) = (i == 0) or exists j < i with
segmentable(j) and s[j:i] in words, a boolean-OR-over-predecessors
recurrence over prefix lengths 0..len(s).
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp


def solve(s, wordDict):
    words = set(wordDict)
    n = len(s)

    def compute(i, table):
        if i == 0:
            return True
        return any(table[j] and s[j:i] in words for j in range(i))

    table = chain_dp(n, compute)
    return table[n]
