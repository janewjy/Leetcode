class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)
        i,j = 0,0
        res = []
        while i < n and j < n:
            if s[:j] in wordDict:
                res.append(s[:j])
                i = j
            j += 1 

