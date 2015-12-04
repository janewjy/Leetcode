class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                del dic[num]
        return dic.keys()[0]


#   one line python
return reduce(lambda x, y: x ^ y, nums)

# Bit manipulation
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for num in nums[1:]:
            result = result ^ num
        return result
        