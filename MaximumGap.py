class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
            
        nums.sort()
        i = 1
        result = 0
        while i < n:
            temp = nums[i] - nums[i-1]
            if temp >= result:
                result = temp
            i += 1
        
        return result       

#radix sort version

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        nums = radix(nums)
        i = 1
        result = 0
        for i in xrange(n):
            if nums[i]-nums[i-1] > result:
                result = nums[i]-nums[i-1]
        return result
            
            
        
def radix(alist):
    for k in xrange(20):
        s = [[] for x in xrange(10)]
        for i in alist:
            s[i/10**k%10].append(i)
        alist = [a for b in s for a in b]
    return alist
            
