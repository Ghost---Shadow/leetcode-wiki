from .._meta.algorithm import explore


def converge(left0, right0, step):
    """Two pointers starting at (left0, right0), moving inward until they
    meet or cross. `step(left, right)` is a stateful closure that owns
    all of the comparison/accumulation logic for the caller's problem
    (closing over whatever running answer it is building) and returns the
    next (left, right) pair to advance to, or None to stop early. Returns
    the final (left, right) pair reached.

    Container With Most Water, Trapping Rain Water, the inner two-pointer
    scan of 3Sum (run once per fixed outer index, with explicit bounds
    (i+1, n-1) rather than the whole array), and Valid Palindrome are all
    this same shape: two pointers converging inward, differing only in
    what `step` does at each pair.

    Instantiation of the shared _meta explore() engine: state = (left,
    right) pair (mirrors floyd_cycle_detection's (slow, fast) state),
    chain discipline (single-successor transition), with `step` as the
    transition's per-state work and the fold simply keeping the last
    state reached -- the closure inside `step` accumulates whatever real
    answer the caller needs.
    """
    def transition(state):
        left, right = state
        if left >= right:
            return ()
        nxt = step(left, right)
        return (nxt,) if nxt is not None else ()

    if left0 > right0:
        return (left0, right0)

    last = (left0, right0)
    for state in explore((last,), transition):
        last = state
    return last
