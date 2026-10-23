def returnLargestDigit(n):
    # Convert n to a string, find the maximum character (digit), and convert it back to an integer
    return int(max(str(n)))