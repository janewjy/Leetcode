class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        candidates.sort()
        cs(res,[],target,candidates,0)
        return res
        
def cs(res,subres,target,candidates,index):
    if target == 0:
        res.append(subres)
        return 
    if target>0:
        for i in xrange(index,len(candidates)):
            if i>index and candidates[i] == candidates[i-1]:
                continue
            cs(res,subres+[candidates[i]],target-candidates[i],candidates,i+1)
        
    
print Solution().combinationSum2([10,1,2,7,6,1,5],8)