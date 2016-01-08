# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        while head:
            if head not in dic:
                dic[head] = 1
            else:
                return True
            head = head.next

        return False

    # constant space solution
    # why is the faster one will finally meet the slower one???

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while  slow is not fast:
                slow = slow.next
                fast = fast.next.next

            return True
        except:
            return False


