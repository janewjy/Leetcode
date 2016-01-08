    class Solution(object):
        def jump(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            n = len(nums)
            cur_far = min(nums[0],n-1)
            next_far = 0
            step = 0
            for i in xrange(n):
                if i <= cur_far:
                    if next_far< i+nums[i]:
                        next_far = min(i+nums[i],n-1)
                    if i == cur_far and cur_far != 0:
                        cur_far = next_far
                        step += 1
    
            return step