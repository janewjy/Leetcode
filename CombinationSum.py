class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        res = []
        fres = []

        bt(candidates,target,0,res,fres)
        return fres

def bt(candidates,target,index,res,fres):
    if target < 0:
        return 
    if target == 0:
        fres.append(res)
        return
    # ??? How to  stop running for loop when target <0
    for i in xrange(index, len(candidates)):
        bt(candidates,target - candidates[i], i,res+[candidates[i]],fres)
        


a = Solution()
print a.combinationSum([2,3,4,5],7)
