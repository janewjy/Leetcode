class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums:
            self.dp = [0]*len(nums)
            self.dp[0] = nums[0]
            
            for i in xrange(1,len(nums)):
                self.dp[i] = self.dp[i-1] + nums[i]
            print self.dp
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i-1 < 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]
        
        
nums = [-2,0,3,-5,2,-1]
# Your NumArray object will be instantiated and called as such:
numArray = NumArray(nums)
print numArray.sumRange(0, 2)
numArray.sumRange(1, 2)