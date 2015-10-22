class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = 0
        end = len(nums) - 1
        while n < len(nums):
            if n == end:
                break
            if nums[n] == 0:
                nums.pop(n)
                nums.append(0)
                end -= 1
                n -= 1
            n += 1
            
            
                