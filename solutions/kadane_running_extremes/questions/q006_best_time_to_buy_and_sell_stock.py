"""Reshaper for questions/q006_best_time_to_buy_and_sell_stock.

Converts this question's prices -> max-profit I/O into a call to the
shared running_fold_best(): state carries the minimum price seen so far,
and the profit from selling at the current price is exactly the
"best ending here" value the routine already maximizes over the pass.
"""
from .. import algorithm as _algorithm
running_fold_best = _algorithm.running_fold_best


def solve(prices):
    if not prices:
        return 0

    def init_state(first_price):
        return (first_price, 0)

    def step(state, price):
        min_price, _ = state
        new_min = min(min_price, price)
        return (new_min, price - new_min)

    def extract(state):
        return state[1]

    return running_fold_best(prices, init_state, step, extract)
