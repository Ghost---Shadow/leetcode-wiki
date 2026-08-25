from .._meta.algorithm import explore


def streaming_scan(n, step):
    """Single left-to-right pass over indices 0..n-1. `step(i)` is a
    stateful closure -- it owns whatever window bookkeeping the caller
    needs (two pointers, a monotonic deque, a running counter, ...) for
    the newly-admitted index `i`, and returns a value to emit for this
    step, or None to emit nothing. Returns the list of emitted values, in
    index order.

    Every "sliding window" problem is this one linear pass with a
    different stateful step: variable windows that expand and contract a
    left pointer (longest substring without repeating characters, minimum
    window substring) and fixed windows maintained with a monotonic deque
    (sliding window maximum) are all instances -- only what `step` closes
    over and emits changes.

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over indices 0..n-1 (a plain left-to-right
    pass, mirroring kadane_running_extremes's index chain), with all
    window state carried inside the `step` closure and the fold
    collecting whatever `step` chooses to emit.
    """
    def transition(i):
        return (i + 1,) if i + 1 < n else ()

    emitted = []
    for i in explore((0,) if n else (), transition):
        value = step(i)
        if value is not None:
            emitted.append(value)
    return emitted
