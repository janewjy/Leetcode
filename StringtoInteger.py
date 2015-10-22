class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        l = len(str)
        num = []
        i = 0
        if str:
            if str[0] in ["-","+"]:
                if l > 1 and str[1].isdigit():
                    num.append(str[0])
                    i = 1
                else:
                    return 0
            
            if str[i].isdigit():
                while i < l:
                    if str[i].isdigit():
                        num.append(str[i])
                        i += 1
                    else:
                        break
        if num:    
            a  = int(''.join(num))
            if a > 2**31 - 1:
                return 2**31 - 1
            elif a < -2**31:
                return -2**31
            else:
                return a
        else:
            return 0

# Solution online
class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)  #???

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0
                
            

        

print not "b".isdigit()
print myAtoi("00000345")
print myAtoi("345")
print myAtoi("------345")
print myAtoi("345q34")
print myAtoi("       345  ")
print myAtoi("aef")
print myAtoi("00000sdf")
print myAtoi("-0000345")
print myAtoi("-00001")
print myAtoi("-")
print myAtoi("+0")
print myAtoi("b11228552307")
print myAtoi("2147483648")

print myAtoi("123")