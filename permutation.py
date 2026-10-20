from itertools import permutations
def permuteString(s: str):
    return [''.join(p) for p in permutations(s)]