import math

def is_strong_number(n):
    if n <= 0:
        return False
    total = sum(math.factorial(int(d)) for d in str(n))
    return total == n