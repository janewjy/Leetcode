class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list2Node(alist):
    node = ListNode(0)
    head = node
    for i in alist:
        node.val = i
        node.next = ListNode(0)
        node = node.next
    return head


alist = [1,1,3,3,4,4,5,6,6]

def deleteDuplicates(head):

    dummy = pre = ListNode(0)
    dummy.next = head
    while head and head.next:
        print dummy.next.val, pre.next.val,head.val

        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next

    return dummy.next


print deleteDuplicates(list2Node(alist)).val




