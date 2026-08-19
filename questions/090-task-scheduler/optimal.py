from collections import Counter


def solve(tasks, n):
    """Optimal: closed-form counting formula. Take the most frequent task's count
    (max_count) and lay out (max_count - 1) full cooldown "blocks" of length
    (n + 1), then add the number of tasks tied for that max frequency for the
    final block. This lower bound is always achievable by round-robining the
    other tasks into the idle slots, and the answer can never be less than the
    total number of tasks. O(n) time (n = len(tasks)) to count frequencies,
    O(1) additional work for the formula."""
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for c in counts.values() if c == max_count)

    return max(len(tasks), (max_count - 1) * (n + 1) + num_max)
