def solve(nums):
    """Brute-force: for each candidate 1, 2, 3, ... check membership with a
    linear scan ('in' on a list), O(n) per check and O(n^2) overall instead
    of the O(n) in-place index-marking approach."""
    candidate = 1
    while True:
        if candidate not in nums:
            return candidate
        candidate += 1
