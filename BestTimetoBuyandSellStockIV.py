class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        if k >= n/2:
            return sum(i-j for i, j in zip(prices[1:],prices[:-1]) if i-j > 0)

        dp = [[0]*(n+1) for _ in xrange(k+1)]
        for i in xrange(1,k+1):
            for j in xrange(1,n+1):
                profit = prices[j]-prices[j-1]
                dp[i][j] = max(dp[i][j-1],dp[i-1][j-1]+profit,dp[i-1][j-1],dp[i][j-1]+profit)
        return dp[-1][-1]



def maxProfit4(self, k, prices):
    n = len(prices)
    if n < 2:
        return 0
    # k is big enougth to cover all ramps.
    if k >= n / 2:
        return sum(i - j
                   for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
    globalMax = [[0] * n for _ in xrange(k + 1)]
    for i in xrange(1, k + 1):
        # The max profit with i transations and selling stock on day j.
        localMax = [0] * n
        for j in xrange(1, n):
            profit = prices[j] - prices[j - 1]
            localMax[j] = max(
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day (j - 1)
                # and sell it on day j.
                globalMax[i - 1][j - 1] + profit,
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day j and
                # sell it on the same day, so we have 0 profit, apparently
                # we do not have to add it.
                globalMax[i - 1][j - 1],  # + 0,
                # We have made profit in (j - 1) days.
                # We want to cancel the day (j - 1) sale and sell it on
                # day j.
                localMax[j - 1] + profit)
            globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
    return globalMax[k][-1]