"""Reshaper for questions/q063_best_time_to_buy_and_sell_stock_ii.

Converts this question's prices -> total-profit I/O into a call to the
shared running_fold_best(): state carries the cumulative profit from
summing every positive day-to-day gain. That total only ever increases, so
its running max across the whole pass is simply its final value.
"""
from .. import algorithm as _algorithm
running_fold_best = _algorithm.running_fold_best


def solve(prices):
    if not prices:
        return 0

    def init_state(first_price):
        return (first_price, 0)

    def step(state, price):
        prev_price, total = state
        diff = price - prev_price
        if diff > 0:
            total += diff
        return (price, total)

    def extract(state):
        return state[1]

    return running_fold_best(prices, init_state, step, extract)
