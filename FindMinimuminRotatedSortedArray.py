
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0,len(nums)-1
        while i<j:
            k = (i+j)/2
            if nums[k] < nums[j]:
                j = k
            else:
                i = k+1

        return nums[i]
# def mid(nums):
#     if not nums:
#         return
#     if len(nums) == 1:
#         return nums[0]
#     i,j = 0,len(nums)-1
#     mid = (i+j)/2
#     if nums[mid] > nums[i] and nums[nums]


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        