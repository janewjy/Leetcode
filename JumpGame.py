class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 1:
            return True
        i = 0
        step = 0
        far = 0
        while  i < len(nums):
            step = i + nums[i]
            far = max(step,far)
            if far >= len(nums)-1:
                return True
            if nums[i] == 0 and far <= i:
                return False
            i += 1
# online version
def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

a = Solution()
print a.canJump([3,2,1,0,4])
            