class Solution(object):
    # too slow
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l < 3:
            return []
        triple = []
        nums.sort()
        for i in range(l):
            for j in range(i+1, l):
                v = 0 - nums[i] - nums[j]
                if v in nums[j+1:] and [nums[i], nums[j], v] not in triple:
                    triple.append([nums[i], nums[j], v])
                
        return triple
            
        
        
        
        