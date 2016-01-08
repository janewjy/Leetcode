# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    res = []
    helper.(root, res)
    return res


def helper(root, res):
    if root:
        helper(root.left,res)
        res.append(root.val)
        helper(root.right.res)

# iterative soltion

class Solution(object):
    # recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    res = []
    stack = []
    while  root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right

    return res


