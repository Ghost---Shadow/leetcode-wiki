def solve(s):
    """Brute-force: repeatedly rescans the whole value list from the start merging
    the first adjacent subtractive pair (e.g. IV, IX) it finds into its combined
    value, one merge per pass -- O(n^2) instead of a single O(n) left-to-right pass."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    nums = [values[ch] for ch in s]
    merged = True
    while merged:
        merged = False
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                nums[i:i + 2] = [nums[i + 1] - nums[i]]
                merged = True
                break
            i += 1
    return sum(nums)
