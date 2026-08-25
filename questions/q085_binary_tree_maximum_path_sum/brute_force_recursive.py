class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Builds a binary tree from a LeetCode-style level-order list (None
    marks a missing child) and returns the root."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    n = len(values)
    while queue and i < n:
        node = queue.pop(0)
        if i < n:
            left_val = values[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
        if i < n:
            right_val = values[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
    return root


def max_downward_sum(node):
    """Naive O(n) helper: the largest sum of a downward path starting at
    `node` (recomputed independently for every node in solve())."""
    if node is None:
        return 0
    best_child = max(max_downward_sum(node.left), max_downward_sum(node.right), 0)
    return node.val + best_child


def solve(values):
    """Brute-force: for every single node in the tree, independently
    recompute the best downward path sum through each of its children from
    scratch via max_downward_sum(). O(n^2) total work (each of the n nodes
    triggers an O(n) traversal) instead of the standard single O(n)
    post-order DP that reuses each subtree's result exactly once."""
    root = build_tree(values)
    if root is None:
        return 0

    nodes = []

    def collect(node):
        if node is None:
            return
        nodes.append(node)
        collect(node.left)
        collect(node.right)

    collect(root)

    best = float("-inf")
    for node in nodes:
        left_sum = max(max_downward_sum(node.left), 0)
        right_sum = max(max_downward_sum(node.right), 0)
        best = max(best, node.val + left_sum + right_sum)
    return best
