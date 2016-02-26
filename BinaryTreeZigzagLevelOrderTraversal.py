# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 44ms
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = [[root.val]]
        nodes = [root]
        order = -1
        while  nodes:
            nextlval = []
            nextlnode = []
            
            for n in nodes:
                if n.left != None:
                    nextlval.append(n.left.val)
                    nextlnode.append(n.left)
                if n.right != None:
                    nextlval.append(n.right.val)
                    nextlnode.append(n.right)
            if nextlval != []:
                res.append(nextlval[::order])
                order *= -1
            nodes = nextlnode

        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        front = [root]
        order = -1
        res = [[root.val]]
        while front:
            level = []
            value = []
            for i in front:
                if i.left:
                    level.append(i.left)
                    value.append(i.left.val)
                    
                if i.right:
                    level.append(i.right)
                    value.append(i.right.val)
            if level:
                if order<0:
                    res.append(value[::-1])
                else:
                    res.append(value)
            order = -order
            front = level
        return res
            
            
        