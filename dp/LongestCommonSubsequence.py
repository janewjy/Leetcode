def lcsq(arr1,arr2,m,n):
    print arr1[:m], arr2[:n]
    if m == 0 or n == 0:
        return 0
    elif arr1[m-1] == arr2[n-1]:
        return 1 + lcsq(arr1,arr2,m-1,n-1)
    else:
        return max(lcsq(arr1,arr2,m-1,n),lcsq(arr1,arr2,m,n-1))


def printMatrix(testMatrix):
    for i in xrange(len(testMatrix)):
        print testMatrix[i]
    print
def lcs(arr1,arr2):
    m = len(arr1)
    n = len(arr2)

    table = [[None] * (n+1) for _ in xrange(m+1)]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif arr1[i-1] == arr2[j-1]:
                table[i][j] = table[i-1][j-1] + 1 
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
            print i,j, table[i][j]
        printMatrix(table)
    return table[m][n]

X = "AXY"
Y = "AYZ"
print "Length of LCS is ", lcs(X, Y)
