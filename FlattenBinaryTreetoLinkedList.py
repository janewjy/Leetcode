# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        head = root
        stack = []
        while  head or stack:
            if not head:
                head = stack.pop()
                tmp.right = head
            if head.right:
                stack.append(head.right)
            if head.left:
                head.right = head.left
                head.left = None
            else:
                head.right = None
            tmp = head
            head = head.right

        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        self.flatten(root.left)
        self.flatten(root.right)

        temp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = temp
