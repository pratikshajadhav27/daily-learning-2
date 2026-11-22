def is_spy_number(n):
    if n < 0:
        return False
    digit_sum = 0
    digit_product = 1
    for ch in str(n):
        d = int(ch)
        digit_sum += d
        digit_product *= d
    return digit_sum == digit_product