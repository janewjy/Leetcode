class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1]*n
        res = 1
        for i in xrange(1,n):
            subres = 1
            for j in xrange(i):
                if nums[i]>nums[j]:
                    subres = dp[j]+1
                dp[i] = max(subres,dp[i])
            res = max(res,dp[i])
        return res
            
        
            

def lengthOfLIS(self, nums):
    if not nums: return 0
    c=[nums[0]]
    for i in nums:
        if i<=c[0]:
            c[0]=i
        elif i>c[-1]:
            c+=i,
        else:
            index=self.bs(c ,0, len(c), i)
            c[index]=min(i, c[index])
    return len(c)

def bs(self, nums, l, r, key):
    while r-l>1:
        m=(r+l)/2
        if nums[m]>=key:
            r=m
        else:
            l=m
    return r