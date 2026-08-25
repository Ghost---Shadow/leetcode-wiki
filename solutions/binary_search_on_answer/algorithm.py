from .._meta.algorithm import explore


def binary_search_converge(seed, step):
    """Generic binary-search-style interval convergence.

    `seed` is an opaque state tuple packed by the caller so that it carries
    everything needed both to compute the next, narrower state AND (once
    convergence is reached) to read off the final answer. `step(state)`
    inspects the current state, decides which half of the search space
    survives, and returns the next state -- or None to signal that `state`
    is already terminal (the search has converged / the answer has been
    found).

    Instantiation of the shared _meta explore() engine: state shape is a
    caller-defined tuple (typically (lo, hi, ...payload)); frontier
    discipline is LIFO, but since `step` produces at most one successor the
    graph degenerates into a plain sequential chain -- each "narrowing" is
    just the next link; the transition owns all of the interval-shrinking
    logic (and, when relevant, the terminal payload); the fold keeps only
    the last state to leave the frontier, i.e. the terminal state.

    Returns the final (terminal) state.
    """
    def transition(state):
        nxt = step(state)
        return [] if nxt is None else [nxt]

    final = seed
    for state in explore([seed], transition, order="lifo"):
        final = state
    return final
