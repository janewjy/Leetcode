def mcp(cost, a, b):
    m = len(cost)
    n = len(cost[0])
    dp = [[0]*(n) for _ in xrange(m)]
    dp[0][0] = cost[0][0]
    for i in xrange(1,m):
        for j in xrange(1,n):
            if j == 1:
                dp[i][0] = dp[i-1][0] + cost[i][0]
            if i == 1:
                dp[0][j] = dp[0][j-1] + cost[0][j]
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + cost[i][j]
        print dp
    print dp[m-1][n-1]

# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(mcp(cost, 2, 2))

# This code is contributed by Bhavya Jain
