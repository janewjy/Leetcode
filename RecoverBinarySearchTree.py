# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        inorder = [float('-inf')]
        notinorder = []
        stack = []
        while  root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val < inorder[-1]:
                notinorder.append(inorder[-1])
            inorder.append(root.val)
            root = root.right

        notinorder[0].val, notinorder[1].val = notinorder[1].val,notinorder[0].val



