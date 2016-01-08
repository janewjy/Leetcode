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
        queue = []
        front = [root]

        while front:
            for i in xrange(len(front)):
                if front[i].left:
                    queue.append(front[i].left)
                if front[i].right:
                    queue.append(front[i].right)
                if i < len(front) -1:
                    front[i].next = front[i+1]
            front = queue
            queue = []


        