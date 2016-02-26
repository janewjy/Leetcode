
class Solution(object):
    def missingNumber(self, nums):
        
        n = len(nums)
        for ind in xrange(n):
            
            while  ind!=nums[ind] and nums[ind]<n and nums[ind]!= nums[nums[ind]]:
                print ind,nums[ind]                
                nums[nums[ind]],nums[ind] = nums[ind], nums[nums[ind]]
                print ind,nums[ind]
                
        for ind in xrange(n):
            if ind != nums[ind]:
                return ind
        return n


nums = [2,0]

ind = 1

nums[ind],nums[nums[ind]] = nums[nums[ind]], nums[ind]
print  nums[nums[ind]], nums[ind]

# nums[nums[ind]],nums[ind] = nums[ind], nums[nums[ind]]
# print nums

# print Solution().missingNumber([2,0])


# 2-5
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            while nums[i] != i and nums[i]<len(nums):
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
        for i,j in enumerate(nums):
            if i != j:
                return i
        return len(nums)