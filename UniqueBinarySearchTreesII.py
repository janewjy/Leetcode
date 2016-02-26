# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1,n+1)
         
    def dfs(self, start,end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start,i) or [None]:
                for r in self.dfs(i+1,end) or [None]:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    result.append(node)
        return result

# not working mine version
# class Solution(object):
#     def generateTrees(self, n):
#         """
#         :type n: int
#         :rtype: List[TreeNode]
#         """
#         if n == 0:
#             return []
#         subtree = {0:[None], 1:[TreeNode(1)]}
#         for i in xrange(2,n+1):
#             num = []
            
#             for j in range(i):
#                 for p in subtree[j]:
#                     newN = TreeNode(i)
#                     newN.left = p
#                     for q in subtree[i-1-j]:
#                         newN.right = q
#                         num.append(newN)
#             subtree[i] = num
#         return subtree[n]




#             [[2,1],[2,null,1]]
#             [[1,null,2],[2,1]]

