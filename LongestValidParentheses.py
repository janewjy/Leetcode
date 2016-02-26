class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = len(s)
        stack = [-1]
        res = 0
        for i in xrange(l):
            if s[i] == "(":
                stack.append(i)
            else: 
                stack.pop()
                if len(stack)!=0:
                    res = max(res,i-stack[len(stack)-1])
                else:
                    stack.append(i)
        return res

print Solution().longestValidParentheses("))((((()))))))))")
            
