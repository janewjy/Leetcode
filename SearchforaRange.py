# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         res = [-1, -1]
#         i = 0
#         j = len(nums) - 1

#         while i < j:
#             mid1 = mid2 = (i+j)/2
#             if nums[mid1] > target:
#                 j = mid1-1
#             elif nums[mid1] < target:
#                 i = mid1+1
#             else:
#                 while i < mid1:
#                     mid = (i+mid1)/2
#                     if nums[mid] != target:
#                         i = mid + 1
#                     else:
#                         mid1 = mid

#                 while  j > mid2:
#                     mid = (j+mid2)/2
#                     if nums[mid] != target:
#                         j = mid -1
#                     else:
#                         mid2 = mid
#                 return [mid1,mid2]
#         return res
[1,2,3,4,5,5,5,5,5,6,6,6,7]
5
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(nums)-1
        while i <= j:
            m =(i+j)/2
            if nums[m] > target:
                j = m-1
            elif nums[m] < target:
                i = m+1
            else:
                m1 = m2 = m
               
                while nums[i] != target or nums[j]!= target:
                    mm1 = (m1+i)/2
                    mm2 = (m2+j)/2
                    if nums[mm1]<target:
                        i = mm1+1
                    else:
                        m1 = mm1-1
                    if nums[mm2] > target:
                        j = mm2-1
                    else:
                        m2 = mm2+1
                return [i,j]
        return [-1,-1]

nums = [1,2,3,4,5,5,5,5,5,6,6,6,7]
target = 5

print Solution().searchRange([1,2],1)