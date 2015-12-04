def longestP(s):
    
    res = ''
    for i in range(len(s)):
        # odd case

        temps = helper(s, i, i)
        if len(temps) > len(res):
            res = temps

        # even case
        temps = helper(s, i, i+1)
        if len(temps) > len(res):
            res = temps
    return res


def helper(s, i, j):

    while i >= 0 and j < len(s) and s[i] == s[j] :
            i -= 1
            j += 1

    return s[i+1:j]



if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]

print longestP('wefwetrtbdtsbab')