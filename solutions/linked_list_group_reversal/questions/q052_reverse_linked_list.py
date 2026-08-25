"""Reshaper for questions/q052_reverse_linked_list.

Converts this question's list[int] -> list[int] I/O into a call to the
shared reverse_in_groups(): reversing the whole list is reversing it in a
single group whose size equals the list's length.
"""
from .. import algorithm as _algorithm
ListNode = _algorithm.ListNode
reverse_in_groups = _algorithm.reverse_in_groups


def solve(head):
    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    n = len(head)
    if n == 0:
        return []

    node = build(head)
    result_head = reverse_in_groups(node, n)

    result = []
    cur = result_head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result
