class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(l1, l2):
    """Optimal: single pass walking both lists simultaneously, adding digits plus
    carry as we go and building the result list directly -- O(max(n, m)) time,
    O(max(n, m)) output space, no big-integer conversion round trip."""

    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    n1 = build(l1)
    n2 = build(l2)

    dummy = ListNode()
    cur = dummy
    carry = 0
    while n1 or n2 or carry:
        v1 = n1.val if n1 else 0
        v2 = n2.val if n2 else 0
        total = v1 + v2 + carry
        carry, digit = divmod(total, 10)
        cur.next = ListNode(digit)
        cur = cur.next
        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None

    result = []
    node = dummy.next
    while node:
        result.append(node.val)
        node = node.next
    return result
