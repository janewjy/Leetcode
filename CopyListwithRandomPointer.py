# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        rhead = dummy
        table = {}
        ohead = head
        while  head != None:
            Node = RandomListNode(head.label)
            table[head] = Node

            rhead.next = Node
            rhead = rhead.next
            head = head.next
        rhead = dummy.next
        while ohead != None:
            if ohead.random != None:
                rhead.random = table[ohead.random]
            rhead = rhead.next
            ohead = ohead.next            

        return dummy.next