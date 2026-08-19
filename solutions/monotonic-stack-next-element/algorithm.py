import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "meta_algorithm", os.path.join(_here, "..", "_meta", "algorithm.py"))
_meta = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_meta)
explore = _meta.explore


def next_dominant_index(values, dominates):
    """For every index i, finds the nearest index j > i such that
    dominates(values[j], values[i]) is True, using a single-pass monotonic
    stack. Returns a list `nxt` where nxt[i] is that index, or len(values)
    if no such index exists.

    This one routine powers both "next greater element" problems
    (dominates = lambda a, b: a > b) and "next smaller element" problems
    (dominates = lambda a, b: a < b) -- the whole family of monotonic-stack
    problems that ask "how far to the next element that beats this one".

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over the indices (a plain left fold), with the
    pending stack carried in the fold's accumulator.
    """
    n = len(values)
    nxt = [n] * n
    pending = []  # indices whose "next dominant" hasn't been found yet

    def transition(i):
        return (i + 1,) if i + 1 < n else ()

    for i in explore((0,) if n else (), transition):
        while pending and dominates(values[i], values[pending[-1]]):
            nxt[pending.pop()] = i
        pending.append(i)
    return nxt
