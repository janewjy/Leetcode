# backtracking solution
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        code = [0]
        gencode(code,n,0,1<<n)
        return code


def gencode(code,n,curr,size):
    if len(code) == size:
        return
    for i in xrange(n):
        mask = 1 << i
        el = curr^mask
        if el not in code:
            code.append(el)
            # print code
            gencode(code, n ,el,size)
            # print code
            if len(code) == size:
                return
            code.remove(el)
            # print code


# iteration solution???
    def grayCode(self, n):
        ans = [0]
        for i in xrange(n):
            for j in xrange(len(ans) - 1, -1, -1):
                print 1 << i,ans[j]
                ans.append(1 << i | ans[j])
                print ans
        return ans

a = Solution()
print a.grayCode(4)