def solve(digits):
    """Optimal: iterative backtracking that builds each combination
    incrementally, appending a completed combination to the result and
    backtracking (removing the last letter) rather than materializing the
    full Cartesian product up front. O(4^n * n) time (n = len(digits)),
    which is asymptotically optimal since that many combinations must be
    produced."""
    if not digits:
        return []

    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }

    result = []
    current = []

    def backtrack(index):
        if index == len(digits):
            result.append("".join(current))
            return
        for letter in mapping[digits[index]]:
            current.append(letter)
            backtrack(index + 1)
            current.pop()

    backtrack(0)
    return result
