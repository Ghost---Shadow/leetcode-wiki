def post_order_fold(node, combine, empty):
    """Generic post-order binary-tree fold: recursively computes
    combine(node, left_result, right_result) bottom-up, where left_result
    and right_result are the (already-folded) results of node's children,
    or `empty` for a missing child. Returns `empty` for a None node without
    calling combine. O(n) time, O(h) recursion-stack space.

    This is tree-shaped recursion with a combine-on-return step, not a
    linear fold over a frontier, so -- per the taxonomy in
    solutions/README.md -- it does not build on the shared _meta.explore()
    engine; it is the standalone routine that engine explicitly doesn't
    cover.
    """
    if node is None:
        return empty
    left_result = post_order_fold(node.left, combine, empty)
    right_result = post_order_fold(node.right, combine, empty)
    return combine(node, left_result, right_result)


def preorder_serialize(node, get_value, null_token="#"):
    """Generic preorder tree serialization: visits `node` before its
    children, appending get_value(node) for every real node and
    `null_token` for every missing child, producing a token list that
    preorder_deserialize() can rebuild exactly. O(n) time/space.
    """
    tokens = []

    def helper(n):
        if n is None:
            tokens.append(null_token)
            return
        tokens.append(get_value(n))
        helper(n.left)
        helper(n.right)

    helper(node)
    return tokens


def preorder_deserialize(tokens, make_node, null_token="#"):
    """Inverse of preorder_serialize(): consumes `tokens` (as produced by a
    preorder walk, null children marked by `null_token`) and rebuilds the
    tree, calling make_node(value) to construct each real node and wiring
    up .left/.right by recursing in the same preorder shape. O(n)
    time/space.
    """
    it = iter(tokens)

    def helper():
        val = next(it)
        if val == null_token:
            return None
        node = make_node(val)
        node.left = helper()
        node.right = helper()
        return node

    return helper()
