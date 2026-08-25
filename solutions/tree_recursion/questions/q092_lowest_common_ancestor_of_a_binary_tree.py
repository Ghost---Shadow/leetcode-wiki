"""Reshaper for questions/q092_lowest_common_ancestor_of_a_binary_tree.

Converts this question's (tree_list, p_val, q_val) -> value I/O into a call
to the shared post_order_fold(): combine(node, left_found, right_found)
returns node itself once node is p or q (or once both children reported a
find), otherwise propagates whichever side (if any) found something.
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
    root = build_tree(tree_list)

    def combine(node, left_found, right_found):
        if node.val == p_val or node.val == q_val:
            return node
        if left_found and right_found:
            return node
        return left_found if left_found else right_found

    result = post_order_fold(root, combine, empty=None)
    return result.val if result else None
