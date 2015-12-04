# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# keep in mind that list operation are in palce
class Solution(object):
    def pathSum(self, root, sumn):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
       
        if not root:
            return []
        result = []
        stack = [(root, [])]
        while stack:
            root, nodes = stack.pop()
            if not root.left and not root.right:
                nodes.append(root.val)
                if sum(nodes) == sumn:
                    result.append(nodes)
            if root.left:
                 stack.append((root.left, nodes+[root.val]))
            if root.right:
                stack.append((root.right,nodes+[root.val]))
                
        return result
                