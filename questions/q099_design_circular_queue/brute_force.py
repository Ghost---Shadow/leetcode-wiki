class MyCircularQueue:
    """Brute-force: backs the queue with a plain Python list, using append and
    pop(0) (O(n) dequeue due to shifting), instead of a fixed-size array with
    head/tail index arithmetic for O(1) operations."""

    def __init__(self, k):
        self.capacity = k
        self.data = []

    def enQueue(self, value):
        if len(self.data) >= self.capacity:
            return False
        self.data.append(value)
        return True

    def deQueue(self):
        if not self.data:
            return False
        self.data.pop(0)
        return True

    def Front(self):
        return self.data[0] if self.data else -1

    def Rear(self):
        return self.data[-1] if self.data else -1

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.capacity


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against MyCircularQueue.

    operations[0] is always "MyCircularQueue" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "MyCircularQueue":
            obj = MyCircularQueue(*args)
            results.append(None)
        elif op == "enQueue":
            results.append(obj.enQueue(*args))
        elif op == "deQueue":
            results.append(obj.deQueue())
        elif op == "Front":
            results.append(obj.Front())
        elif op == "Rear":
            results.append(obj.Rear())
        elif op == "isEmpty":
            results.append(obj.isEmpty())
        elif op == "isFull":
            results.append(obj.isFull())
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
