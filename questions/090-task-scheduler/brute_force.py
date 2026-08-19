from collections import Counter


def solve(tasks, n):
    """Brute-force simulation: steps through the timeline one tick at a time, at
    each tick scanning all task types to pick the available one (not in cooldown)
    with the highest remaining count, instead of using the closed-form counting
    formula based on the most frequent task."""
    counts = Counter(tasks)
    time = 0
    cooldown_until = {}
    remaining = sum(counts.values())

    while remaining > 0:
        best = None
        for t in counts:
            if counts[t] > 0 and cooldown_until.get(t, -1) <= time:
                if best is None or counts[t] > counts[best]:
                    best = t
        if best is not None:
            counts[best] -= 1
            cooldown_until[best] = time + n + 1
            remaining -= 1
        time += 1

    return time
