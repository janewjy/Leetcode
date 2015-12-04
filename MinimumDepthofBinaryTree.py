# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        if not root:
            return level
        q  = [root]
        while q:
            nextl = []
            for node in q:
                if not node.left and not node.right:
                    return level+1
                if node.left:
                    nextl.append(node.left)
                if node.right:
                    nextl.append(node.right)
            level += 1
            q = nextl
        
        return level
                
        
#this is dfs            
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        else:
            # if one of the subtree is None, you should return the depth of another subtree.
            # if all of the subtree is not None, you should return the minimum depth of the two subtrees
            if root.left is None:
                return self.minDepth(root.right) + 1
            elif root.right is None:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
