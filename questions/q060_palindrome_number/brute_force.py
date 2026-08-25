def solve(x):
    """Brute-force: reverse the entire number via arithmetic and compare it
    to the original, instead of only reversing half the digits."""
    if x < 0:
        return False
    original = x
    reversed_num = 0
    n = x
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num == original
