def is_neon_number(n):
    if n < 0:
        return False
    square = n * n
    digit_sum = sum(int(d) for d in str(square))
    return digit_sum == n