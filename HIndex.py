class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        n = len(citations)
        h = 0
        i = 0
        while i < n:
            if citations[i] >= n-i:
                h = max(n-i, h)
            i += 1
        return h

[0]
[1]
[3, 0, 6, 1, 5]
[1,0]

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        n = len(citations)
        h = 0
        i = 0
        while i < n:
            if citations[i] >= n-i:
                return n-i
            i += 1
        return h