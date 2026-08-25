def solve(gas, cost):
    """Brute-force: try every possible starting station and simulate the full
    trip around the circuit for each one. O(n^2) instead of the O(n) greedy
    single pass."""
    n = len(gas)
    for start in range(n):
        tank = 0
        ok = True
        for i in range(n):
            idx = (start + i) % n
            tank += gas[idx] - cost[idx]
            if tank < 0:
                ok = False
                break
        if ok:
            return start
    return -1
