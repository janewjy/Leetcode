class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            else:
                if stack == []:
                    return False
                x = stack.pop()
                if (x,c) not in [("(",")"),("[","]"),("{","}")]:
                    return  False
        if stack == []:
            return True
        return False


#better verion from the disscussion forum
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
