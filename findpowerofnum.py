def power_of_num(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result