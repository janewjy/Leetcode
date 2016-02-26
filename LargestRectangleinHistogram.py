class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        stack = [0]
        r = 0
        for i in range(1, len(height)):
            print [height[l] for l in stack],r
            while stack and height[i] < height[stack[-1]]:
                print [height[l] for l in stack]
                h = height[stack.pop()]
                if not stack:
                    w = i 
                else:
                    w = i - stack[-1] -1
                r = max(r, w*h)
            stack.append(i)
        return r


# # o(n^2) solution,time limit exceed
# class Solution(object):
#     def largestRectangleArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         n = len(height)
#         area = [0]*n
#         for ind in xrange(n):
#             i = ind
#             area[ind] = height[ind]
#             while i<n-1 and height[i]<=height[i+1]:
#                 area[ind] += height[ind]
#                 i += 1 
#             while i > 0 and height[i-1]>=height[i]:
#                 area[ind] += height[ind]
#                 i -= 1
#         return max(area)



a = [2,1,5,6,2,3,1,1,1,1,1,1]
print Solution().largestRectangleArea(a)
# 1-19
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [0]
        res = 0
        for i in xrange(1,len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    v = stack.pop()
                    h = heights[v] 
                    if stack:
                        w = i-stack[-1]-1                        
                    else:
                        w = i
                    res = max(res,w*h)                
                    
                stack.append(i)
        return res

print Solution().largestRectangleArea([2,1,5,6,2,3])
10
print Solution().largestRectangleArea([2,1,2])
print Solution().largestRectangleArea([1,2,3,4,5])
3

