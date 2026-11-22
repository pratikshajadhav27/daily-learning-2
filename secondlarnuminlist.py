def second_largest(nums):
    if len(nums) < 2:
        return None
    largest = second = float("-inf")
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return None if second == float("-inf") else second