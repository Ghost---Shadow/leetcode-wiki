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
    """Naive preorder serialization: writes every value (and a '#' marker for
    every null child) into a single comma-joined string. Uses an explicit
    stack instead of recursion."""
    vals = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            vals.append("#")
            continue
        vals.append(str(node.val))
        stack.append(node.right)
        stack.append(node.left)
    return ",".join(vals)


def deserialize(data):
    """Rebuilds the tree from the comma-separated preorder token stream
    using an explicit stack of (node, next-side-to-fill) frames instead of
    recursion."""
    tokens = iter(data.split(","))

    def next_node():
        val = next(tokens)
        return None if val == "#" else TreeNode(int(val))

    root = next_node()
    if root is None:
        return None

    stack = [[root, "left"]]
    while stack:
        frame = stack[-1]
        node, side = frame
        child = next_node()
        if side == "left":
            node.left = child
            frame[1] = "right"
        else:
            node.right = child
            stack.pop()
        if child is not None:
            stack.append([child, "left"])

    return root


def solve(tree_list):
    """Builds a tree from the input, serializes it, deserializes it back, and
    returns the round-tripped tree as a trimmed level-order list."""
    root = build_tree(tree_list)
    data = serialize(root)
    new_root = deserialize(data)
    return tree_to_level_order(new_root)
