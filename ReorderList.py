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
        if not head or not head.next or not head.next.next:
            return 
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        prev = None
        print second.val
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        print second,prev.val

        while head.next and prev:
            head_next = head.next
            prev_next = prev.next
            head.next = prev
            prev.next = head_next
            head = head_next
            prev = prev_next
            
                    



[1,2,3,4,5,6]