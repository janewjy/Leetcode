# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# dfs + recursion

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        self.dfs(root,'',result)
        return result
        
    def dfs(self,root,ls,result):
        if not root.left and not root.right:
            result.append(ls+str(root.val))  
        if root.left != None:
            self.dfs(root.left, ls+str(root.val)+'->',result)
        if root.right != None:
            self.dfs(root.right, ls+str(root.val)+'->',result)

# dfs + stack

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        stack = [(root,"")]

        while stack:
            root, ls = stack.pop()
            if not root.left and not root.right:
                result.append(ls+str(root.val))
            if root.left:
                stack.append((root.left,ls+str(root.val)+'->'))
            if root.right:
                stack.append((root.right,ls+str(root.val)+'->'))
        return result


# bfs + queue
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        stack = [(root,"")]

        while stack:
            root, ls = stack.pop(0)
            if not root.left and not root.right:
                result.append(ls+str(root.val))
            if root.left:
                stack.append((root.left,ls+str(root.val)+'->'))
            if root.right:
                stack.append((root.right,ls+str(root.val)+'->'))
        return result
