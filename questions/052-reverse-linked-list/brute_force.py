class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    """Brute-force: repeatedly rescans the list from the head to find the current
    last node, records its value, then unlinks it -- O(n^2) instead of a single
    O(n) pointer-reversal pass."""

    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    node = build(head)
    result = []
    while node:
        prev = None
        cur = node
        while cur.next:
            prev = cur
            cur = cur.next
        result.append(cur.val)
        if prev:
            prev.next = None
        else:
            node = None
    return result
