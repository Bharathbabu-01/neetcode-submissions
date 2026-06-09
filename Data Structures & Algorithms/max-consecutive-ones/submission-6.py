class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        reset = numCount = 0
        for i in nums:
            if i == 1:
                numCount += 1
                reset = max(reset, numCount)
            else:
                numCount = 0
        return reset
            