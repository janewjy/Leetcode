class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = len(coins)
        coins.sort()
        table = [[0] * m for y in xrange(amount+1) ]

        for i in xrange(amount+1):
            for j in xrange(m):
                if i == 0:
                    table[i][j] = 1
                else:
                    x = table[i-coins[j]][j] if i - coins[j] >= 0 else 0
                    y = table[i][j-1] if j >= 1 else 0

                    table[i][j] = (x+y)
        print table
        return table[amount][m-1]


[186,419,83,408], 6249

a = Solution()
print a.coinChange([186,419,83,408], 6249)



# not correct
        # coins.sort()
        # n = 0
        # for i in coins[::-1]:
        #     if amount == 0:
        #         return n
        #     while amount-i >= 0:

        #         amount -= i
        #         n += 1
        # if amount == 0:
        #     return n
        # else:
        #     return -1
