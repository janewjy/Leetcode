class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        dic = {beginWord:1}
        front = [beginWord]
        res = []
        ladder(res,subres,dic,front,endWord,wordlist)
        return res
        
        
def ladder(res,subres,dic,beginWord, endWord,wordlist):
    if beginWord in wordlist:
        subres.append(beginWord)
        res.append(subres)
        return 

    for 