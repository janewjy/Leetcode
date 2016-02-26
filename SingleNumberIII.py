class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = b = 0
        for i in nums:
            xor ^= i
        mask = 1
        while xor&mask == 0:
            mask = mask << 1
        for i in nums:
            if i&mask:
                a ^= i
            else:
                b ^= i
        return [a,b]
