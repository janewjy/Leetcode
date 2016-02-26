class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pos = 0
        if nums:
            for cur in range(0,len(nums)-1):
                if nums[cur+1] != nums[cur]:
                    nums[pos+1] = nums[cur+1]
                    pos += 1
            return pos+1
        return 0
            
        
# 1-27         
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 0
        for i in xrange(len(nums)):
            if nums[i] != nums[j]:
                nums[i],nums[j+1] = nums[j+1],nums[i]
                j += 1
        return j+1
            
                 
            
        