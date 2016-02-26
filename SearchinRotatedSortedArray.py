# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         pivot = 0
#         i = 0
#         j  = len(nums) - 1 
#         for k in xrange(len(nums)-1):
#             if nums[k] > nums[k+1]:
#                 pivot = k+1
#                 j = k
#                 break

        
#         res = bs(nums[pivot:]+nums[:pivot],target)
#         print res, pivot
#         if res == -1:
#             return res
#         if res + pivot >= len(nums)-2:
#             print 't'
#             res = (res+pivot)%len(nums)
#             return res
 
#         return res+pivot

# def bs(nums, target):
#     i = 0
#     j = len(nums)-1
#     while i <= j:
        
#         mid = (i + j)/2
#         if nums[mid] < target:
#             i = mid + 1 
#         elif target < nums[mid]:
#             j = mid - 1 
#         else:
#             return mid
#     return -1

# a = Solution()
# print a.search([4,5,6,7,0,1,2], 0)

[3,1]
1
[5,1,3]
1
        
[1]
0

[4,5,6,7,0,1,2]
0

# not sort solution

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
                return mid
            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1
        return -1

a = Solution()
print a.search([4,5,6,7,1,2,3], 1)