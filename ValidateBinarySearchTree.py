class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = []
        stack = []
        while  root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        print inorder
        for i in xrange(len(inorder)-1):
            if inorder[i+1] <= inorder[i]:
                return False
    
        return True
