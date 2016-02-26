def rightSideView(self, root):
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        front = [root]
        res = [root.val]
        while front:
            level = []
            for node in front:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                res.append(level[-1].val)
            front = level
        return res
        
                    
                    
                    
                    
                
        