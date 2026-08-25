class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(nums, k):
    """Brute-force: dump every node's value into a plain Python list, reverse
    each k-sized chunk with slicing, then rebuild the linked list from
    scratch. Uses O(n) extra list storage instead of reversing the links
    in place."""
    head = None
    tail = None
    for val in nums:
        node = ListNode(val)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node

    values = []
    cur = head
    while cur:
        values.append(cur.val)
        cur = cur.next

    result = []
    i = 0
    while i < len(values):
        chunk = values[i:i + k]
        if len(chunk) == k:
            chunk.reverse()
        result.extend(chunk)
        i += k

    dummy = ListNode()
    tail = dummy
    for val in result:
        tail.next = ListNode(val)
        tail = tail.next

    out = []
    cur = dummy.next
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out
