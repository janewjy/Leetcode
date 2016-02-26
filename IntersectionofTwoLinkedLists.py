class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
            

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         if not headA or not headB:
#             return 
        
#         a, b  = headA, headB
#         while a.next or b.next :
#             if a.next:
#                 a = a.next
#             if b.next:
#                 b = b.next
#         if a == b:
#             a.next = headB
#             slow  = headA
#             fast = headA
#             while slow!=fast:
#                 slow = slow.next
#                 fast = fast.next.next
#             slow = headA
#             while slow != fast:
#                 slow = slow.next
#                 fast = fast.next
#             a.next = None
#             return slow
#         else:
#             return

