class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """Optimal LRU: hash map (key -> node) + doubly linked list for O(1) get/put.

    The linked list is kept in most-recently-used -> least-recently-used order,
    with sentinel head/tail nodes to avoid None-checks at the boundaries.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> _Node
        self.head = _Node()  # sentinel, head.next is MRU
        self.tail = _Node()  # sentinel, tail.prev is LRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_front(node)
            return
        if len(self.cache) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        node = _Node(key, value)
        self.cache[key] = node
        self._add_front(node)


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against LRUCache.

    operations[0] is always "LRUCache" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "LRUCache":
            obj = LRUCache(*args)
            results.append(None)
        elif op == "get":
            results.append(obj.get(*args))
        elif op == "put":
            obj.put(*args)
            results.append(None)
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
