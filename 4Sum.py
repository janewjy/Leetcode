def four_sum(nums,target):
    # 776 ms
    n = len(nums)
    nums.sort()
    if n >= 4 and  (sum(nums[0:4]) > target or sum(nums[-4:]) < target):
        return []
    result = []
    for i in range(0,n-3):
        for j in range(i+1,n-2):
            k = j+1
            l = n-1
            while k < n and l >j+1 and k != l:
                value = nums[i] + nums[j] + nums[k] + nums[l]
                if value == target:
                    if [nums[i],nums[j],nums[k],nums[l]] not in result:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1                                      
                if value > target:
                    l -= 1
                elif value < target:
                    k += 1     
    return result
                    

test4 = [-1,0,1,2,-1,-4]
-1
test = [0,10,-10,0,4,-4,-5,3,2]



test2 = [0,0,0,0]
0
test3 = [2,1,0,-1]
2

test5 = [-3,-2,-1,0,0,1,2,3]
0
test6 = [1,-2,-5,-4,-3,3,3,5] 
-11




[-499,-486,-479,-462,-456,-430,-415,-413,-399,-381,-353,-349,-342,-337,-336,-331,-330,-322,-315,-280,-271,-265,-249,-231,-226,-219,-216,-208,-206,-204,-188,-159,-144,-139,-123,-115,-99,-89,-80,-74,-61,-22,-22,-8,-5,4,43,65,82,86,95,101,103,123,149,152,162,165,168,183,204,209,209,220,235,243,243,244,248,253,260,273,281,284,288,290,346,378,382,384,407,411,423,432,433,445,470,476,497]
3032

nums = [-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481]
-5617
nums2 = [-494,-474,-425,-424,-391,-371,-365,-351,-345,-304,-292,-289,-283,-256,-236,-236,-236,-226,-225,-223,-217,-185,-174,-163,-157,-148,-145,-130,-103,-84,-71,-67,-55,-16,-13,-11,1,19,28,28,43,48,49,53,78,79,91,99,115,122,132,154,176,180,185,185,206,207,272,274,316,321,327,327,346,380,386,391,400,404,424,432,440,463,465,466,475,486,492]
-1211
print four_sum(test6, -11)

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        result = []
        for i in xrange(len(num)-3):
            if num[i] > target/4.0:
                break
            if i > 0 and num[i] == num[i-1]:
                continue
            target2 = target - num[i]
            for j in xrange(i+1, len(num)-2):
                if num[j] > target2/3.0:
                    break
                if j > i+1 and num[j] == num[j-1]:
                    continue
                k = j + 1
                l = len(num) - 1
                target3 = target2 - num[j]
                # we should use continue not break
                # because target3 changes as j changes
                if num[k] > target3/2.0:
                    continue
                if num[l] < target3/2.0:
                    continue
                while k < l:
                    sum_value = num[k] + num[l]
                    if sum_value == target3:
                        result.append([num[i], num[j], num[k], num[l]])
                        kk = num[k]
                        k += 1
                        while k<l and num[k] == kk:
                            k += 1

                        ll = num[l]
                        l -= 1
                        while k<l and num[l] == ll:
                            l -= 1
                    elif sum_value < target3:
                        k += 1
                    else:
                        l -= 1
        return result
# 1-20
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        n = len(nums)
        nums.sort()

        for i in xrange(n-3):
            if nums[i] > target/4.0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target2 = target - nums[i]
            for j in xrange(i+1,n-2):
                if nums[j] > target2/3.0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                target3 = target2-nums[j]
                k,l = j+1,n-1
                while k < l:
                    if nums[k] > target3/2.0:
                        break
                    if nums[l] < target3/2.0:
                        break
                    
                    sumation = nums[i]+nums[j]+nums[k]+nums[l]
                    if sumation == target and [nums[i],nums[j],nums[k], nums[l]] not in res :
                        res.append([nums[i],nums[j],nums[k], nums[l]])
                    if sumation > target:
                        l -= 1
                    else:
                        k += 1
        return res