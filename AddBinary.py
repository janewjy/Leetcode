def addBinary(a, b):
        a = int(a)
        b = int(b)
        print a, b
        return ("" + bin(a+b))[2:]
print addBinary("1111",'10101')

# 1-29
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        n = len(b)
        i,j = m-1,n-1
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            if i >=0:
                carry += int(a[i])
                i -= 1
            if j >=0:
                carry += int(b[j])
                j -=1
            res = [str(carry%2)] + res
            carry = carry//2
        if carry != 0:
            res = [str(carry)]+res
        a = ''.join(res)
        return a

print Solution().addBinary('1111','10101')