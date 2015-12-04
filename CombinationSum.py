class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        n = len(candidates)
        
        result = []

        back(candidates,target)


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        n = len(candidates)

        back(candidates,target,result,n)


def back(candidates, target,result,n):
    for i in xrange(n):
        
        print target, result, candidates[i]
        if candidates[i] <= target:
            target = target - candidates[i]
            print target
            if target == 0:
                result.append(candidates[i])
                print result
                
            elif target < candidates[i]: 
                return
            else:
                result.append(candidates[i])
                back(candidates, target, result,n)
    
        
            