class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res = []
        wb('',res,wordDict,s)
        return res       


def wb(sub,res,wordDict,s):
    if s in wordDict:
        res.append(sub+s)

        return 

    dp = [False]*(len(s)+1)
    dp[0] = True

    for i in xrange(1,len(s)+1):
        if dp[i-1] == True:
            for w in wordDict:
                if s.find(w,i-1) == i-1:
                    sub = sub + w+' '
                    wb(sub,res,wordDict,s[i-1+len(w):])
                    sub = ''
a="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
b= ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
print Solution().wordBreak(s,dic)


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.dict = dict
        self.cache = {}
        return self.break_helper(s)

    def break_helper(self, s):
        combs = []
        if s in self.cache:
            return self.cache[s]
        if len(s) == 0:
            return []

        for i in range(len(s)):
            if s[:i+1] in self.dict:
                if i == len(s) - 1:
                    combs.append(s[:i+1])
                else:
                    sub_combs = self.break_helper(s[i+1:])
                    for sub_comb in sub_combs:
                        combs.append(s[:i+1] + ' ' + sub_comb)

        self.cache[s] = combs
        return combs


