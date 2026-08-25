from .._meta.algorithm import explore


def running_fold_sum(values, init_state, step):
    """Single left-to-right pass carrying `state` forward via
    step(state, value) -> (new_state, contribution), summing every step's
    contribution and returning the total.

    Subarray Sum Equals K carries (running prefix sum, hashmap of
    prefix-sum -> occurrence count) and contributes "how many earlier
    prefixes equal prefix - k" at each step -- the hashmap turns an O(n^2)
    pair count into a single O(n) pass with O(1) lookups per step.

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over indices (a plain left fold), carrying
    (state, running total) in the fold's accumulator.
    """
    state = init_state
    total = 0

    def transition(i):
        return (i + 1,) if i + 1 < len(values) else ()

    for i in explore((0,) if values else (), transition):
        state, contribution = step(state, values[i])
        total += contribution
    return total


def longest_chain_from_seeds(seeds, in_domain, successor):
    """For every state in `seeds`, follows the implicit successor chain
    (successor(x) -> the "next" state) for as long as in_domain(next)
    holds, and returns the longest chain length found across all seeds.

    Longest Consecutive Sequence seeds with every number that starts a run
    (its predecessor is absent from the set), then walks forward while the
    next integer is present -- a hashset gives O(1) membership checks, and
    restricting seeds to true run-starts keeps the whole scan O(n) despite
    the nested walk.

    Instantiation of the shared _meta explore() engine: an outer LIFO pass
    over the seeds themselves (transition releases nothing further at that
    level -- each seed's own chain is walked directly, not through
    explore), with the fold taking the running max chain length.
    """
    best = 0

    def transition(seed):
        return ()

    for seed in explore(seeds, transition, order="lifo"):
        length = 1
        current = seed
        while True:
            nxt = successor(current)
            if not in_domain(nxt):
                break
            current = nxt
            length += 1
        best = max(best, length)
    return best
