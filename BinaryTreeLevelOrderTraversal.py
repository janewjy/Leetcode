# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
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
                    print f.left.val,nextlval
                if f.right != None:
                    nextlval.append(f.right.val)
                    nextlnode.append(f.right)
            front = nextlnode            
            if nextlval != []:
                level.append(nextlval)
            
            
        return level


#faster


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        r = []
        if not root:
            return r
        q.append((root,0))
        while q:
            node,level = q.pop(0)
            if len(r) == level:
                r.append([node.val])
            else:
                r[level].append(node.val)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        return r