class MyCircularQueue:
    """Optimal: a fixed-size preallocated array with head index and count,
    wrapping indices via modulo arithmetic. Every operation is O(1), with no
    shifting of elements (unlike list.pop(0))."""

    def __init__(self, k):
        self.capacity = k
        self.data = [None] * k
        self.head = 0
        self.count = 0

    def enQueue(self, value):
        if self.count >= self.capacity:
            return False
        tail = (self.head + self.count) % self.capacity
        self.data[tail] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        return self.data[self.head] if self.count else -1

    def Rear(self):
        if self.count == 0:
            return -1
        tail = (self.head + self.count - 1) % self.capacity
        return self.data[tail]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity


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
