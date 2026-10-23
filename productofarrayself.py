def productExceptSelf(nums):
    res, p = [1] * len(nums), 1
    for i in range(len(nums)): res[i], p = p, p * nums[i]
    for i in range(len(nums) - 1, -1, -1): res[i] *= p; p *= nums[i]
    return res