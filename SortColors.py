class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # counting sort
        k = [0,0,0]
        for i in nums:
            k[i] += 1
        # my version
        nums[:] = [0 for x in range(0,k[0])] + [1 for x in range(0,k[1])] + [2 for x in range(0, k[2])]
        # nums[:k[0]] = [0] * k[0]
        # nums[k[0]:k[0]+k[1]] = [1] * k[1]
        # nums[k[0]+k[1]:] = [2] * k[2]


        # one pass
        lo = 0
        hi = len(nums) - 1
        curr = 0

        while curr <= hi:
            if nums[curr] == 0:
                nums[lo] = 0
                curr += 1
                lo += 1
            elif nums[curr] == 2:
                nums[hi], nums[curr] = nums[curr], nums[hi]
                hi -= 1
            else:
                curr += 1
            if curr > hi:
                break
            print nums, lo, hi, curr
        nums[lo:hi+1] = [1] * (hi+1 - lo)

        # better version

        l, r, zero = 0, len(nums)-1, 0
        while l <= r:
            if nums[l] == 0:
                nums[l], nums[zero] = nums[zero], nums[l]
                l += 1; zero += 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count1 = count0= 0
        for i in nums:
            if i == 1:
                count1 += 1
            elif i == 0:
                count0 += 1
        nums[:count0] = [0]*count0
        nums[count0:count0+count1] = [1]*count1
        nums[count0+count1:] = [2]*(len(nums)-count1-count0)
        