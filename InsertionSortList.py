class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # time limit exceeded for [5000:1] case
        if not head:
            return head
        pos = head
        while pos:
            curr = pos
            cval = curr
            while curr:
                if curr.val < cval.val:
                    cval = curr
                curr = curr.next
            pos.val, cval.val = cval.val, pos.val
            pos = pos.next        
        return head


# why is is faster???
class Solution1(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        fh = ListNode(0)
        fh.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = fh
                while pre.next.val < cur.next.val:
                    pre = pre.next
                t = cur.next
                cur.next = t.next
                t.next = pre.next
                pre.next = t
            else:
                cur = cur.next
        return fh.next

[2,1]
[1,1]


if __name__ == '__main__':

    import time
    bgn_time = time.time()

    range(5000)[::-1]
    Solution().insertionSortList()


    print time.time() - bgn_time

