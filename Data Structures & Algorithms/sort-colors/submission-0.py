class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapping = {key:0 for key in range(3)}
        for n in nums:
            mapping[n] += 1

        for i in range(len(nums)):
            if mapping[0]:
                nums[i] = 0
                mapping[0] -= 1
            elif mapping[1]:
                nums[i] = 1
                mapping[1] -= 1
            else:
                nums[i] = 2
                mapping[2] -= 1

            
        