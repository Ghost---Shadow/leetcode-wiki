def solve(coins, amount):
    """Brute-force, no memoization: explores every coin choice at every
    remaining amount via an explicit stack instead of recursion -- the exact
    same exponential O(k^amount) search tree, just walked iteratively."""
    best = float("inf")
    stack = [(amount, 0)]
    while stack:
        remaining, count = stack.pop()
        if remaining == 0:
            best = min(best, count)
            continue
        if remaining < 0:
            continue
        for coin in coins:
            stack.append((remaining - coin, count + 1))
    return best if best != float("inf") else -1
