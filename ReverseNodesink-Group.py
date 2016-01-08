# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        q = dummy
        if not head or k == 0 or k == 1:
            return head
        while True:
            f = q.next
            i = 0
            while i < k:
                i += 1
                tail = tail.next
                if not tail :
                    return dummy.next
            latter = last = tail.next
            while head != latter:
                p = head.next
                head.next = last
                last = head
                head = p
            q.next = tail
            q = tail = f

        return dummy.next