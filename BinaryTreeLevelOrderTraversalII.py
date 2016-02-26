# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        level = [[root.val]]
        front = [root]
        
        while front:
            nextlval = []
            nextlnode = []
            for f in front:
                if f.left != None:
                    nextlval.append(f.left.val)
                    nextlnode.append(f.left)
                if f.right != None:
                    nextlval.append(f.right.val)
                    nextlnode.append(f.right)
                    
            front = nextlnode
            if nextlval != []:
                level.insert(0, nextlval)
                
        return level

# 2-4
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        front = [root]
        res = []
        while front:
            level = []
            subres = []
            for node in front:
                subres.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.insert(0,subres)
            front = level
        return res
        