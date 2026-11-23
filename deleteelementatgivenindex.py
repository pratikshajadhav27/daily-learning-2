def deleteAtIndex(arr: List[int], P: int) -> List[int]:
    # Shift elements after index P one position to the left
    for i in range(P, len(arr) - 1):
        arr[i] = arr[i + 1]

    # Fill the last position with 0 to keep array size unchanged
    if len(arr) > 0:
        arr[-1] = 0

    return arr