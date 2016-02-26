class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in xrange(n):
            while nums[i]>0 and nums[i] <= n and nums[nums[i] -1 ]!=nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        for i in xrange(n):
            if nums[i] != i +1:
                return i+1
        return n+1

print Solution().firstMissingPositive([-1,1,2,3])