# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = helper(root,res)
        res = []
        return res

def helper(root,res):
    if not root:
        return

    helper(root.left,res)
    helper(root.right,res)
    res.append(root.val)
    
    return res

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# two stack solution
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 
        res = []
        stack1 = [root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if stack2[-1].left:
                stack1.append(stack2[-1].left)
            if stack2[-1].right:
                stack1.append(stack2[-1].right)
        while stack2:
            res.append(stack2.pop().val)
        return res

# one stack solution
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right and len(stack)>0 and root.right == stack[-1]:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                res.append(root.val)
                root = None
        return res




def build_tree():
    # Driver program to test above function
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root



if __name__ == '__main__':
    root = build_tree()
    assert Solution().postorderTraversal(root) == [4, 5, 2, 6, 7, 3, 1]



        
  



