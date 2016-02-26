class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = {}
        return dp(s1,s2,m)


def dp(s1,s2,m):
    if (s1,s2) in m:
        return m[(s1,s2)]

    if not sorted(s1) == sorted(s2):
        m[(s1,s2)] = False
        return False
    if len(s1)<4 and sorted(s1) == sorted(s2):
        m[(s1,s2)] = True
        return True

    for i in xrange(1,len(s1)):
        if (dp(s1[:i],s2[-i:],m) and dp(s1[i:],s2[:-i],m)) or \
        (dp(s1[:i],s2[:i],m) and dp(s1[i:],s2[i:],m)):
            m[(s1,s2)] = True
            return True
    m[(s1, s2)] = False    
    return False