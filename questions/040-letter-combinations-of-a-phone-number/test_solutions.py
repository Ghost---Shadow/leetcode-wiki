"""Runs against every solution file (*.py, excluding this file) in this directory.

Each solution file must expose: solve(digits) -> list[str]
(order of the returned combinations does not matter)
"""
import glob
import importlib.util
import os
import sys

TEST_CASES = [
    (("23",), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    (("",), []),
    (("2",), ["a", "b", "c"]),
    (("79",), ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]),
]


def load_solution_modules():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    modules = {}
    for filepath in sorted(glob.glob(os.path.join(dir_path, "*.py"))):
        name = os.path.basename(filepath)
        if name.startswith("test_"):
            continue
        spec = importlib.util.spec_from_file_location(name[:-3], filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "solve"):
            modules[name] = module
    return modules


def normalize(combos):
    return sorted(combos)


def run():
    modules = load_solution_modules()
    if not modules:
        print("No solution files found.")
        sys.exit(1)

    failures = 0
    for name, module in modules.items():
        for args, expected in TEST_CASES:
            (digits,) = args
            result = module.solve(digits)
            ok = normalize(result) == normalize(expected)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: solve({digits!r}) -> {result} (expected {expected})")
            if not ok:
                failures += 1

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run()
