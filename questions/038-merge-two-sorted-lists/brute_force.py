class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(list1, list2):
    """Brute-force: dump all values from both linked lists into a plain
    Python list and sort it, instead of merging the two already-sorted lists
    in a single O(n + m) pass. O((n + m) log(n + m))."""

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

    values = []
    node = head1
    while node:
        values.append(node.val)
        node = node.next
    node = head2
    while node:
        values.append(node.val)
        node = node.next

    values.sort()

    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next

    return to_list(dummy.next)
