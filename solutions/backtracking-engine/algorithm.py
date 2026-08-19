def generate_all(initial_state, expand):
    """Generic backtracking/DFS search shared by every problem that explores
    a space of partial solutions and collects the complete ones.

    `expand(state)` must return an iterable of `(next_state, is_complete)`
    pairs reachable from `state` in one step. Whenever `is_complete` is True
    for a yielded state, that state is captured as one finished solution
    instead of being expanded further.

    Walked via an explicit stack (no Python recursion), so this is the one
    engine every backtracking-shaped problem below plugs its own state shape
    and branching rules into via `expand`.
    """
    results = []
    stack = [initial_state]
    while stack:
        state = stack.pop()
        for next_state, is_complete in expand(state):
            if is_complete:
                results.append(next_state)
            else:
                stack.append(next_state)
    return results
