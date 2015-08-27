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
        l = len(s)
        n = 0
        for letter in s:
        	n += ord(letter)-ord('A')+1)*26**(l-1)
        	l -= 1
        return n

aaa = map(lambda x: x ** 2, range(10))
