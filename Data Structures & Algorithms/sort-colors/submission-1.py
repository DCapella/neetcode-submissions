class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = 0
        for i in range(len(nums)):
            n = nums[i]
            nums[i] = 2
            if n < 2:
                nums[one] = 1
                one += 1
            if n < 1:
                nums[zero] = 0
                zero += 1