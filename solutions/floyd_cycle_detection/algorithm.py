from .._meta.algorithm import explore


def find_cycle_meeting_point(start, step):
    """Floyd's tortoise-and-hare over an arbitrary state space: advances a
    slow pointer one step() at a time and a fast pointer two step()s at a
    time. Returns the value at which they first meet, or None if the fast
    pointer runs off the end (step() returns None) before that happens --
    i.e. there is no cycle.

    Works for any chain of states: linked-list nodes (step = lambda n:
    n.next), or a purely functional iteration like the digit-square-sum
    chain in Happy Number (step = next_number). O(n) time, O(1) space --
    no visited set needed.

    Instantiation of the shared _meta explore() engine: a single-successor
    chain over (slow, fast) pointer pairs; the fold returns the first pair
    whose halves meet.
    """
    def advance(pair):
        slow, fast = pair
        slow = step(slow)
        fast = step(fast)
        if fast is None:
            return None
        fast = step(fast)
        if fast is None:
            return None
        return (slow, fast)

    def transition(pair):
        slow, fast = pair
        if slow == fast:
            return ()  # met: stop unfolding the chain
        nxt = advance(pair)
        return (nxt,) if nxt is not None else ()

    first = advance((start, start))
    for slow, fast in explore((first,) if first is not None else (), transition):
        if slow == fast:
            return slow
    return None
