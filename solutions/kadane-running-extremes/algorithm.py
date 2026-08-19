def running_fold_best(values, init_state, step, extract):
    """Generalized Kadane's algorithm: a single left-to-right pass carrying
    an arbitrary `state` forward via `step(state, value) -> new_state`, and
    tracking the best value seen so far via `extract(state)`.

    Maximum Subarray uses state = running max ending here (a plain number).
    Maximum Product Subarray uses state = (running max, running min) ending
    here, since a negative running min times a negative number can flip
    into the new running max. Both are "carry forward the best-ending-here
    value(s), take the global best across the whole pass" -- this one
    routine is the shared shape.
    """
    state = init_state(values[0])
    best = extract(state)
    for v in values[1:]:
        state = step(state, v)
        candidate = extract(state)
        if candidate > best:
            best = candidate
    return best
