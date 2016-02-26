# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,  q.right)
        return p == q



    # tuple solution, why???
    def isSameTree(self, p, q):
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)

# bfs 1-20
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        front1 = [p]
        front2 = [q]
        while front1 or front2:
            next1 = []
            next2 = []
            for i,j in zip(front1,front2):
                if i and j and i.val != j.val:
                    return False
                if i.left and j.left and i.left.val == j.left.val:
                    next1.append(i.left)
                    next2.append(j.left)
                elif j.left != None or i.left != None:
                    return False
                    
                if i.right and j.right and i.right.val == j.right.val:
                    next1.append(i.right)
                    next2.append(j.right)
                elif i.right != None or j.right != None:
                    return False
            front1 = next1
            front2 = next2
        return True
                
