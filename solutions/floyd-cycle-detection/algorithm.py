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
    """
    slow = fast = start
    while True:
        slow = step(slow)
        fast = step(fast)
        if fast is None:
            return None
        fast = step(fast)
        if fast is None:
            return None
        if slow == fast:
            return slow
