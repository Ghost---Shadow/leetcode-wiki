import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "meta_algorithm", os.path.join(_here, "..", "_meta", "algorithm.py"))
_meta = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_meta)
explore = _meta.explore


def running_fold_best(values, init_state, step, extract):
    """Generalized Kadane's algorithm: a single left-to-right pass carrying
    an arbitrary `state` forward via `step(state, value) -> new_state`, and
    tracking the best value seen so far via `extract(state)`.

    Maximum Subarray uses state = running max ending here (a plain number).
    Maximum Product Subarray uses state = (running max, running min) ending
    here, since a negative running min times a negative number can flip
    into the new running max. Both are "carry forward the best-ending-here
    value(s), take the global best across the whole pass" -- this one
    routine is the shared shape.

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over indices 1..n-1 (a plain left fold),
    carrying (state, best) in the fold's accumulator.
    """
    state = init_state(values[0])
    best = extract(state)

    def transition(i):
        return (i + 1,) if i + 1 < len(values) else ()

    for i in explore((1,) if len(values) > 1 else (), transition):
        state = step(state, values[i])
        candidate = extract(state)
        if candidate > best:
            best = candidate
    return best
