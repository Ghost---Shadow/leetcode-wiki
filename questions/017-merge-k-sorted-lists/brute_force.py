class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(lists):
    """Brute-force: dump every node's value from every list into one big
    list, then sort it. O(N log N) via a full sort instead of a k-way
    merge, and does not exploit that each input list is already sorted."""
    nodes = []
    for lst in lists:
        head = None
        tail = None
        for val in lst:
            node = ListNode(val)
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next

    nodes.sort()

    dummy = ListNode()
    tail = dummy
    for val in nodes:
        tail.next = ListNode(val)
        tail = tail.next

    result = []
    cur = dummy.next
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result
