"""Verifies that every question adapter in questions/ correctly reshapes its
problem-specific operation log onto the shared run_ops() harness in
algorithm.py.
"""
import importlib
import pkgutil
import sys
from pathlib import Path

if __package__ in (None, ""):
    _file = Path(__file__).resolve()
    _repo_root = _file.parents[2]
    sys.path.insert(0, str(_repo_root))
    __package__ = ".".join(_file.parent.relative_to(_repo_root).parts)
    importlib.import_module(__package__)

# Exact-equality cases: (operations, arguments) -> expected results list.
TEST_CASES = {
    "q002_lru_cache.py": [
        (
            (
                ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            ),
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
        (
            (
                ["LRUCache", "put", "get", "put", "get", "get"],
                [[1], [1, 1], [1], [2, 2], [1], [2]],
            ),
            [None, None, 1, None, -1, 2],
        ),
    ],
    "q036_min_stack.py": [
        (
            (
                ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[], [-2], [0], [-3], [], [], [], []],
            ),
            [None, None, None, None, -3, None, 0, -2],
        ),
        (
            (
                ["MinStack", "push", "push", "getMin", "pop", "getMin"],
                [[], [1], [2], [], [], []],
            ),
            [None, None, None, 1, None, 1],
        ),
    ],
    "q055_lfu_cache.py": [
        (
            (
                ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
            ),
            [None, None, None, 1, None, -1, 3, None, -1, 3, 4],
        ),
    ],
    "q057_time_based_key_value_store.py": [
        (
            (
                ["TimeMap", "set", "get", "get", "set", "get", "get"],
                [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
                 ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
            ),
            [None, None, "bar", "bar", None, "bar2", "bar2"],
        ),
        (
            (
                ["TimeMap", "set", "get"],
                [[], ["a", "1", 1], ["a", 0]],
            ),
            [None, None, ""],
        ),
    ],
    "q084_design_hit_counter.py": [
        (
            (
                ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"],
                [[], [1], [2], [3], [4], [300], [300], [301]],
            ),
            [None, None, None, None, 3, None, 4, 3],
        ),
    ],
    "q091_logger_rate_limiter.py": [
        (
            (
                [
                    "Logger",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                ],
                [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]],
            ),
            [None, True, True, False, False, False, True],
        ),
    ],
    "q099_design_circular_queue.py": [
        (
            (
                [
                    "MyCircularQueue",
                    "enQueue",
                    "enQueue",
                    "enQueue",
                    "enQueue",
                    "Rear",
                    "isFull",
                    "deQueue",
                    "enQueue",
                    "Rear",
                ],
                [[3], [1], [2], [3], [4], [], [], [], [4], []],
            ),
            [None, True, True, True, False, 3, True, True, True, 4],
        ),
        (
            (
                ["MyCircularQueue", "isEmpty", "enQueue", "isEmpty", "isFull", "deQueue", "isEmpty"],
                [[1], [], [5], [], [], [], []],
            ),
            [None, True, True, False, True, True, True],
        ),
    ],
}

# Membership-checked case: RandomizedSet's getRandom() is nondeterministic,
# so exact equality won't hold -- verify deterministic ops exactly and
# verify every getRandom() result is currently a member of the set.
RANDOMIZED_SET_CASES = [
    (
        ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
        [[], [1], [2], [2], [], [1], [2], []],
        [None, True, False, True, "RANDOM", True, False, "RANDOM"],
    ),
    (
        ["RandomizedSet", "insert", "insert", "insert", "remove", "getRandom", "insert", "getRandom"],
        [[], [1], [2], [3], [2], [], [4], []],
        [None, True, True, True, True, "RANDOM", True, "RANDOM"],
    ),
]

# Distribution-checked case: Solution.pickIndex() is randomized -- verify
# every pick is in range and the empirical distribution roughly tracks the
# given weights over a large batch.
NUM_TRIALS = 4000
TOLERANCE = 0.08
WEIGHT_CASES = [
    [1, 3],
    [1],
    [1, 1, 1, 1],
    [5, 1, 1, 1],
]


def load_question_modules():
    modules = {}
    questions_dir = Path(__file__).resolve().parent / "questions"
    for info in pkgutil.iter_modules([str(questions_dir)]):
        if info.name == "__init__":
            continue
        module = importlib.import_module(f".questions.{info.name}", package=__package__)
        modules[f"{info.name}.py"] = module
    return modules


def check_randomized_set(operations, arguments, results, expected):
    contents = set()
    for op, args, result, exp in zip(operations, arguments, results, expected):
        if op == "RandomizedSet":
            continue
        elif op == "insert":
            (val,) = args
            should_add = val not in contents
            if result != exp:
                return False
            if should_add:
                contents.add(val)
        elif op == "remove":
            (val,) = args
            should_remove = val in contents
            if result != exp:
                return False
            if should_remove:
                contents.discard(val)
        elif op == "getRandom":
            if result not in contents:
                return False
    return True


def check_weight_distribution(weights, results):
    n = len(weights)
    for idx in results:
        if not isinstance(idx, int) or idx < 0 or idx >= n:
            return False
    total = sum(weights)
    expected_props = [w / total for w in weights]
    counts = [0] * n
    for idx in results:
        counts[idx] += 1
    observed_props = [c / len(results) for c in counts]
    return all(abs(observed_props[i] - expected_props[i]) <= TOLERANCE for i in range(n))


def run():
    modules = load_question_modules()
    if not modules:
        print("No question adapters found.")
        sys.exit(1)

    failures = 0

    for name, module in modules.items():
        if name == "q034_insert_delete_getrandom_o_1.py":
            continue
        if name == "q083_random_pick_with_weight.py":
            continue
        for args, expected in TEST_CASES.get(name, []):
            operations, arguments = args
            result = module.solve(list(operations), [list(a) for a in arguments])
            ok = result == expected
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve(...) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    randomized_set_module = modules.get("q034_insert_delete_getrandom_o_1.py")
    if randomized_set_module is not None:
        for operations, arguments, expected in RANDOMIZED_SET_CASES:
            result = randomized_set_module.solve(list(operations), [list(a) for a in arguments])
            ok = len(result) == len(expected) and check_randomized_set(operations, arguments, result, expected)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] q034_insert_delete_getrandom_o_1.py: solve(...) -> {result} (expected shape {expected})")
            if not ok:
                failures += 1

    weight_module = modules.get("q083_random_pick_with_weight.py")
    if weight_module is not None:
        for weights in WEIGHT_CASES:
            operations = ["Solution"] + ["pickIndex"] * NUM_TRIALS
            arguments = [[list(weights)]] + [[] for _ in range(NUM_TRIALS)]
            outputs = weight_module.solve(list(operations), [list(a) for a in arguments])
            ok = outputs[0] is None and check_weight_distribution(weights, outputs[1:])
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] q083_random_pick_with_weight.py: pickIndex distribution for weights={weights}")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
