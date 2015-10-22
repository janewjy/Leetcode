def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        dummy = cur = ListNode(0)


        while lists:
            cur.next = lists[0].val
            for head in lists:
                if ln.val < tem: cur.next = ln
                ln = ln.next










