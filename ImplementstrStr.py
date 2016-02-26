class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        m = len(haystack)
        n = len(needle)
        for i in xrange(len(haystack)-len(needle)+1):
            if haystack[i:i+n] == needle:
                return i
        return -1