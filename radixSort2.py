def radixSort(alist):
    
    for k in xrange(0,10):
        s = [[] for x in xrange(10)]
        print s
        for i in alist:
            s[(i/10**k)%10].append(i)
        print s
        alist = [b for a in s for b in a]
        print alist 

    return alist


print radixSort([1,34,345,1231,3453,12])