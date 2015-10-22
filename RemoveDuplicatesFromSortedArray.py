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
            
        
                
            
        