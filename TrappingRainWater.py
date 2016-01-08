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
                 
