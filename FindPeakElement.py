class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        if len(nums) == 1:
            return 0
        for i in xrange(0,len(nums)):
            if i == 0 and nums[i+1] < nums[i]:
                return 0
            if i == len(nums)-1 and nums[i-1] < nums[i]:
                return i
            if nums[i]>nums[i-1] and nums[i] > nums[i+1]:
                return i
        