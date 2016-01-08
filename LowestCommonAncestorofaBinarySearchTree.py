# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ap = []
        aq = []
        stack = []
        while  root or stack:
            while root:
                stack.append(root)
                if root == p:
                    ap = [ _ for _ in stack]
                if root == q:
                    aq = [_ for _ in stack]
                root = root.left

            root = stack.pop()
            root = root.right
        for i, j in zip(ap.revers(),aq.revers()):
            if i == j:
                return i


                pass
            pass

    s