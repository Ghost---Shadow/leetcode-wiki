def solve(gas, cost):
    """Optimal: greedy single pass. If total gas >= total cost, a valid
    start exists. Track a running tank; whenever it drops below zero, no
    station in the current segment can be the start, so reset the start to
    the next station. O(n) time, O(1) space."""
    total = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1
