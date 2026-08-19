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
    """Brute-force: finds the full root-to-node path for p and for q via separate
    DFS calls, then walks both paths together to find the last matching node,
    instead of a single recursive traversal that finds the LCA directly."""
    root = build_tree(tree_list)

    def find_path(node, target, path):
        if node is None:
            return False
        path.append(node.val)
        if node.val == target:
            return True
        if find_path(node.left, target, path) or find_path(node.right, target, path):
            return True
        path.pop()
        return False

    path_p = []
    path_q = []
    find_path(root, p_val, path_p)
    find_path(root, q_val, path_q)

    lca = None
    for a, b in zip(path_p, path_q):
        if a == b:
            lca = a
        else:
            break
    return lca
