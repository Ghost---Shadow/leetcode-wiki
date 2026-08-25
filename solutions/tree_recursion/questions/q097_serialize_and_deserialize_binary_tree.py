"""Reshaper for questions/q097_serialize_and_deserialize_binary_tree.

Converts this question's (tree_list) -> list I/O into calls to the shared
preorder_serialize()/preorder_deserialize(): builds a tree, round-trips it
through the generic preorder token codec, then reads the rebuilt tree back
out as a trimmed level-order list.
"""
from .. import algorithm as _algorithm
preorder_serialize = _algorithm.preorder_serialize
preorder_deserialize = _algorithm.preorder_deserialize


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
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


def solve(tree_list):
    root = build_tree(tree_list)
    tokens = preorder_serialize(root, get_value=lambda n: str(n.val))
    new_root = preorder_deserialize(tokens, make_node=lambda v: TreeNode(int(v)))
    return tree_to_level_order(new_root)
