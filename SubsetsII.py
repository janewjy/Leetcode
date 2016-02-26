class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if path not in res:
            res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

a = Solution()
print a.subsetsWithDup([1,2,2])

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        subset(res,[],0,nums)
        return res
        
        
def subset(res,subres,index,nums):
    res.append(subres)
    for i in xrange(index,len(nums)):
        if i == index or nums[i] != nums[i-1]:
            subset(res,subres+[nums[i]],i+1,nums)
        
        