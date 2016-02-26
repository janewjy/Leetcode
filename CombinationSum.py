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

# 2-8
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        bk([],res,target,candidates)
        return res

def bk(path,res,target,cddt):
    if target == 0:
        path.sort()
        if path not in res:
            res.append(path)
        return 
    for i in cddt:
        if target - i >= 0:
            bk(path+[i],res,target-i,cddt)

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        bk([],res,target,candidates,0)
        return res

def bk(path,res,target,cddt,index):
    
    if target == 0:
        res.append(path)
        return 
    for i in xrange(index,len(cddt)):
        if target - i >= 0:
            bk(path+[cddt[i]],res,target-cddt[i],cddt,i)
            
            