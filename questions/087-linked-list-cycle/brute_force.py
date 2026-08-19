class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(values, pos):
    """Brute-force: traverses the list tracking every visited node in a set
    (O(n) extra space), instead of Floyd's O(1)-space fast/slow pointer trick."""
    if not values:
        return False

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]

    visited = set()
    node = nodes[0]
    while node:
        if id(node) in visited:
            return True
        visited.add(id(node))
        node = node.next
    return False
