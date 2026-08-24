class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            mid = start + ((end - start) // 2)
            n = nums[mid]
            if n == target:
                return mid
            elif n > target:
                end = mid
            else:
                start = mid + 1
        return -1