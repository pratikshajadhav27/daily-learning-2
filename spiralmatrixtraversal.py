def spiralOrder(matrix):
    res = []
    while matrix:
        res.extend(matrix.pop(0))
        matrix = [*zip(*matrix)][::-1]
    return res