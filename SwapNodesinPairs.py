# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        l,r = dummy, head.next
        while head and r:
            l.next, head.next, r.next = r, r.next, head 
            l = head
            head = head.next
            if head:
                r = head.next
            else:
                break
        return dummy.next
        
# online solution
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        p1 = guard = ListNode(0)
        guard.next = head

        try:
            while True:
                p0, p1, p2 = p1, p1.next, p1.next.next
                p0.next, p1.next, p2.next = p2, p2.next, p1
        except:
            return guard.next        