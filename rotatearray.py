class Solution:
    def rotateArray(self, arr: List[int], r: int) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr

        r %= n
        arr[:] = arr[-r:] + arr[:-r] if r else arr
        return arr