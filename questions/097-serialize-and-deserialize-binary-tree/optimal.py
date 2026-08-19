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


def tree_to_level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def serialize(root):
    """Single preorder DFS pass, appending values (and '#' for nulls) directly
    to a list which is joined once at the end. O(n) time and space."""
    vals = []

    def helper(node):
        if node is None:
            vals.append('#')
            return
        vals.append(str(node.val))
        helper(node.left)
        helper(node.right)

    helper(root)
    return ','.join(vals)


def deserialize(data):
    """Single preorder DFS pass over an iterator of tokens, rebuilding the tree
    directly with no backtracking or rescanning. O(n) time and space."""
    tokens = iter(data.split(','))

    def helper():
        val = next(tokens)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node

    return helper()


def solve(tree_list):
    """Builds a tree from the input, serializes it, deserializes it back, and
    returns the round-tripped tree as a trimmed level-order list. Both
    serialize and deserialize are single O(n) preorder passes."""
    root = build_tree(tree_list)
    data = serialize(root)
    new_root = deserialize(data)
    return tree_to_level_order(new_root)
