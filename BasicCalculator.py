s = "1+2 + 3"
number = []
opr = []
# for n in s.split("+"):
#     if n.isdigit():
#         number.append(int(n))
#     else:
#         if n != "(":
#             opr.append(n)

# print number, opr

s = "234+(9-2)"
index = 0
while index < len(s):
    count = 0
    getNum(s.index)
    if index < len(s):
        if s[index] in ['+','-']:
            opr.append(s[index])
    

    index += 1
print number, opr

def getNum(s,index):
    while index < len(s) and s[index].isdigit():
        count += 1
        index += 1
        print count,index
    number.append(int(s[index-count:index]))