class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list2Node(alist):
    if alist:
        node = ListNode(0)
        head = node
        for i in range(0,len(alist)):
            node.val = alist[i]
            if i != len(alist)-1:
                node.next = ListNode(alist[i])
                node = node.next
        return head
    else:
        return None

def printNodes(head):
    node = head
    while node:
        print node.val
        node = node.next

h1 = [2]
h2 = [1,5,10]

l1 = list2Node(h1)
l2 = list2Node(h2)



# def mergeTwoLists(l1, l2):
    
   
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     if not l1: return l2
#     if not l2: return l1
    
#     newList = ListNode(0)
#     head = newList
    
#     while l1 and l2:
#         print "while"
        
#         if l1.val < l2.val:
#             newList.val = ListNode(l1.val)
#             newList.val = l1.val
#         else:
#             newList.val = l2.val
        
#         if l1.next:
#             l1 = l1.next
#         if l2.next:
#             l2 = l2.next

    
#     while l1.next != None:
#         newList.val = l1.val
#         newList = l1.next
#         l1 = l1.next
        
#     while l2.next != None:
#         newList.val = l2.val
#         newList = l2.next
#         l2 = l2.next
    
    
#     return head

def mergeTwoLists( l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
        print "cur"
        printNodes(cur)
    return dummy.next


head = mergeTwoLists(l1,l2)
print "results"
printNodes(head) 
    
    
print [] and 0
            
        
    
# 1-20
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
            elif l2:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
            cur = cur.next

        return dummy.next
                

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        cur.next = l1 if l1 else l2

        return dummy.next
                
                