# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        #  notice the inital position of slow and fast so when process a short linked list, 
        # cut in the right position
        slow = head
        fast = head.next.next
        while fast and  fast.next:
            slow = slow.next 
            fast = fast.next.next
        second = slow.next
        slow.next = None
        root = TreeNode(second.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(second.next)

        return root
