def solve(digits):
    """Brute-force: generate the full Cartesian product of all letter choices
    up front via itertools.product (materializing every combination at once)
    instead of incrementally building combinations with backtracking."""
    import itertools

    if not digits:
        return []

    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }

    letter_groups = [mapping[d] for d in digits]
    combinations = itertools.product(*letter_groups)
    return ["".join(combo) for combo in combinations]
