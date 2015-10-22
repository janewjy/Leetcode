# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            temp = cur
            while temp.next and temp.next.val == temp.val:
                temp = temp.next
            cur.next = temp.next
            cur = cur.next
        return head
            