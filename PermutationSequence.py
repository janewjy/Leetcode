from math import factorial


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in xrange(1, n+1)]
        while n-1 >= 0:
            num, k = k/factorial(n-1), k % factorial(n-1)
            if k > 0:
                res.append(str(nums[num]))
                nums.remove(nums[num])
            else:
                res.append(str(nums[num-1]))
                nums.remove(nums[num-1])

            n -= 1

        return ''.join(res)
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in xrange(1,n+1)]
        print nums
        k %= math.factorial(n)
        res = ""
        while n-1>=0:
            if k%math.factorial(n-1) != 0:
                d = k//math.factorial(n-1)
            else:
                d = k//math.factorial(n-1)-1
            res += nums[d]
            nums.remove(nums[d])
            k %= math.factorial(n-1)
            n -= 1
        return res
            
            
import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation