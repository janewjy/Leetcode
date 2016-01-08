class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        res = [[nums[0]]]
        for i in nums[1:]:
            temp = []
            for sub in res:
                for j in xrange(len(sub)+1):
                    if sub[:j]+[i]+sub[j:] not in temp:
                        temp.append(sub[:j]+[i]+sub[j:])
            res = temp
        return res

    


[1,1,0,0,1,-1,-1,1]
[3,3,1,2,3,2,3,1]
[3,3,0,0,2,3,2]