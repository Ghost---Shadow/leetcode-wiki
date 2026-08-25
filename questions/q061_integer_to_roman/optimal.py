def solve(num):
    """Optimal: single greedy pass over a fixed value/symbol table, each
    entry consuming a bounded number of digits. O(1) time (bounded by input
    range), no wasted recomputation."""
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = []
    remaining = num
    for val, sym in values:
        if remaining <= 0:
            break
        count, remaining = divmod(remaining, val)
        if count:
            result.append(sym * count)
    return "".join(result)
