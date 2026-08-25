class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_walk(node1, node2, step, state=None):
    """Walks two singly-linked lists together, one step at a time,
    threading a caller-owned `state` across the whole walk. At each step,
    step(node1, node2, state) decides what to do with the current pair of
    positions and returns either None (stop) or a tuple
    (emitted, next_node1, next_node2, next_state), where `emitted` is a
    sequence of values to append to the output. Returns the flat list of
    everything emitted.

    This is the shared shape behind "walk two linked lists together and
    build a result": merge_two_sorted_lists advances whichever pointer
    currently holds the smaller value and ignores `state`, while
    add_two_numbers advances both pointers together each step and threads
    a running carry as `state`.
    """
    out = []
    while True:
        result = step(node1, node2, state)
        if result is None:
            break
        emitted, node1, node2, state = result
        out.extend(emitted)
    return out
