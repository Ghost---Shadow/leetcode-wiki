from .._meta.algorithm import explore


def scan(items, initial_acc, combine):
    """Left-to-right single-pass scan/fold over `items`, carrying an
    accumulator forward.

    `combine(acc, item)` returns the updated accumulator for the next
    step; it may also perform a side effect (e.g. writing into an output
    array in place) as it goes. This is the classic "running state
    carried across one linear pass" shape: prefix/suffix running
    products, a read/write compaction pointer, a merge-from-the-back
    pointer pair, Boyer-Moore's candidate/count -- all are one forward
    sweep threading an accumulator through every element.

    Instantiation of the shared _meta explore() engine: state shape is
    (index, accumulator); frontier discipline is FIFO, but a single
    successor per step degenerates the graph into a plain left-to-right
    chain; the transition calls `combine` to advance the accumulator by
    one item; the fold keeps only the final accumulator once every item
    has been consumed.

    Returns the final accumulator.
    """
    n = len(items)

    def transition(state):
        i, acc = state
        if i >= n:
            return []
        return [(i + 1, combine(acc, items[i]))]

    final_acc = initial_acc
    for _, acc in explore([(0, initial_acc)], transition, order="fifo"):
        final_acc = acc
    return final_acc
