class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # l = len(s)
        # n = 0
        # for letter in s:
        # 	n = n + (ord(letter)-64)*26**(l-1)
        # 	l=l-1
        # return n

        # version 1
        res = 0
        for i in s:
            res = res*26 + ord(i)-ord("A") + 1
        return res

        # version 2
        return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))
