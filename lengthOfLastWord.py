def lengthOfLastWord(self, s):
    if not s or s.isspace():
        return 0
    else:
        l = 0
        flag = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                flag = 1
                l = l+1
            if flag == 1 and (i == 0 or s[i] ==" "):
                return l

                    
            