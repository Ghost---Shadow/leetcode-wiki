"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(operations, arguments) -> list
following the LeetCode-judge replay format, e.g.:
    operations = ["Solution", "pickIndex", "pickIndex", ...]
    arguments  = [[[1, 3]], [], [], ...]

pickIndex() is randomized, so we can't assert exact values. Instead we
check that every returned index is in range, and (for a large batch) that
the empirical pick frequency roughly tracks the given weights.
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

NUM_TRIALS = 4000
TOLERANCE = 0.08  # allowed absolute deviation in empirical proportion

TEST_CASES = [
    [1, 3],
    [1],
    [1, 1, 1, 1],
    [5, 1, 1, 1],
]


def load_solution_modules():
    modules = {}
    for info in pkgutil.iter_modules([str(Path(__file__).resolve().parent)]):
        if info.name.startswith("test_") or info.name == "__init__":
            continue
        module = importlib.import_module(f".{info.name}", package=__package__)
        if hasattr(module, "solve"):
            modules[f"{info.name}.py"] = module
    return modules


def check(weights, results):
    n = len(weights)
    # every picked index must be a valid index into weights
    for idx in results:
        if not isinstance(idx, int) or idx < 0 or idx >= n:
            return False, f"index {idx} out of range for weights of length {n}"

    total = sum(weights)
    expected_props = [w / total for w in weights]

    counts = [0] * n
    for idx in results:
        counts[idx] += 1
    observed_props = [c / len(results) for c in counts]

    for i in range(n):
        if abs(observed_props[i] - expected_props[i]) > TOLERANCE:
            return False, (
                f"index {i}: observed proportion {observed_props[i]:.3f} "
                f"deviates too much from expected {expected_props[i]:.3f}"
            )
    return True, ""


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for weights in TEST_CASES:
            operations = ["Solution"] + ["pickIndex"] * NUM_TRIALS
            arguments = [[list(weights)]] + [[] for _ in range(NUM_TRIALS)]
            outputs = module.solve(list(operations), [list(a) for a in arguments])

            if outputs[0] is not None:
                ok, reason = False, "constructor call should return None"
            else:
                ok, reason = check(weights, outputs[1:])

            status = "PASS" if ok else "FAIL"
            suffix = f" ({reason})" if reason else ""
            print(f"[{status}] {name}: pickIndex distribution for weights={weights}{suffix}")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
