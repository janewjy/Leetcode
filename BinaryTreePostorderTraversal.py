# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        res = helper(root,res)
        return res

def helper(root,res):
    if not root:
        return

    helper(root.left,res)
    helper(root.right,res)
    res.append(root.val)
    
    return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        last = None
        while  root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            if root.right != None and last != root.right:
                root = stack[-1].right
            else:
                res.append(root.val)
                last = stack.pop()

        return res
                

