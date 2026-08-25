"""Reshaper for questions/q045_add_two_numbers.

Converts this question's (list[int], list[int]) -> list[int] I/O into a
call to the shared merge_walk(): at each step advance both list pointers
together, adding corresponding digits plus a running carry threaded as
`state`, stopping once both lists and the carry are exhausted.
"""
from .. import algorithm as _algorithm
ListNode = _algorithm.ListNode
merge_walk = _algorithm.merge_walk


def solve(l1, l2):
    def build(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    head1 = build(l1)
    head2 = build(l2)

    def step(n1, n2, carry):
        if n1 is None and n2 is None and carry == 0:
            return None
        v1 = n1.val if n1 else 0
        v2 = n2.val if n2 else 0
        total = v1 + v2 + carry
        new_carry, digit = divmod(total, 10)
        next1 = n1.next if n1 else None
        next2 = n2.next if n2 else None
        return ([digit], next1, next2, new_carry)

    return merge_walk(head1, head2, step, 0)
