# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        helper(root, res)
        return res


def helper(root, res):
    if root:
        helper(root.left,res)
        res.append(root.val)
        helper(root.right.res)

# iterative soltion

class Solution(object):
    # recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while  root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res

# 1-20 morries solution O(1) space

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                
                if prev.right == None:
                    prev.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    prev.right = None
                    root = root.right
        return res
                    


class Solution(object):
    # recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while  root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


def build_tree():
    """ Constructed binary tree is
                1
              /   \
             2     3
           /  \
          4    5   """
     
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


if __name__ == '__main__':
    root = build_tree()
    print Solution().inorderTraversal(root)
    # assert Solution().inorderTraversal(root) == [4, 2, 5, 1, 3]
    assert Solution().inorderTraversal(None) == []