# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        while head:
            if head not in dic:
                dic[head] = 1
            else:
                return head
            head = head.next

        return None

# constant space
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head
            fast = head.next
            while  slow is not fast:
                slow = slow.next
                fast = fast.next.next
            
        except:
            return None
            
        slow = head
        while  slow is not fast.next:
            slow = slow.next
            fast = fast.next
        return slow

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        fast = head
        slow = head
        isloop = False
        
        while fast and slow:
            if not fast.next:
                return None
            else:
                fast = fast.next.next
                slow = slow.next
            if slow is fast:
                isloop = True
                break
        if isloop == False:
            return None
        slow = head
        while slow is not fast:
            
            slow = slow.next
            fast = fast.next
        return slow
            