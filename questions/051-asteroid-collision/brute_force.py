def solve(asteroids):
    """Brute-force: repeatedly rescans the whole list left-to-right looking for any
    adjacent right-moving/left-moving collision pair, resolves just that one
    collision, then restarts the scan from the beginning -- O(n^2) instead of a
    single-pass stack simulation."""
    arr = list(asteroids)
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(arr) - 1:
            if arr[i] > 0 and arr[i + 1] < 0:
                a, b = arr[i], arr[i + 1]
                if a == -b:
                    del arr[i + 1]
                    del arr[i]
                elif a > -b:
                    del arr[i + 1]
                else:
                    del arr[i]
                changed = True
                break
            i += 1
    return arr
