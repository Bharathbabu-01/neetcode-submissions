class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        reset = count = 0
        list=[]
        for num in nums:
            if num == 1:
                count += 1
                list.append(count)
            if num == 0:
                reset = count = 0
                list.append(count)
        return max(list)
