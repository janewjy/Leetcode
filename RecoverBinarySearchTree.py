# import sys

#  o(n) stack solution
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
    

#     def recoverTree(self, root):
#         self.first = None
#         self.second = None
#         self.prev = TreeNode(-sys.maxint-1)
#         self.inorder(root)
#         print self.first.val, self.second.val
#         self.first.val, self.second.val = self.second.val, self.first.val
        
#     def inorder(self, root):
#         if not root:
#             return 
#         self.inorder(root.left)
#         print root.val
#         if self.first == None and self.prev.val > root.val:
#             self.first, self.second = self.prev, root
#             print self.first.val, 'f'
#         if self.first != None and self.prev.val > root.val:
#             self.second = root
#             print self.first.val, self.second.val,'s'
#         self.prev = root
#         self.inorder(root.right)

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
        if not root:
            return
        cur = root
        former1 = None
        former2 = None
        former = None
        while cur!=None:
            if cur.left == None:
                former = cur
                cur = cur.right
            else:
                prev = cur.left
                while prev.right!= None  and prev.right!=cur:
                    prev = prev.right
                if prev.right == None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    former = cur
                    cur = cur.right
            if former and cur:
                if former1 == None and former.val > cur.val :
                    former1 = former
                if former1!=None and former.val > cur.val:
                    former2 = cur
                    
        former1.val, former2.val = former2.val, former1.val
# 1-20 space o(n) solution
#??? pass paramters into nested function
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        first, second, prev = None,None,None
        
        def inorder(root):
            if root:
                inorder(root.left)
                if prev == None:
                    prev = root
                else:
                    if root.val < prev.val and first == None:
                        first = prev
                    if first != None and root.val < prev.val:
                        second = root
                    prev = root
                inorder(root.right)
        inorder(root)
        first.val, second.val = second.val, first.val
                    
                    
                
            
        