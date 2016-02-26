class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow = nums[0]
        fast = nums[nums[0]]
        
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        # how to decide the starting point and restart point???
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# if can change the array
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[abs(nums[i])]>0:
                nums[abs(nums[i])] = -nums[abs(nums[i])]
            else:
                return abs(nums[i])




