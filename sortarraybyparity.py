def sortArrayByParity(arr):
    # Even numbers ko aage aur odd numbers ko piche rakhna
    return [x for x in arr if x % 2 == 0] + [x for x in arr if x % 2 != 0]