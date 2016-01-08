class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = []
        low,max_profit = prices[0],0
        for i in prices:
            low = min(low,i)
            max_profit = max(max_profit,i-low)
            profit.append(max_profit)

        high = prices[-1]
        max_profit2 = 0
        total = 0
        for i in range(len(prices)-1,-1,-1):
            high = max(high,prices[i])
            max_profit2 = max(max_profit2,high-prices[i])
            total = max(total,max_profit2+profit[i])
        return total

        # profit = []
        # low,high = 0,0
        # i = 0
        # while i < len(prices)-1:
        #     while i < len(prices)-1  and prices[i+1] < prices[i] :
        #         low = i+1
        #         i += 1
        #     while i < len(prices)-1 and prices[i+1]>= prices[i] :
        #         high = i+1
        #         i += 1
        #     if high > low:                
        #         profit.append(prices[high] - prices[low])

        # profit.sort()
        # print profit
        # return sum(profit[-2:])


# class Solution(object):
#     def maxProfit(self, prices):
#         if not prices:
#             return 0

#         # forward traversal, profits record the max profit 
#         # by the ith day, this is the first transaction
#         profits = []
#         max_profit = 0
#         current_min = prices[0]
#         for price in prices:
#             current_min = min(current_min, price)
#             max_profit = max(max_profit, price - current_min)
#             profits.append(max_profit)
#         print profits
#         # backward traversal, max_profit records the max profit
#         # after the ith day, this is the second transaction 
#         total_max = 0    
#         max_profit = 0
#         current_max = prices[-1]
#         for i in range(len(prices) - 1, -1, -1):
#             current_max = max(current_max, prices[i])
#             max_profit = max(max_profit, current_max - prices[i])
#             print max_profit
#             total_max = max(total_max, max_profit + profits[i])
#         return total_max

test = [1,2,4,2,5,7,2,4,9,0]

a = Solution()
print a.maxProfit(test)


# # class Solution {
# # public:
# #     int maxProfit(vector<int> &prices) {
# #         // f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
# #         // f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
# #         //          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
# #         // f[0, ii] = 0; 0 times transation makes 0 profit
# #         // f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
# #         if (prices.size() <= 1) return 0;
# #         else {
# #             int K = 2; // number of max transation allowed
# #             int maxProf = 0;
# #             vector<vector<int>> f(K+1, vector<int>(prices.size(), 0));
# #             for (int kk = 1; kk <= K; kk++) {
# #                 int tmpMax = f[kk-1][0] - prices[0];
# #                 for (int ii = 1; ii < prices.size(); ii++) {
# #                     f[kk][ii] = max(f[kk][ii-1], prices[ii] + tmpMax);
# #                     tmpMax = max(tmpMax, f[kk-1][ii] - prices[ii]);
# #                     maxProf = max(f[kk][ii], maxProf);
# #                 }
# #             }
# #             return maxProf;
# #         }
# #     }
# # };