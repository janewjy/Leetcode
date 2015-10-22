# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.right, R.left) and isSym(L.left, R.right)
            else:
                return False
        return isSym(root, root)
            
            
        