from .._meta.algorithm import explore


def pointer_sweep(seed, step):
    """Generic in-place, pointer-driven array rewrite.

    `seed` is an opaque state tuple of one or more indices (e.g. (lo, hi)
    for inward-converging swaps, (low, mid, high) for a three-way
    partition sweep, or (i,) for a single forward-scanning pointer).
    `step(state)` performs whatever in-place swaps/writes are needed as a
    side effect (closing over the array being rewritten) and returns the
    next pointer state, or None once the rewrite is complete.

    Instantiation of the shared _meta explore() engine: state shape is the
    caller's pointer tuple; frontier discipline is LIFO, but a step
    producing at most one successor degenerates the graph into a plain
    sequential chain; the transition owns every swap/write (that's where
    the actual rewriting happens); the fold keeps only the terminal
    state.

    Returns the final (terminal) pointer state.
    """
    def transition(state):
        nxt = step(state)
        return [] if nxt is None else [nxt]

    final = seed
    for state in explore([seed], transition, order="lifo"):
        final = state
    return final
