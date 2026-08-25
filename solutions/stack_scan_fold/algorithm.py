from .._meta.algorithm import explore


def stack_scan(items, step):
    """Scans `items` left-to-right over the shared explore() index chain,
    threading one explicit stack across the whole pass. For each item,
    step(stack, item) is invoked and is free to push, pop, or otherwise
    collapse the stack however the specific parsing/simulation rule
    requires -- bracket matching, run-length decoding, operator folding,
    path-segment collapsing, physical collision resolution, and so on.
    Any extra scalar bookkeeping the rule needs (a running number, a sign,
    a validity flag) is the caller's responsibility -- typically a small
    mutable cell closed over by `step`, since the stack itself is the only
    piece of state this routine owns. Returns the final stack.

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over the indices (a plain left fold), with the
    stack carried in the fold's accumulator -- the same shape as
    monotonic_stack_next_element, generalized to an arbitrary step rule.
    """
    n = len(items)
    stack = []

    def transition(i):
        return (i + 1,) if i + 1 < n else ()

    for i in explore((0,) if n else (), transition):
        step(stack, items[i])
    return stack
