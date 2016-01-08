class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1) + len(num2))
        pos = len(product)-1
    
        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos-1] += product[tempPos]/10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1
    
        pt = 0
        while pt < len(product)-1 and product[pt] == 0:
            pt += 1
    
        return ''.join(map(str, product[pt:]))

# ??? not correct find a better way
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num2) > len(num1):
            num1,num2 = num2,num1
        dig = 1
        an = ['0']

        for i in num2[::-1]:
            print i
            sub = list(str(int(num1)*int(i)*dig))
            carry = 0
            if len(sub) > len(an):
                an, sub = sub, an
            i = len(sub) - 1
            j = len(an) - 1
            print an,sub
            while i >= 0 :
                tmp = int(sub[i])+int(an[j])+carry
                print tmp
                if tmp > 9:
                    an[j] = str(tmp)[-1]
                    carry = int(str(tmp)[0])
                else:
                    an[j] = str(tmp)
                j -= 1
                i -= 1
            if carry != 0 and j!=-1:
                an[j] = str(int(an[j])+carry)
            elif carry != 0:
                an.insert(0,str(carry))
            print an
            dig *=10

        return ''.join(an)

a = Solution()
print a.multiply('234','234')
                



