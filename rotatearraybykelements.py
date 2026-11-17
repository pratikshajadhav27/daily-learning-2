def rotate(arr, k):
    k = k % len(arr)
    # Piche ke k elements ko aage le aana aur baaki ko piche
    return arr[-k:] + arr[:-k]