class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        low = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            low = min(prices[i],low)
            profit = max(profit, prices[i]-low)
        return profit
            
        