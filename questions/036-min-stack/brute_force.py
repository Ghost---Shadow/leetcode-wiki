class MinStack:
    """Brute-force: getMin() rescans the entire stack for the minimum every
    call, instead of maintaining an auxiliary min-tracking stack for O(1) getMin."""

    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return min(self.data)


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against MinStack.

    operations[0] is always "MinStack" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "MinStack":
            obj = MinStack()
            results.append(None)
        elif op == "push":
            obj.push(*args)
            results.append(None)
        elif op == "pop":
            obj.pop()
            results.append(None)
        elif op == "top":
            results.append(obj.top())
        elif op == "getMin":
            results.append(obj.getMin())
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
