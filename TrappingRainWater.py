a = [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        i, j = 0, len(height) - 1 
        left = 0
        right = 0
        water = 0
        while i != j:
            left, right = max(left,height[i]), max(right,height[j])
            if height[i] < height[j]:
                water += left-height[i]
                i += 1
            else:
                water += right - height[j]
                j -= 1
        return water
                 
#1-19-2016

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        stack = [0]
        area = 0

        for i in xrange(1,len(height)):
            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:                 
                while stack and height[stack[-1]]<height[i]:
                    v = stack.pop()
                    base = height[v]
                    if stack:
                        w = i - stack[-1] -1
                        area += (min(height[stack[-1]],height[i]) - base)*w
                stack.append(i)
        return area



print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])


