class Logger:
    """Brute-force: keeps a flat log of every (timestamp, message) pair and
    linearly rescans it backwards on each call, O(n) per call, instead of a
    hash map keyed by message that gives O(1) lookups."""

    def __init__(self):
        self.log = []

    def shouldPrintMessage(self, timestamp, message):
        for t, m in reversed(self.log):
            if m == message:
                if timestamp - t < 10:
                    return False
                break
        self.log.append((timestamp, message))
        return True


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against Logger.

    operations[0] is always "Logger" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "Logger":
            obj = Logger()
            results.append(None)
        elif op == "shouldPrintMessage":
            results.append(obj.shouldPrintMessage(*args))
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
