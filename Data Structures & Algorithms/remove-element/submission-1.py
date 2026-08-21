class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        diff = len(nums)
        while i < diff:
            if nums[i] == val:
                diff -= 1
                nums[i] = nums[diff]
            else:
                i += 1
        return diff