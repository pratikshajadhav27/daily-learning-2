def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    a, b = abs(a), abs(b)
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1