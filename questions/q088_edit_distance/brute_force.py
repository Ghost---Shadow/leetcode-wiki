def solve(word1, word2):
    """Brute-force, no memoization: explores every insert/delete/replace
    sequence by materializing the exact same exponential recursion tree as
    explicit node objects (so identical (i, j) states reached via different
    paths are NOT deduplicated) and combining bottom-up, instead of using
    the call stack. Exponential time, same as the recursive version."""

    class Node:
        __slots__ = ("i", "j", "children", "value")

        def __init__(self, i, j):
            self.i = i
            self.j = j
            self.children = []
            self.value = None

    root = Node(0, 0)
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        i, j = node.i, node.j
        if i == len(word1) or j == len(word2):
            continue
        if word1[i] == word2[j]:
            child = Node(i + 1, j + 1)
            node.children = [child]
            stack.append(child)
        else:
            children = [Node(i + 1, j), Node(i, j + 1), Node(i + 1, j + 1)]
            node.children = children
            stack.extend(children)

    for node in reversed(order):
        i, j = node.i, node.j
        if i == len(word1):
            node.value = len(word2) - j
        elif j == len(word2):
            node.value = len(word1) - i
        elif word1[i] == word2[j]:
            node.value = node.children[0].value
        else:
            node.value = 1 + min(child.value for child in node.children)

    return root.value
