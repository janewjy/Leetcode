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
            return sum(i-j for i, j in zip(prices[1:],prices[:-1]) for i-j > 0)

        