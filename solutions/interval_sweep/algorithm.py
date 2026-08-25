from .._meta.algorithm import explore


def sweep_sorted(items, key, init_state, step):
    """Sorts `items` by `key`, then folds left-to-right over them via
    step(state, item) -> new_state, starting from `init_state`. Returns
    the final state.

    Merge Intervals sorts by start and folds a "merged output list" state
    (extend the last interval, or append a new one, depending on overlap).
    Maximum Profit in Job Scheduling sorts by end and folds a "(dp table,
    end-times-seen list)" state, binary-searching the end-times list for
    the best compatible earlier job. Both are "sort the intervals once,
    then carry state forward across the sorted sequence" -- only the
    per-step update differs.

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over indices into the sorted sequence (a plain
    left fold), carrying `state` in the fold's accumulator.
    """
    ordered = sorted(items, key=key)
    n = len(ordered)
    if n == 0:
        return init_state

    def transition(i):
        return (i + 1,) if i + 1 < n else ()

    state = init_state
    for i in explore((0,), transition):
        state = step(state, ordered[i])
    return state
