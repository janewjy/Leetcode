class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        low,high = 0,0
        i = 0
        while i < len(prices)-1:
            while i < len(prices)-1  and prices[i+1] < prices[i] :
                low = i+1
                i += 1
            while i < len(prices)-1 and prices[i+1]>= prices[i] :
                high = i+1
                i += 1
            if high > low:                
                profit += prices[high] - prices[low]

        return profit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit