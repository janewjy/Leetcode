# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        slow = fast = head
        count = 0
        while fast:
            count += 1
            fast = fast.next
        k = k%count
        fast = slow
        for i in xrange(k):
            fast = fast.next
            if fast == None:
                fast = slow
                break
    
        if fast == slow:
            return head
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        nh = slow.next
        slow.next = None
        fast.next = head
        
        
        return nh
        
        