class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        get_bin = lambda x, n: format(x, 'b').zfill(n)
        s = get_bin(0,26)
        print s
        s = s[::-1]
        return int(s,2)
        
print Solution().reverseBits(3)



class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)