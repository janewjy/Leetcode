# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry = carry//10
        return dummy.next
            
       
        
# try to do it inplace

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return []
        carry = 0
        dummy = ListNode(0)
        l = dummy
        while l1 and l2:
            value = (l1.val+l2.val+carry)%10
            a = ListNode(value)
            l.next = a
            l = l.next
            carry = (l1.val+l2.val+carry)//10
            l1 = l1.next
            l2 = l2.next
        while l2:
            value = (l2.val+carry)%10
            a = ListNode(value)
            l.next = a
            l = l.next
            carry = (l2.val+carry)//10
            l2 = l2.next
        while l1:
            value = (l1.val+carry)%10
            a = ListNode(value)
            l.next = a
            l = l.next
            carry = (l1.val+carry)//10
            l1 = l1.next
        
        if carry:
            a = ListNode(carry)
            l.next = a
        return dummy.next
            
            
                
            
            