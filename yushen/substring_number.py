def substring(s,t):
    table = {}
    for i in t:
        table[i] = 1
    missing = len(t)
    i =0
    res = 0
    for j,c in enumerate(s,0):
        
        if missing != 1 and c in t and table[c] == 1:
            missing -= 1
            table[c] -= 1
        elif missing == 1 and c in t and table[c] == 1:
            res += (j-i+1)*(j-i)/2
            
            missing -=1 
            table[c] -= 1
        while missing == 0 and i<j: 
            if s[i] not in table:
                i += 1
                continue
            else:
                table[s[i]] += 1
                missing += 1
                i += 1 

    res += (j-i+2)*(j-i+1)/2
    return res
'sabcdelrab','ae'
print substring('sabcdelrab','ae')








