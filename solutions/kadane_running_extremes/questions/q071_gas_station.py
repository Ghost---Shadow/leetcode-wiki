"""Reshaper for questions/q071_gas_station.

Converts this question's (gas, cost) -> int I/O into a call to the shared
running_fold_best(): the valid start is the station right after the
global minimum of the running prefix sum of (gas[i] - cost[i]) (a classic
fact about this problem), so track state = (index, prefix sum) and let
extract return (-prefix, -index) -- maximizing "-prefix" is minimizing the
prefix sum, and the routine's return value (the winning tuple itself, not
just a scalar) carries the index of the first station achieving it back
out. No valid start exists unless the total is non-negative.
"""
from .. import algorithm as _algorithm
running_fold_best = _algorithm.running_fold_best


def solve(gas, cost):
    diffs = [g - c for g, c in zip(gas, cost)]
    if sum(diffs) < 0:
        return -1

    n = len(diffs)

    def init_state(first_diff):
        return (0, first_diff)

    def step(state, diff):
        index, prefix = state
        return (index + 1, prefix + diff)

    def extract(state):
        index, prefix = state
        return (-prefix, -index)

    _, neg_index = running_fold_best(diffs, init_state, step, extract)
    return (-neg_index + 1) % n
