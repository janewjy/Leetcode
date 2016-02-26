class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = n-1
        if target > nums[-1]:
            return n
        if target <= nums[0]:
            return 0
        while i <= j:
            mid = (j+i)//2
            if nums[mid] < target:
                i = mid+1
            elif nums[mid] > target:
                j = mid-1
            else:
                return mid

        return i



class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = n-1
        if target > nums[-1]:
            return n
        if target <= nums[0]:
            return 0
        while i < j-1:
            mid = (j+i)//2
            if nums[mid] < target:
                i = mid
            elif nums[mid] > target:
                j = mid
            else:
                return mid

        return i+1
# 2-6
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j = 0,len(nums)-1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return j+1
        
        while i<=j:
            mid = (i+j)/2
            if nums[mid] > target:
                j = mid-1
            elif nums[mid] == target:
                return mid
            else:
                i = mid+1
        return j+1