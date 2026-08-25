"""Reshaper for questions/q076_longest_valid_parentheses.

Converts this question's (s) -> int I/O into a call to the shared
chain_dp(): valid_len(i) is the length of the longest valid parentheses
substring ending at index i (0 when s[i] == '(' or there's no match),
the classic lookback recurrence:
  - s[i] == ')' and s[i-1] == '(': valid_len(i) = valid_len(i-2) + 2
  - s[i] == ')' and s[i-1] == ')': if the char just before the block
    ending at i-1 is '(', valid_len(i) = valid_len(i-1) + 2 +
    valid_len(before that block).
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp


def solve(s):
    if not s:
        return 0

    n = len(s) - 1

    def compute(i, table):
        if s[i] == "(":
            return 0
        if i - 1 >= 0 and s[i - 1] == "(":
            return (table[i - 2] if i - 2 >= 0 else 0) + 2
        prev_len = table[i - 1] if i - 1 >= 0 else 0
        j = i - prev_len - 1
        if prev_len > 0 and j >= 0 and s[j] == "(":
            before = table[j - 1] if j - 1 >= 0 else 0
            return prev_len + 2 + before
        return 0

    table = chain_dp(n, compute)
    return max(table.values()) if table else 0
