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