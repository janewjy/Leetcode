class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right = n, n 
        res = []

        dfs(left,right,res,"")
        return res
        
def dfs(left,right,res,string):
    if left > right:
        return
    if not left and not right:
        res.append(string)
    if left:
        dfs(left-1, right, res, string+"(")
    if right:
        dfs(left,right-1,res,string+")")