class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        current = 0
        for n in nums:
            if n:
                current += 1
            else:
                if current > consecutive:
                    consecutive = current
                current = 0
        return consecutive if consecutive > current else current

        