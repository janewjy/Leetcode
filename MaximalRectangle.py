# def maximalRectangle(self, matrix):
#     """
#     :type matrix: List[List[str]]
#     :rtype: int
#     """
#     if matrix==[]: return 0 

#     row=len(matrix); col=len(matrix[0]); area=0
#     height=[0]*col; left=[0]*col; right=[col]*col  #""" set the starting values"""

#     for i in xrange(row):
#         curleft=0; curright=col 

#         #""" each row, set the starting values of the current left and right boundaries """

#         for j in xrange(col): 
#             if matrix[i][j]=="1": 
#                 height[j]+=1; left[j]=max(left[j], curleft)
#             else:
#                 height[j]=0; left[j]=0; curleft=j+1 

#         # """ don't forget to set left[j]=0, otherwise, it will mess up the comparison afterwards """        

#         for j in xrange(col-1,-1,-1): 
#             if matrix[i][j]=='1':
#                 right[j]=min(right[j], curright)
#             else:
#                 right[j]=col; curright=j  
#             area=max(area, height[j]*(right[j]-left[j]))

#        # """ the left boundary starts from the left, and the right boundary starts from the right. """

#     return area

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        dp  = [[0]*n for _ in xrange(m)]
        

        for i in xrange(m):
            for j in xrange(n):
                print matrix[i][j],matrix[i-1][j]
                if matrix[i][j] == 1:
                    dp[i][j] = dp[i-1][j] + 1
            for l in dp:
                print l
            print
        return max(self.largestRectangleArea(row) for row in dp)

    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        stack = [0]
        r = 0
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                if not stack:
                    w = i 
                else:
                    w = i - stack[-1] -1
                r = max(r, w*h)
            stack.append(i)
        return r

Solution().maximalRectangle([[1,1,1,0,0,1],[0,0,0,1,1,1],[0,0,0,1,1,0],[1,0,0,1,1,1],[0,1,0,1,1,1]])


# 1-19
def largestRectangleArea(heights):
    res = 0
    stack = [0]
    heights.append(0)
    for i in xrange(1,len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            if stack:
                w = i - stack[-1] -1
            else:
                w = i
            res = max(res,w*h)
        stack.append(i)
    heights.pop()
    return res

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        acc = [0]*len(matrix[0])
        res = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                
                if matrix[i][j] ==  "1" :
                    acc[j] = acc[j] + 1
                else:
                    acc[j] = 0
            res = max(res, largestRectangleArea(acc))

        return   res

print Solution().maximalRectangle(['1','1'])


    
