class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        if n%2:
            quarter_size = n//2 +1
        else:
            quarter_size = n//2
        
        print matrix
        for i in range(n//2):
            for j in range(quarter_size):
                print i, j
                print matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i]
                print matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]
                print id(matrix), id(matrix[0]), id(matrix[1])
                matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = \
                matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]
                print id(matrix), id(matrix[0]), id(matrix[1])
                print matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i]
                print matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]

    def rotate2(self, matrix):
        matrix[:] = map(lambda x: list(x[::-1]), zip(*matrix))[:]

def test():
    matrix = [[1,2],[3,4]]
    matrix1 = [[1,2,3,4,21,22],[5,6,7,8,23,24],[9,10,11,12,25,26],[13,14,15,16,27,28],[13,9,5,1,21,22],[13,9,5,1,21,22]]
    matrix2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]


    num = 2

    matrices = [
    {'input': [], 'output':[]},
    {'input': [[1]], 'output':[[1]]},
    {'input': [[1,2],[3,4]], 'output':[[3,1],[4,2]]},
    {'input': [range(num) for i in range(num)], 'output': [[i] * num for i in range(num)]},
    {'input': map(lambda x: list(tuple(x)), [range(num)] * num), 'output': [[i] * num for i in range(num)]},
    {'input': [[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]], 
     'output': [[21,16,11,6,1],
                [22,17,12,7,2],
                [23,18,13,8,3],
                [24,19,14,9,4],
                [25,20,15,10,5]]},

    ]

    rotate_image = Solution().rotate

    for mat_pair in matrices:
        print mat_pair
        rotate_image(mat_pair['input'])
        print mat_pair
        assert mat_pair['input'] == mat_pair['output']

    # rotateImage(matrix2)
    # print matrix2



if __name__ == '__main__':
    test()
    matrix2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

    Solution().rotate(matrix2)
    print matrix2




