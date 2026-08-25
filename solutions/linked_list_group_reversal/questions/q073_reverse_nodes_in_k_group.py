"""Reshaper for questions/q073_reverse_nodes_in_k_group.

Converts this question's (list[int], int) -> list[int] I/O into a direct
call to the shared reverse_in_groups() -- this question is exactly what
that routine was generalized from.
"""
from .. import algorithm as _algorithm
ListNode = _algorithm.ListNode
reverse_in_groups = _algorithm.reverse_in_groups


def solve(nums, k):
    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    if not nums:
        return []

    head = build(nums)
    result_head = reverse_in_groups(head, k)

    result = []
    cur = result_head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result
