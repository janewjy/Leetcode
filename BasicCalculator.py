# s = "1+2 + 3"
# number = []
# opr = []
# # for n in s.split("+"):
# #     if n.isdigit():
# #         number.append(int(n))
# #     else:
# #         if n != "(":
# #             opr.append(n)

# # print number, opr

# s = "234+(9-2)"
# index = 0
# while index < len(s):
#     count = 0
#     getNum(s.index)
#     if index < len(s):
#         if s[index] in ['+','-']:
#             opr.append(s[index])
    

#     index += 1
# print number, opr

# def getNum(s,index):
#     while index < len(s) and s[index].isdigit():
#         count += 1
#         index += 1
#         print count,index
#     number.append(int(s[index-count:index]))

# #version 1
# class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         numbers = [[]]
#         oprs = [[]]
        

#         i = 0
#         while i < len(s):
#             if s[i] == '(':
#                 numbers.append([])
#                 oprs.append([])
#                 i += 1
#             elif s[i].isdigit():
#                 print s[i]
#                 n,index = get_number(s,i)
#                 numbers[-1].append(n)
#                 i += index
#             elif s[i] in ['+', '-']:
#                 oprs[-1].append(s[i])
#                 i += 1
#             elif s[i] == ' ':
#                 i += 1
#             print numbers, oprs
#             if i == len(s) or s[i] == ')':
#                 a = numbers.pop()
#                 b = oprs.pop()
#                 r = cal(a,b)
#                 if numbers != []:
#                     numbers[-1].append(r)
#                 else:
#                     numbers.append(r)
#                 i += 1
#         print numbers, oprs

#         while oprs != []: 
#             a = numbers.pop()
#             b = oprs.pop()
#             r = cal(a,b)
#             if numbers != []:
#                 numbers[-1].append(r)
#             else:
#                 numbers.append(r)
#         print numbers,  oprs
#         return numbers[0]

# # version 2
# class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         numbers = []
#         oprs = []
#         s = '(' + s + ')'
        

#         i = 0
#         while i < len(s):
#             if s[i] == '(':
#                 numbers.append([])
#                 oprs.append([])
#                 i += 1
#             elif s[i].isdigit():
#                 # print s[i]
#                 n,index = get_number(s,i)
#                 numbers[-1].append(n)
#                 i += index
#             elif s[i] in ['+', '-']:
#                 oprs[-1].append(s[i])
#                 i += 1
#             elif s[i] == ' ':
#                 i += 1
#             # print numbers, oprs
#             if i == len(s) or s[i] == ')':
#                 a = numbers.pop()
#                 b = oprs.pop()
#                 r = cal(a,b)
#                 if numbers != []:
#                     numbers[-1].append(r)
#                 else:
#                     numbers.append(r)
#                 i += 1
#         return numbers[0]

# def cal(numbers, oprs):
#     while len(numbers) > 1:
#         a = numbers.pop(0)
#         b = numbers.pop(0)
#         opr = oprs.pop(0)
#         if opr == '+':
#             numbers.insert(0,a + b)
#         if opr == '-':
#             numbers.insert(0, a-b)
#     return numbers[0]

# def get_number(s,index):
#     number = []
#     while index < len(s):     
#         if s[index].isdigit():
#             number.append(s[index])
#         else:
#             break
#         index += 1
#     return int(''.join(number)), len(number)





# a = Solution()

# print a.calculate("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))")

                


class Solution:
    def calculate(self, s):
        s = '+(+' + s + ')'
        s = s.replace('+-', '-').replace('++', '+') # for the corner case '-5', '+5'
        stack = []
        for i in s:
            if i == ')':
                total = 0
                while stack[-1] != '(':
                    total += int(stack.pop())
                    print stack
                stack.pop()
                sign = 1 if stack.pop() == '+' else -1
                stack.append(sign * total)
            elif i.isdigit() and stack[-1][-1] in '+-0123456789':
                stack[-1] += i
            elif i != ' ':
                stack.append(i)
        return stack[0]

a = Solution()

print a.calculate("(332-6+8+0+2-3)")