class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = 0
        i = 1
        while True:
            if isUgly(i):
                n-=1
            if n==0:
                return i
            else:
                i+=1
        
def isUgly(num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            while num%2  == 0:
                num = num/2
            while num%3 == 0:
                num = num/3
            while num%5 ==0:
                num = num/5
            
            if num == 1 :
                return True
            else:
                return False

def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
        print ugly,i2,i3,i5
    return ugly[-1]

print nthUglyNumber(10)

