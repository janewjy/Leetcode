def reverseBetween(self, head, m, n):
    # if head:
    #     count = 1
    #     curr, p1, p2 = head, head, head
    #     while curr.next and count != n:
    #         p1 = curr
    #         curr = curr.next
    #         count += 1



    #     while curr.next and count != n:
    #         curr = curr.next
    #         count += 1
    #         p2 = curr


    #     curr = p1.next
    #     prev = p2.next
    #     while curr != p2:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp

    #     p1.next = curr

    # return head
class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in xrange(m-1):
            pre = pre.next
        cur = pre.next
        node = None
        for _ in xrange(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        
        pre.next.next = cur
        pre.next = node
        
        return dummy.next

        
        
        
        
