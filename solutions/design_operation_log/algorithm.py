def run_ops(cls, operations, arguments):
    """Generic LeetCode-judge operation-log replayer.

    `operations[0]` is always the constructor call (its name is whatever
    the judge calls the class -- irrelevant here, only its position
    matters), and each subsequent operations[i] names a *method* to call
    on the constructed instance with arguments[i]. Returns a list of
    per-operation results, with None standing in for the constructor slot
    and for any void method call.

    This is the shared shape behind every "design a data structure, then
    replay a sequence of operations against it" question: the interesting
    logic lives entirely in the class each reshaper supplies (LRUCache,
    MinStack, LFUCache, TimeMap, ...) -- this harness is just generic
    dispatch by method name via getattr, so no per-question if/elif chain
    is needed. It deliberately does *not* build on the _meta explore()
    engine: replaying mutating operations against one stateful object is
    not a graph-traversal problem, it's a plain sequential fold over the
    op log where the "state" is the object's own internal mutable state
    rather than anything explore's frontier discipline would help model.
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if obj is None:
            obj = cls(*args)
            results.append(None)
            continue
        method = getattr(obj, op)
        results.append(method(*args))
    return results
