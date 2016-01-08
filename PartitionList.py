# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        d1 = ListNode(0)
        d2 = ListNode(0)
        head1 = d1
        head2 = d2
        cur = head


        while cur:
            if cur.val < x:
                d1.next = cur
                d1 = d1.next
            else:
                d2.next = cur
                d2 = d2.next
            print cur.val
            p  = cur.next
            cur.next = None
            cur = p
        d1.next = head2.next
        return head1.next

public ListNode partition(ListNode head, int x) {
    ListNode dummy=new ListNode(0);
    dummy.next=head;
    ListNode p=dummy;
    ListNode tail=dummy;
    while(p!=null && p.next!=null){
        if(p.next.val>=x)
            p=p.next;
        else{
            if(p==tail){  // don't forget the edge cases when p==tail
                tail=tail.next;
                p=p.next;
            }
            else{
                ListNode tmp=p.next;
                p.next=tmp.next;
                tmp.next=tail.next;
                tail.next=tmp;
                tail=tmp; // don't forget to move tail.
            }
        }
    }
    return dummy.next;
}