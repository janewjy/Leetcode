class Solution(object):
    # too slow
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l < 3:
            return []
        triple = []
        nums.sort()
        for i in range(l):
            for j in range(i+1, l):
                v = 0 - nums[i] - nums[j]
                if v in nums[j+1:] and [nums[i], nums[j], v] not in triple:
                    triple.append([nums[i], nums[j], v])
                
        return triple
            
    #faster solutions online
    
    def threeSum(self, nums):
    count={} # number: count
    for i in nums:
        count[i] = count.get(i,0) + 1

    ans = []
    nsort = sorted(count.keys())

    for i in xrange(len(nsort)):
        n1 = nsort[i]
        count[n1] -= 1
        for j in xrange(i,len(nsort)):
            n2 = nsort[j]
            if count[n2] >= 1:
                count[n2] -= 1
                n3 = - (n1 + n2)
                if n3>=n2 and n3 in count and count[n3]>=1:
                    ans.append([n1, n2, n3])
                count[n2]+=1
        count[n1]+=1
    return ans

    def threeSum(self, nums):
        if len(nums) <3: # deal with special input
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]


        nums = sorted(nums) # sorted, O(nlgn)
        ans = []

        for i in range(len(nums) -2):
            j = i+1
            k = len(nums) -1 # hence i < j < k

            while j<k: # if not cross line
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    ans.append((nums[i], nums[j], nums[k]))

                if temp_sum > 0: # which means we need smaller sum, move k backward, remember we sort the array
                    k -= 1
                else:
                    j += 1

        return list(set(tuple(ans))) # I bet this is not the best way to eliminate duplicate solutions
        
        
        
#1-19 eliminate the duplicat nums make code much faster
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        if n < 3 or nums[0] > 0 or nums[-1] < 0:
            return []
        res = []
        for i in xrange(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in xrange(i+1,n-1):
                target = 0 - nums[i] - nums[j]
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if target < nums[j]:
                    break
                
                if target in nums[j+1:]:
                    res.append([nums[i],nums[j],target])
        return res
                    
                    
                
                
            

        
        