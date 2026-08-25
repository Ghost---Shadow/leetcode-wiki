"""Reshaper for questions/q085_binary_tree_maximum_path_sum.

Converts this question's (values) -> int I/O into a call to the shared
post_order_fold(): combine(node, left_gain, right_gain) updates a running
best "path bends through node" total as a side effect and returns the best
downward gain from node, so a single fold both computes and returns it.
"""
from .. import algorithm as _algorithm
post_order_fold = _algorithm.post_order_fold


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
    root = build_tree(values)
    if root is None:
        return 0

    best = float("-inf")

    def combine(node, left_gain, right_gain):
        nonlocal best
        left_gain = max(left_gain, 0)
        right_gain = max(right_gain, 0)
        best = max(best, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    post_order_fold(root, combine, empty=0)
    return best
