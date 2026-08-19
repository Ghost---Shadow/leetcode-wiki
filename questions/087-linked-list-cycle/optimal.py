class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(values, pos):
    """Optimal: Floyd's tortoise-and-hare cycle detection. Two pointers walk the
    list at different speeds; if they ever meet, there's a cycle. O(n) time,
    O(1) extra space (no visited set needed)."""
    if not values:
        return False

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]

    slow = fast = nodes[0]
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
