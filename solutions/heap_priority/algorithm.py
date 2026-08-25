from .._meta.algorithm import explore


def priority_pop_stream(seeds, transition, priority):
    """Repeatedly pops the highest-priority state from a frontier seeded
    with `seeds`, letting `transition(state)` push further states reachable
    from the one just popped. Yields states in the order they are popped
    (i.e. non-decreasing `priority`).

    This is the single shape behind every "give me things in sorted/best
    order" heap problem in this technique:

    - K-way merge (Merge k Sorted Lists): each popped list head's
      transition releases that same list's next element, so the stream
      is exactly the fully merged, sorted sequence.
    - Selection (Top K Frequent Elements, Kth Largest Element): the items
      are static (transition returns nothing), so the routine degenerates
      to "drain a heap" -- pop the first k (or the k-th) to get the
      answer, using a negated priority to select "largest" instead of
      "smallest".
    - Sweep + side effect (Meeting Rooms II): seeded with every meeting,
      popped in start-time order; transition mutates a closure-held
      min-heap of room end times and tracks the running peak room count
      as a side effect, then returns nothing (there is nothing further to
      release from a single meeting).

    Instantiation of the shared _meta explore() engine: priority
    discipline, `priority(state)` as the sort key (heapq compares tuples,
    so "largest first" selection is expressed by negating the relevant
    field before it becomes a state/priority).
    """
    yield from explore(seeds, transition, order="priority", priority=priority)
