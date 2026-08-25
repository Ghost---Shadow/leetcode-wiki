class _Node:
    __slots__ = ("key", "value", "freq", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class _DoublyLinkedList:
    """A sentinel-bounded doubly linked list holding all keys at one frequency,
    ordered most-recently-used at the front (right after head)."""

    def __init__(self):
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1

    def pop_lru(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

    def is_empty(self):
        return self.size == 0


class LFUCache:
    """True O(1) get/put LFU cache: a hashmap key -> node for O(1) lookup, plus a
    hashmap freq -> doubly-linked-list of nodes at that frequency (MRU-ordered
    within each bucket), plus a running min_freq pointer -- so both get and put
    are O(1) with no scanning."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = {}
        self.min_freq = 0

    def _bump(self, node):
        old_freq = node.freq
        self.freq_map[old_freq].remove(node)
        if self.freq_map[old_freq].is_empty():
            del self.freq_map[old_freq]
            if self.min_freq == old_freq:
                self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = _DoublyLinkedList()
        self.freq_map[node.freq].add_front(node)

    def get(self, key):
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._bump(node)
        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._bump(node)
            return

        if len(self.key_map) >= self.capacity:
            lfu_list = self.freq_map[self.min_freq]
            evicted = lfu_list.pop_lru()
            del self.key_map[evicted.key]
            if lfu_list.is_empty():
                del self.freq_map[self.min_freq]

        node = _Node(key, value)
        self.key_map[key] = node
        if 1 not in self.freq_map:
            self.freq_map[1] = _DoublyLinkedList()
        self.freq_map[1].add_front(node)
        self.min_freq = 1


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against LFUCache.

    operations[0] is always "LFUCache" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "LFUCache":
            obj = LFUCache(*args)
            results.append(None)
        elif op == "get":
            results.append(obj.get(*args))
        elif op == "put":
            obj.put(*args)
            results.append(None)
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
