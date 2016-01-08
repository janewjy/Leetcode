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
                    temp.append(sub[:j]+[i]+sub[j:])
            res = temp
        return res

    


    




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
        fres = []
        for i in xrange(len(nums)):
            res = self.permute(nums[:i]+nums[i+1:])
            fres += [s+[nums[i]] for s in res]
            
        return fres

# backtracking
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.wawa(nums,[],res)
        return(res)

    def wawa(self,nums,cur,res):
        if (len(nums) == 0):
            res.append(cur)
            return
        for i in range(len(nums)):            
            self.wawa(nums[:i]+nums[i+1:], cur+[nums[i]], res)
    


