class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for index,i in enumerate(nums):
            while i < len(nums) and index != nums[index] :
                temp = nums[i]
                nums[i] = i
                i = temp
                index = temp
        print nums
        for index, i in enumerate(nums):
            if i != index:
                return index
        return len(nums)
        
print Solution().missingNumber([1,0])