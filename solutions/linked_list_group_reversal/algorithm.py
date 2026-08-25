class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_in_groups(head, k):
    """Reverses every complete consecutive group of k nodes in a singly
    linked list, in place, in a single pass using O(1) extra pointers. A
    final group with fewer than k remaining nodes is left untouched.

    Reversing the whole list is the degenerate case k = len(list): the
    entire list is exactly one complete group, so this one routine covers
    both reverse_linked_list (k = n) and reverse_nodes_in_k_group
    (arbitrary k). Requires k >= 1 and a non-empty `head`.
    """

    def get_kth(start, count):
        cur = start
        while cur and count > 0:
            cur = cur.next
            count -= 1
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

    return dummy.next
