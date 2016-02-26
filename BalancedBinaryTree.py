# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # from the web
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def height(self, root):
        if not root: 
            return 0
        return 1+max(self.height(root.left), self.height(root.right))
    
    # can you use classified discussion do it as well???s

# [1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5] is a Balanced tree
# 