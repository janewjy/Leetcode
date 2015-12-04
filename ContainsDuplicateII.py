class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)

        dic = {}
        for i in range(0,n):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        print dic
        for key in dic.keys():
            last = len(dic[key]) - 1
            if last == 0:
                continue
            i = 0
            while i < last:
                if dic[key][i+1] - dic[key][i] <= k:
                    return True
                i += 1

        return False


dic = {}
for i,num in enumerate(nums):
    if i not in dic:
        

# better version
def containsNearbyDuplicate(self, nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False

[1,0,1,1]
1

[1,2,3,1,1,2,3]
0