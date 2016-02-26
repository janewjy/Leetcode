class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = big = small = nums[0]        
        for i in nums[1:]:
            big, small = max(i,i*big,i*small), min(i,i*big,i*small)
            res = max(res,big)
        return res
# ??? go over again
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        