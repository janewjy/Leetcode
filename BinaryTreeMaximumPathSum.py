# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = root.val
        self.oneSum(root)
        return self.res
    
    def oneSum(self, node):
        if not node:
            return 0
        l = max(0, self.oneSum(node.left))
        r = max(0, self.oneSum(node.right))
        self.res = max(self.res, node.val+l+r)
        return node.val + max(l, r)
        
        