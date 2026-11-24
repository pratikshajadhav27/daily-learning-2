def sum_odd_in_range(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            total += num
    return total