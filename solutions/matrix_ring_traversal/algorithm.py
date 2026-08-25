from .._meta.algorithm import explore


def ring_layers(rows, cols):
    """Yields (top, bottom, left, right) boundaries for each concentric
    ring of a `rows` x `cols` grid, outermost first, shrinking by one
    layer at a time until the ring is exhausted.

    Instantiation of the shared _meta explore() engine: state shape is a
    (top, bottom, right, left) boundary tuple; frontier discipline is
    LIFO, but the transition produces at most one successor (the next
    ring in by one layer, or none once the boundaries cross), so the
    graph degenerates into a plain chain -- one ring per link. Callers
    fold this stream of boundaries themselves: collecting elements in
    spiral order, rotating each ring's border in place, etc.
    """
    if rows == 0 or cols == 0:
        return

    def transition(state):
        top, bottom, left, right = state
        nxt = (top + 1, bottom - 1, left + 1, right - 1)
        if nxt[0] > nxt[1] or nxt[2] > nxt[3]:
            return []
        return [nxt]

    seed = (0, rows - 1, 0, cols - 1)
    yield from explore([seed], transition, order="lifo")
