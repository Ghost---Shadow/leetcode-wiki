class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Builds a tree from a LeetCode-style level-order list (None = missing child)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def solve(tree_list, p_val, q_val):
    """Optimal: a single recursive DFS pass. At each node, if it matches p or q
    it's returned up; a node whose left and right subtrees both report a find
    is the LCA. Otherwise the non-None side (if any) is propagated up. O(n)
    time, single traversal, O(h) recursion stack space."""
    root = build_tree(tree_list)

    def dfs(node):
        if node is None or node.val == p_val or node.val == q_val:
            return node
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            return node
        return left if left else right

    result = dfs(root)
    return result.val if result else None
