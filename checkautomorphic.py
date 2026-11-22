def is_automorphic(n):
    if n < 0:
        return False
    square_str = str(n * n)
    num_str = str(n)
    return square_str.endswith(num_str)