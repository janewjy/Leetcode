class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index,n in enumerate(nums):
            while n != index and n>=0:
                nums[n],nums[index] = nums[index], nums[n]


Solution().firstMissingPositive([1,2,3])