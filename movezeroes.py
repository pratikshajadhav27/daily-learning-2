from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        pos = 0

        # Step 1: Move all non-zero elements forward
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1

        # Step 2: Fill the remaining positions with 0
        for i in range(pos, len(nums)):
            nums[i] = 0

        return nums