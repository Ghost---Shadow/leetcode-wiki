def solve(prices):
    """Brute-force: explores, on every day, both 'do nothing' and 'buy/sell'
    branches via an explicit stack of (day, holding, profit-so-far) states
    instead of recursion -- same 2^n decision sequences, walked iteratively."""
    n = len(prices)
    if n == 0:
        return 0

    best = 0
    stack = [(0, False, 0)]
    while stack:
        day, holding, profit = stack.pop()
        if day == n:
            best = max(best, profit)
            continue
        stack.append((day + 1, holding, profit))
        if not holding:
            stack.append((day + 1, True, profit - prices[day]))
        else:
            stack.append((day + 1, False, profit + prices[day]))
    return best
