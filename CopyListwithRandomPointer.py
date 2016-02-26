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
        if not head:
            return None   
        cur = head
        mapping = {}
        while cur:
            if cur not in mapping:
                node = RandomListNode(cur.label)
                mapping[cur] = node
            if cur.next:
                if cur.next not in mapping:
                    node = RandomListNode(cur.next.label)
                    mapping[cur.next] = node
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                if cur.random not in mapping:
                    node = RandomListNode(cur.random.label)
                    mapping[cur.random] = node
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]





        