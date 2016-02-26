# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = 0
        self.k = k
        self.ks(root,self.k)
        return self.res

    def ks(self,root,k):
        if root:
            self.ks( root.left,self.k)
            self.k-=1
            if self.k==0:
                self.res = root.val
                return 
            self.ks(root.right,self.k)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        p = root
        stack = []
        
        while p:
            stack.append(p)
            p = p.left
        while k!= 0 :
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            right = node.right
            while right:
                stack.append(right)
                right = right.left
                
                
            
            
            