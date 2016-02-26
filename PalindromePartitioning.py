class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        back_track(s,res,[])
        return res
def  back_track(s, res, sub):
    for i in xrange(1,len(s)+1):
        if check(s[0:i]):
            sub.append(s[0:i])
            if s[i:] == '':
                res.append([i for i in sub])
                sub.pop()
                return         
            back_track(s[i:],res,sub)
            sub.pop()
            

def check(s):    
    for i in xrange(0,len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

    
a = Solution()
print a.partition('baaab')

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

print Solution().partition("aab")