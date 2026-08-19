class MinStack:
    """Optimal: maintain an auxiliary stack that tracks the minimum seen so
    far at each depth. Every push also pushes the new running minimum onto
    the min-stack; every pop pops both stacks in lockstep. getMin() is then
    just a peek. All operations O(1) time, O(n) extra space."""

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val):
        self.data.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.data.pop()
        self.min_stack.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.min_stack[-1]


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
