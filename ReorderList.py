# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        helper = head
        slow = helper
        fast = slow
        
        if head and head.next:
            while fast and fast.next:
                p = slow
                slow = slow.next
                fast = fast.next.next
            last = None
            p.next = None
            while slow.next:
                later = slow.next
                slow.next = last
                last = slow
                slow = later
            slow.next = last
            while helper.next:
                forw = helper.next
                backw = slow.next
    
                helper.next = slow
                slow.next = forw
    
                helper = forw
                slow = backw
            helper.next = slow
            
