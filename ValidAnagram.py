def isAnagram(self, s, t):
    letters = [0]*26
    for l in s:
        n = ord(l)
        letters[n-97] = letters[n-97]+1
    for l in t:
        n = ord(l)
        letters[n-97] = letters[n-97]-1
        if letters[n-97] < 0:
            return False
    if sum(letters) == 0:
        return True
    else:
        return False


# one line solution
sorted(s) == sorted(t)
