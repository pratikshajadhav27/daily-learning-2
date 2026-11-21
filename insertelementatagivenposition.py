def insertAtPosition(arr: List[int], X: int, P: int) -> List[int]:
    if not arr:
        return []
    return arr[:P] + [X] + arr[P:-1]