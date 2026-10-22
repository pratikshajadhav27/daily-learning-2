import heapq
def findKthLargest(nums, k) -> int:
    return heapq.nlargest(k, nums)[-1]