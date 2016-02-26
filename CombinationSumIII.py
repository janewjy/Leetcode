class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        cs(res,1,n,k,[])
        return res
        
def cs(res,index,n,k,path):
    if k == 0 and n == 0:
        res.append(path)
        return 
    if k > 0 and n>0:
        for i in xrange(index,10):
            if n-i>i or n-i == 0:
                cs(res,i+1,n-i,k-1,path+[i])