# n = 30
# t,l = n
# s = ""

# while t > 0:
# 	i = 0
# 	while t > 26:
# 	    t = t/26
# 	    i += 1

# 	s =  s+chr((t-1)+ord("A"))
# 	t = n - 26**i
# 	print s,l


# n = 26
# s = ""
# while n > 0:
# 	if n % 26 != 0:
# 		r = n%26
# 		n = (n-r)/26
# 		s = s+chr(r-1+ord("A"))
		
# 	else:
# 		n = n/26
# 		s = s+chr(25+ord("A"))
		
# print s  


num = 677
ans = ''
while num:
    ans = chr(ord('A') + (num - 1) % 26) + ans
    num = (num -1) / 26

print ans



class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            
            l = (n-1)%26
            
            res = chr(l+ord('A')) + res
            n = (n-l)/26
        return res
