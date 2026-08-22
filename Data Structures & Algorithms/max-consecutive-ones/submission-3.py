class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        run_max = 0
        for n in nums:
            if n:
                run_max += 1
            else:
                res = max(res,run_max)
                run_max = 0
        return max(res,run_max)

        