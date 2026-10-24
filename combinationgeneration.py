from itertools import combinations
def combine(n: int, k: int):
    return [list(c) for c in combinations(range(1, n + 1), k)]