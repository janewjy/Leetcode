def ed(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[None]*(n+1) for _ in xrange(m+1)]

    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            for q in dp:
                print q
            print

    return dp[m][n]


def ed2(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[None]*(n+1) for _ in xrange(m+1)]

    for i in xrange(m, -1, -1):
        for j in xrange(n, -1, -1):

            if i == m:
                dp[i][j] = n-j
            elif j == n:
                dp[i][j] = m-i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1+min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
            for q in dp:
                print q
            print

    return dp[0][0]

# Driver program
str1 = "day"
str2 = "saturday"

print ed2(str1, str2)
# This code is contributed by Bhavya Jain


# Driver program
str1 = "day"
str2 = "sundaysun"

print ed(str1, str2)
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[1, 0, 1, 2, 3, 4, 5, 6, 7]
[2, 1, 1, 2, 2, 3, 4, 5, 6]
[3, 2, 2, 2, 3, 3, 4, 5, 6]
[4, 3, 3, 3, 3, 4, 3, 4, 5]
[5, 4, 3, 4, 4, 4, 4, 3, 4]
[6, 5, 4, 4, 5, 5, 5, 4, 3]

[3, 4, 3, 3, 3, 4, 4, 5, 6]
[4, 3, 3, 2, 2, 3, 3, 4, 5]
[5, 4, 3, 2, 1, 2, 2, 3, 4]
[6, 5, 4, 3, 2, 1, 1, 2, 3]
[6, 5, 4, 3, 2, 1, 0, 1, 2]
[7, 6, 5, 4, 3, 2, 1, 0, 1]
[8, 7, 6, 5, 4, 3, 2, 1, 0]


# print ed2(str1, str2)
# This code is contributed by Bhavya Jain
