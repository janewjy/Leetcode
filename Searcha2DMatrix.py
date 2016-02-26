class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        i,j = 0, m-1
        mid = (i+j)//2
        while  i <= j:
            mid = (i+j)//2
            if target == matrix[mid][0]:
                return True
            if target > matrix[mid][0]:
                i = mid + 1 
            else:
                j = mid-1
        row = min(i,j)
        
        n = len(matrix[row])

        i,j = 0, n-1
        while  i <= j:
            mid = (i+j)//2
            if target == matrix[row][mid]:
                return True
            if target > matrix[row][mid]:
                i = mid + 1
            else:
                j = mid-1

        return False

# ??? don't treat it like as a 2D array, treat it as a sorted list.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        
        i,j = 0,m*n-1
        while i <= j:
            mid = (i+j)/2
            if matrix[mid/n][mid%n] < target:
                i = mid+1
            elif matrix[mid/n][mid%n] > target:
                j = mid-1
            else:
                return True
        return False
        


            

matrix = [  [1,   3,  5,  7],  [10, 11, 16, 20],  [23, 30, 34, 50]]
target = 11
# matrix = [[1],[3]]
# target = 3

print Solution().searchMatrix(matrix,target)