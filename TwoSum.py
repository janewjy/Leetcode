class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index in range(len(nums)):
            if nums[index] in dic:
                return [dic[nums[index]]+1, index+1]
            num = target-nums[index]    
            dic[num] = index


    def twoSum2(self, nums, target):
        #Time Limit Exceeded 
        for index in range(len(nums)):
            n = target - nums[index]
            try:
                nIndex = nums[index+1:].index(n)
                return [index+1, nIndex+index+2]
            except:
                continue


             
            
            
            
            