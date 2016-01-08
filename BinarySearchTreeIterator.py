# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.h = []
        self.leftstack(root)
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.h:
            return True
        else:
            return False      
        

    def next(self):
        """
        :rtype: int
        """
        if self.h:
            root = self.h.pop()
            self.leftstack(root.right)
            return root.val

    def leftstack(self,root):
        while root:
            self.h.append(root)
            root = root.left

        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
