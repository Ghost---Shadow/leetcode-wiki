from itertools import combinations_with_replacement


def solve(candidates, target):
    """Brute-force: since candidates can repeat, first bound how many
    elements a combination could possibly hold (target // smallest
    candidate), then for every length up to that bound enumerate ALL
    multisets of that length via combinations_with_replacement and keep the
    ones that sum to target. Explores a much larger search space than the
    standard pruning backtrack (which stops early once the running sum
    exceeds target)."""
    if not candidates:
        return []
    smallest = min(candidates)
    if smallest <= 0:
        return []
    max_len = target // smallest

    results = []
    for length in range(1, max_len + 1):
        for combo in combinations_with_replacement(sorted(candidates), length):
            if sum(combo) == target:
                results.append(list(combo))
    return results
