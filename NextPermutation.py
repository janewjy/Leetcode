class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in xrange(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                k = i
                break
            if k == -1:
                nums.reverse()
                return 
        l = -1
        for i in xrange(len(nums)-1,-1,-1):
            if nums[i] > nums[k]:
                l = i
                break
        nums[l],nums[k] = nums[k],nums[l]
        nums[k+1:] = nums[k+1:][::-1]
        
