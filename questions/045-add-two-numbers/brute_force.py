class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(l1, l2):
    """Brute-force: converts each linked list into a plain integer (summing
    digit * 10**i), adds the two integers directly, then peels the sum back apart
    into a reversed-digit list -- avoids the elegant digit-by-digit carry walk."""

    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def node_to_int(node):
        num = 0
        power = 1
        while node:
            num += node.val * power
            power *= 10
            node = node.next
        return num

    n1 = build(l1)
    n2 = build(l2)
    total = node_to_int(n1) + node_to_int(n2)

    if total == 0:
        return [0]

    result = []
    while total > 0:
        result.append(total % 10)
        total //= 10
    return result
