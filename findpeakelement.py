def findPeakElement(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            # Peak left side mein ho sakti hai
            right = mid
        else:
            # Peak right side mein ho sakti hai
            left = mid + 1
            
    return left