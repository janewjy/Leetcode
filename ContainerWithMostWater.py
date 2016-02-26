class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        water = 0
        while i<j:
            water = max(water,(j-i) * min(height[i],height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j += 1

        return water
# 1-19-2016
class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, res = 0, len(height)-1, 0

        while i < j:
            area = (j-i) * min(height[i],height[j])
            res = max(res,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res

print Solution().maxArea([1,1,3,4,5,6])
