def radixSort(alist):
    for k in xrange(10):
        s = [[] for i in xrange(10)]
        print s
        for i in alist:
            s[i/(10**k)%10].append(i)
        print "after", s
            
        alist = [a for b in s for a in b]
        print alist
    return alist


print radixSort([23,33125,2,1,4,0,12])