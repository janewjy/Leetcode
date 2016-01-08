class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        alist = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                alist.append(nums1[i])
                i += 1
            else:
                alist.append(nums2[j])
                j += 1

        if i == m:
            alist.extend(nums2[j:])
        if j == n:
            alist.extend(nums1[i:])

        if (m + n)%2 == 1:
            return alist[(m + n)/2]
        if (m + n)%2 == 0:
            return (alist[(m + n)/2] + alist[(m + n)/2-1])/float(2)
        
        
#another online solution ???

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0


def findKth(A,B):
    
    if len(A)>len(B):
            A,B=B,A
    if not A:
        return B[len(B)/2]
    i = len(A)/2
    j = len(B)/2

    if A[i] < B[j]:
        return findKth(A[i:],B[:j+1])
    else:
        return findKth(A[:i+1],B[j:])



    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            #Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)