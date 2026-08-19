class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(list1, list2):
    """Optimal: merge the two already-sorted linked lists in a single pass
    by splicing existing nodes onto a dummy-headed result list, advancing
    whichever pointer has the smaller value. No sorting, no extra node
    allocation for values already in a list. O(n + m) time, O(1) extra
    space (excluding the input/output list nodes themselves)."""

    def build_list(values):
        dummy = ListNode()
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    def to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    head1 = build_list(list1)
    head2 = build_list(list2)

    dummy = ListNode()
    tail = dummy

    while head1 and head2:
        if head1.val <= head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 else head2

    return to_list(dummy.next)
