def solve(n):
    """Brute-force: builds the exact same exponential Fibonacci-style search
    tree as climb(k) = climb(k-1) + climb(k-2), then combines it bottom-up --
    but materializes the tree as explicit node objects (so identical k values
    reached via different paths are NOT deduplicated/memoized) instead of
    using the call stack. O(2^n) time."""
    if n <= 0:
        return 0

    class Node:
        __slots__ = ("k", "left", "right", "value")

        def __init__(self, k):
            self.k = k
            self.left = None
            self.right = None
            self.value = None

    root = Node(n)
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.k > 2:
            node.left = Node(node.k - 1)
            node.right = Node(node.k - 2)
            stack.append(node.left)
            stack.append(node.right)

    for node in reversed(order):
        if node.k <= 2:
            node.value = node.k
        else:
            node.value = node.left.value + node.right.value

    return root.value
