from .._meta.algorithm import explore


def generate_all(initial_state, expand):
    """Generic backtracking/DFS search shared by every problem that explores
    a space of partial solutions and collects the complete ones.

    `expand(state)` must return an iterable of `(next_state, is_complete)`
    pairs reachable from `state` in one step. Whenever `is_complete` is True
    for a yielded state, that state is captured as one finished solution
    instead of being expanded further.

    Instantiation of the shared _meta explore() engine: LIFO (depth-first)
    discipline over (payload, is_complete) states; complete states are
    leaves (transition returns nothing for them); the fold collects the
    payloads of every complete state that leaves the frontier.
    """
    def transition(meta_state):
        payload, complete = meta_state
        if complete:
            return ()
        return expand(payload)

    results = []
    for payload, complete in explore([(initial_state, False)], transition, order="lifo"):
        if complete:
            results.append(payload)
    return results
