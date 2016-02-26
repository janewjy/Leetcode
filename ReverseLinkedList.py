# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        last = None
        while head.next:
            
            later = head.next
            head.next = last
            last = head
            head = later
        head.next = last
        return head 
        


        # Iteration
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
        
    def reverseList2(self, head, last = None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # recursion
        if not head:
            return last
        next = head.next
        head.next = last
        return self.reverseList(next, head)

# 1-21
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        prev = None
        cur = head
        while cur.next:
            nex = cur.next
            cur.next = prev
            prev = cur 
            cur = nex
        cur.next = prev
        return cur
        
            
        
        