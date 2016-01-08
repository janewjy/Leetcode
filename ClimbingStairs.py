class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return rec({},n)
        
def rec(dic, n):
    if n in dic:
        return dic[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        v = rec(dic, n-1) + rec(dic, n-2)
    dic[n] = v
    return v

# bottom up DP
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        for k in range(1,n+1):
            if k == 1:
                v = 1
            elif k == 2:
                v = 2
            else:
                v = dic[k-2] + dic[k-1]
            dic[k] = v
        return dic[k]

