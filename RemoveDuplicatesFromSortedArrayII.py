class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return len(nums)
        
        pos = 1
        cur = 1
        
        while cur+1 < len(nums):
            if nums[cur] != nums[cur+1]:
                nums[pos+1] = nums[cur+1]
                pos += 1
                cur += 1
            else:
                if nums[cur+1] == nums[pos-1]:
                    cur += 1
                else:
                    nums[pos+1]  = nums[cur+1]
                    pos += 1
                    cur += 1
        return pos+1
                    
                
                
        
        