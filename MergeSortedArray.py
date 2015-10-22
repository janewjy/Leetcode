class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        for j in range(n):
            while i < m+j and nums1[i] < nums2[j]:
                i += 1
            nums1.insert(i,nums2[j])
            i += 1
            
        nums1[m+j+1:] = nums2[j+1:]
        # inster() slow the code down
        
    def merge2(self, nums1, m, nums2, n):
        l1, l2, end = m-1, n-1, m+n-1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] > nums2[l2]:
                nums1[end] = nums1[l1]
                l1 -= 1
            else:
                nums1[end] = nums2[l2]
                l2 -= 1
            end -= 1

        if l1 < 0:
            nums1[:l2+1] = nums2[:l2+1]


            
            