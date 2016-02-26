class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in xrange(1,len(s)+1):
            if dp[i-1] == True:
                for w in wordDict:
                    if s.find(w,i-1) == i-1:
                        dp[i-1+len(w)] = True
        print dp
        return dp[-1]


class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        is_breakable = [False] * (n+1)
        is_breakable[0] = True
        for i in xrange(1,n+1):
            for j in xrange(0,i):
                if is_breakable[j] and s[j:i] in wordDict:
                    is_breakable[i] = True
                    break
        return is_breakable[n]
            
            