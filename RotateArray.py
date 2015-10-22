class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        l = len(nums)
        k = k % l
    
        if l > 1 and k != 0:
            l = len(nums)
            k = k % l
    
            latter_half = nums[-k:]
            first_half = nums[:l-k]
            
            nums[:] = latter_half + first_half

        

class Solution:
    def rotate(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1