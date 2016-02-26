# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         m = len(s1)
#         n = len(s2)
#         l = len(s3)
#         # if l != m+n:
#         #     return False
#         if m == 0:
#             return s2 == s3
#         if n == 0:
#             return s1 == s3
#         if l == 0:
#             return m == 0 and n == 0

#         if s3[0] not in [s1[0],s2[0]]:
#             return False

#         elif s1[0] != s2[0]:
#             if s3[0] == s1[0]:
#                 return self.isInterleave(s1[1:],s2,s3[1:])
#             if s3[0] == s2[0]:
#                 return self.isInterleave(s1,s2[1:],s3[1:])
#         else:
#             return self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:])
            

a = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
b = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
c = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
# print Solution().isInterleave(a,b,c)


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        l = len(s3)
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        
        for i in xrange(0,m+1):
            dp[i][0]  = (s1[:i] == s3[:i])
        for j in xrange(0,n+1):
            dp[0][j] = (s2[:j] == s3[:j])
        
        for i in xrange(1,m+1):
            count = i            
            for j in xrange(1,n+1):
                dp[i][j] = (dp[i-1][j] and (s3[count] == s1[i-1])) or (dp[i][j-1] and (s3[count] == s2[j-1]))       
                count += 1
                
        return dp[m][n]


print Solution().isInterleave(a,b,c)
# ??? try to use o(n) space

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2) != len(s3):
            return False
        # if not s1 or not s2:
        #     return s3 == s1 if s1 else s2
        m = len(s1)
        n = len(s2)
        dp = [[False]*(n+1) for _ in xrange(m+1)]
        
        for i in xrange(m+1):
            for j in xrange(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and dp[i][j-1] and s2[j-1]==s3[j-1]:
                    dp[i][j] = True
                elif j == 0 and dp[i-1][j] and s1[i-1] == s3[i-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
                
                    
                
        