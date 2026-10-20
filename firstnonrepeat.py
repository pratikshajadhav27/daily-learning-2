from collections import Counter
def firstUniqChar(s: str) -> int:
    c = Counter(s)
    return next((i for i, ch in enumerate(s) if c[ch] == 1), -1)