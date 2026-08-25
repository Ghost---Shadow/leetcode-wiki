class Logger:
    """Optimal: a hash map from message to the timestamp it was last printed.
    Each call is a single O(1) dict lookup/update instead of rescanning a log."""

    def __init__(self):
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp, message):
        last = self.last_printed.get(message)
        if last is not None and timestamp - last < 10:
            return False
        self.last_printed[message] = timestamp
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
