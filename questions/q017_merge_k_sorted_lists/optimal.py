import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(lists):
    """K-way merge with a min-heap: push the head of each list, repeatedly
    pop the smallest, and push its successor. O(N log k) time (N = total
    nodes, k = number of lists), O(k) heap space."""
    heap = []
    for i, lst in enumerate(lists):
        head = None
        tail = None
        for val in lst:
            node = ListNode(val)
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
        if head is not None:
            heapq.heappush(heap, (head.val, i, head))

    dummy = ListNode()
    tail = dummy
    counter = len(lists)
    while heap:
        val, _, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    result = []
    cur = dummy.next
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result
