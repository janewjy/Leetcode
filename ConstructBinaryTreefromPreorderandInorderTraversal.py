# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return

        root = TreeNode(preorder.pop(0))
        index = inorder(root.val)

        root.left = self.buildTree(preorder,inorder[:index])
        root.right = self.buildTree(preorder,inorder[index+1:])

        return root


p = [10,30,40,50,60,70,90]
i = [50,30,10,40,70,60,90]

