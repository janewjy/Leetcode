# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return

        while root.left:
            p = root
            while p:
                p.left.next = p.right
                if p.next:
                    p.right.next = p.next.left
                p = p.next
            root = root.left
        
        