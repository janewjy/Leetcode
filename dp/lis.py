def lis(arr):
    n = len(arr)
    lis = [1]*n
    maxi = 1
    for i in xrange(1,n):
        for j in xrange(i-1,-1,-1):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j] + 1
        maxi = max(maxi,lis[i])
        print lis
    print maxi

arr = [10, 22, 9, 33, 21, 50, 41, 60]
lis(arr)
