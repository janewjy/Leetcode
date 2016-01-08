class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort() 
        k = 0
        diff = float('inf')
        while k < len(nums)-2:
            j = len(nums) - 1
            i = k + 1 
            while  i < j:
                if abs(nums[i] + nums[j] + nums[k] - target) < diff:
                    diff = abs(nums[i] + nums[j] + nums[k] - target)
                    res = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                elif nums[i] + nums[j] + nums[k] > target:
                    j -= 1
                else:
                    i += 1
            k += 1 
        return res
               

a = Solution()
print a.threeSumClosest([0,1,2],3)