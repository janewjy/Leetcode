class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, val in enumerate(nums):
            if val not in dic:
                dic[val] = [index+1]
            else:
                dic[val].append(index+1)
        
        nums.sort()
        res = [0,1]
        i,j = 0, len(nums) -1
        while i < j:
            sumation = nums[i] + nums[j]
            if sumation == target:
                if nums[i] == nums[j]:
                    res = sorted(dic[nums[i]])
                else:
                    res = sorted([dic[nums[i]][0], dic[nums[j]][0]])
                
                return res
            
            if sumation > target:
                j -= 1
            else:
                i += 1
    
                    
            
# better on line solution:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in xrange(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i+1]
            else:
                dic[target-nums[i]] = i+1
        
