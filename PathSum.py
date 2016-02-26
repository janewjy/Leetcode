# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root,0)]
        while stack:
            root, total = stack.pop()
            if not root.left and not root.right:
                total += root.val
                if total == sum:
                    return True
            if root.left:
                stack.append((root.left, total+root.val))
            if root.right:
                stack.append((root.right, total+root.val))
        return False

# 2-4
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
            
        l,r = False, False
        if root.left:
            l =  self.hasPathSum(root.left,sum-root.val)
        if root.right:
            r =  self.hasPathSum(root.right,sum-root.val)
        return l or r