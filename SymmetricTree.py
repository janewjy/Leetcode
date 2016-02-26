# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.right, R.left) and isSym(L.left, R.right)
            else:
                return False
        return isSym(root, root)
            
            
# 2-4
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return subtree(root.left,root.right)
        
def subtree(ltree,rtree):
    if not ltree and not rtree:
        return True
    if not ltree or not rtree:
        return False
    if ltree.val != rtree.val:
        return False
    return subtree(ltree.left,rtree.right) and subtree(ltree.right,rtree.left)
    
    
def isSymmetric(self, root):
    if root is None:
        return True
    stack = [(root.left, root.right)]
    while stack:
      left, right = stack.pop()
      if left is None and right is None:
          continue
      if left is None or right is None:
          return False
      if left.val == right.val:
          stack.append((left.left, right.right))
          stack.append((left.right, right.left))
      else:
          return False
    return True