class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end,i = -1,0
        l = len(nums)
        while i < l :
            if nums[i] != val:
                i += 1
            else:
                nums[i] = nums[end]
                end -= 1
                l -= 1
        return l

    # use python build in function is faster, why
    def removeElement(self, nums, val):
        for x in nums[:]:
            if x == val:
                nums.remove(val)
        return len(nums)
            
                