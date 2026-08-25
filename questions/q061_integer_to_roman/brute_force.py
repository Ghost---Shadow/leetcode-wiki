def solve(num):
    """Brute-force: recompute the greedy value/symbol conversion from
    scratch for every integer from 1 up to num, keeping only the final
    result. O(num) instead of the O(1) single-pass conversion."""
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = ""
    for n in range(1, num + 1):
        result = ""
        remaining = n
        for val, sym in values:
            while remaining >= val:
                result += sym
                remaining -= val
    return result
