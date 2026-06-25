class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]): 
        count = 0
        list=[]
        for num in nums:
            if num == 1:
                count += 1
            list.append(count)
            if num == 0:
                count = 0
        return max(list)