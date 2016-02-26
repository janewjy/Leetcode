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

# this is a naive solution take o(n) time.
# count the n/2 number
# 1-23
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        mid = (m+n)/2
        
        if not nums1:
            return nums2[mid] if (m+n)%2 != 0 else float(nums2[mid]+nums2[mid-1])/2
    
        count  = 0
        i, j = 0, 0
        m1 = None
        m2 = None
        while count <= mid:
            count += 1
            if i == m:
                m1 = m2
                m2 = nums2[j]
                j += 1
                continue
            elif j == n:
                m1=m2
                m2 = nums1[i]
                i += 1
                continue
            
            if nums1[i]<nums2[j]:
                m1 = m2
                m2 = nums1[i]
                i += 1
            else:
                m1 = m2
                m2 = nums2[j]
                j += 1
            
            
        if not m1 or (m+n)%2 != 0:
            return m2
        else:
            return (m1+m2)/float(2)

# ??? need to do later
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
    
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)



               

