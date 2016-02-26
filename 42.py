class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        partition_helper(res,[],s)
        return res


def partition_helper(res,subres,s):
    if not s:
        res.append(subres)
        return
    for i in xrange(1,len(s)+1):
        if isPalindrome(s[:i]):
            partition_helper(res,subres+[s[0:i]],s[i:])




def isPalindrome(s):
    for i in xrange(len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

print Solution().partition("ababababababababababababcbabababababababababababa")