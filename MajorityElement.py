def majorityElement(self, nums):
    D = {}
    for n in nums:
        if n in D.keys():
            D[n] = D[n]+1
        else:
            D[n] = 1
            
        if D[n]> len(nums)/2.0:
            return n

        
def make_inc(n):
	def func(x):
		return x + n
	return func
# 1-31
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]

# 1-31
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if count == 0:
                count += 1
                maj = i
            else:
                if i == maj:
                    count += 1
                else:
                    count -= 1
        return maj