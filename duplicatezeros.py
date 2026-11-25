def duplicateZeros(arr: List[int]) -> List[int]:
    n = len(arr)
    temp = []

    for x in arr:
        temp.append(x)
        if x == 0:
            temp.append(0)

    # Original length tak slice karke arr ko update karna
    arr[:] = temp[:n]
    return arr