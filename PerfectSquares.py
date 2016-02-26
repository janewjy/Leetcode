# tle
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = int(math.sqrt(n))
        r = [i*i for i in xrange(1,r+1)]
        dp = [n]*(n+1)
        dp[0] = 0
        for i in xrange(1,n+1):
            for j in r:
                if i-j>=0:
                    dp[i] = min(dp[i],dp[i-j]+1)

        return dp[-1]

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        visited = [False]*(n+1)
        level = 1
        front = [0]
        while True:
            nextl = []
            for v in front:
                i = 1
                while i*i <=n:
                    if v+i*i == n:
                        return level
                    elif v+i*i>n:
                        break
                    else:
                        if not visited[v+i*i]:
                            visited[v+i*i] = True
                            nextl.append(v+i*i)
                    i += 1
            front = nextl
            level+=1
        return 
                    
            
        
        
        
        
       
            