class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums2 = list(nums)

        for i in range(1,len(nums)-1):
            nums[i] *= nums[i-1]
            nums2[-i-1] *= nums2[-i]
        res = list(nums)
        res[0] = nums2[1]
        res[-1] = nums[-2]

        for i in range(1,len(nums)-1):
            res[i] = nums[i-1]*nums2[i+1]
        return res

# O(1) space solution

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
        



a = Solution()
print a.productExceptSelf([2,3,5,7])
[1,2,3]

[1,0]