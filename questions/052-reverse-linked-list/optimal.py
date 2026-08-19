class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    """Optimal: single-pass iterative pointer reversal -- walk the list once,
    at each node flipping its `next` pointer to point at the previous node --
    O(n) time, O(1) extra space."""

    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    node = build(head)
    prev = None
    while node:
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt

    result = []
    while prev:
        result.append(prev.val)
        prev = prev.next
    return result
