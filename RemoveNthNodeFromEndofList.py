# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = dummy = ListNode(0)
        dummy.next = head
        
        count = 0
        while count < n:
            p2 = p2.next
            count += 1
            
    
        while p2:
            head = p1
            p1 = p1.next
            p2 = p2.next
            
    
        head.next = p1.next
    
        return dummy.next


#Online solution
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# 1-20
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        i = 0
        while i < n:
            i += 1
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        after = slow.next.next
        de = slow.next
        de.next = None
        slow.next = after
        return dummy.next
        
        
            
        