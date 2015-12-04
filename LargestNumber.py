class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        strings = [str(c) for c in nums]
        strings.sort(cmp = lambda x, y: cmp(y+x, x+y))  # [121,12]
        return ''.join(strings).lstrip('0') or '0'      # [0,0]