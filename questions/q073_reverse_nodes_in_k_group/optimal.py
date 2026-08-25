class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(nums, k):
    """Optimal: reverse the links in place, group by group, using O(1) extra
    space (a handful of pointers) instead of dumping values into an
    auxiliary list. O(n) time."""
    head = None
    tail = None
    for val in nums:
        node = ListNode(val)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node

    def get_kth(start, k):
        cur = start
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if kth is None:
            break
        group_next = kth.next

        # reverse the group
        prev, cur = group_next, group_prev.next
        while cur != group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        new_group_prev = group_prev.next
        group_prev.next = kth
        group_prev = new_group_prev

    out = []
    cur = dummy.next
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out
