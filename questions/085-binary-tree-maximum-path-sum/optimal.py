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


def solve(values):
    """Optimal: a single post-order DFS pass. Each call returns the best
    downward path sum starting at that node (0 if going down would only
    hurt), while updating a running global best that considers the node as
    the "peak" of a path bending through both children. Each subtree's
    result is computed exactly once. O(n) time, O(h) space for the
    recursion stack."""
    root = build_tree(values)
    if root is None:
        return 0

    best = float("-inf")

    def dfs(node):
        nonlocal best
        if node is None:
            return 0
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)
        best = max(best, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return best
