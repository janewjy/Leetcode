# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root,res = [],fres = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res =  0
        stack = [(root, root.val)]

        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += val
                if node.left:
                    stack.append((node.left, val*10+node.left.val))
                if node.right: 
                    stack.append((node.right, val*10+node.right.val))
        return res
# recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root,res = [],fres = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = dfs(root,root.val,0)

        return res


def dfs(root,val,res):
    if root:
        if root.left:
            res = dfs(root.left,val*10+root.left.val,res)
        if root.right:
            res = dfs(root.right,val*10+root.right.val,res)
        if not root.right and not root.left:
            return res + val
            
    return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        front = [root]
        total = 0
        while front:
            level = []
            for node in front:
                if node.left:
                    node.left.val = node.val*10 + node.left.val
                    level.append(node.left)
                if node.right:
                    node.right.val = node.val*10+ node.right.val
                    level.append(node.right)

                if not node.left and not node.right:
                    total += node.val
            front = level
        return total



        