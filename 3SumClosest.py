class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        k = 0
        diff = float('inf')
        while k < len(nums)-2:
            j = len(nums) - 1
            i = k + 1
            while i < j:
                if abs(nums[i] + nums[j] + nums[k] - target) < diff:
                    diff = abs(nums[i] + nums[j] + nums[k] - target)
                    res = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                elif nums[i] + nums[j] + nums[k] > target:
                    j -= 1
                else:
                    i += 1
            k += 1
        return res


a = Solution()
print a.threeSumClosest([0, 1, 2], 3)

# 1-20 tle
import sys


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i, j = 0, len(nums)-1
        res = sys.maxint
        sum = 0
        for i in xrange(n-2):
            for j in xrange(i+1, n-1):
                for k in xrange(j+1, n):
                    if abs(target-nums[i]-nums[j]-nums[k]) < res:
                        sum = nums[i]+nums[j]+nums[k]

        return sum


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i, j = 0, n-1
        res = 0
        diff = sys.maxint
        while i < j-1:
            third = target-nums[i]-nums[j]
            p, q = i, j
            while p < q:
                mid = (p+q)
                if nums[mid] = third:
                    return target
                elif nums[mid] < third:
                    p = mid+1
                else:
                    q = mid-1

            diff = min(diff, abs(target-nums[i]-nums[j]-nums[p]))

            if nums[i]+nums[j] < target:
                i += 1
            else:
                j -= 1

        return target - diff
[-3,-2,-5,3,-4]
-1

[1,2,4,8,16,32,64,128]
82

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1]+ nums[2]
        n = len(nums)
        for i in xrange(n-2):
            j = i+1
            k = n-1
            while j < k:
                sumation = nums[i]+nums[j]+nums[k]
                if abs(target - res) > abs(target - sumation):
                    res = sumation
                if sumation > target:
                    k -= 1
                elif sumation == target:
                    return sumation
                else:
                    j += 1
        return res

