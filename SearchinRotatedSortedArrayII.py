# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: bool
#         """
#         if len(nums) == 1:
#             return target == nums[0]

#         for i in xrange(0,len(nums)-1):
#             if nums[i] > nums[i+1]:
#                 break
#             else:
#                 i += 1
#         return binarySearch(nums[i+1:]+nums[0:i+1],target)

# def binarySearch(nums,target):
#     n = len(nums)
#     i,j = 0,n-1
#     while  i <= j :
#         mid = (i+j)//2
#         if target > nums[mid]:
#             i = mid + 1
#         elif target < nums[mid]:
#             j = mid - 1

#         else:
#             return True
#     return False

nums = [4,5,6,7,7,8,1,1,1,2,3]
target = 7

nums = [1,3]
target = 1

# nums = [3,1]
# target = 1
# print Solution().search(nums,target)

# not sort first solution

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        i, j = 0, n-1

        while i <= j:

            mid = (i+j)//2
            if target == nums[mid]:
                return True
            
            if nums[i] < nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            elif nums[i] > nums[mid]:
                if nums[mid] < target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1
            else:
                i += 1
        return False

nums = [1,1,1,1,1,1,3,1,1,1]
target = 2

print Solution().search(nums,target)