"""Reshaper for questions/q038_merge_two_sorted_lists.

Converts this question's (list[int], list[int]) -> list[int] I/O into a
call to the shared merge_walk(): at each step advance whichever of the two
list pointers currently holds the smaller value (state unused).
"""
from .. import algorithm as _algorithm
ListNode = _algorithm.ListNode
merge_walk = _algorithm.merge_walk


def solve(list1, list2):
    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    head1 = build(list1)
    head2 = build(list2)

    def step(n1, n2, state):
        if n1 is None and n2 is None:
            return None
        if n2 is None or (n1 is not None and n1.val <= n2.val):
            return ([n1.val], n1.next, n2, state)
        return ([n2.val], n1, n2.next, state)

    return merge_walk(head1, head2, step)
