class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for i in range(n)] for i in range(n)]
        result = []
        self.queen_back_track(0,n,board,result)
        return result


    def queen_back_track(self, row, n, board, result):
        for col in range(n):
            if self.queen_safe(row,col,board,n):
                board[row][col] = 'Q'
                if row == n-1:
                    printboard = [''.join(x) for x in board]
                    result.append(printboard) 
                    board[row][col] = '.'
                    return
                else:
                    self.queen_back_track(row+1, n, board, result)
                    board[row][col] = '.'

                

    def queen_safe(self, row, col,board,n):
        for i in range(n):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
 
        cleft = col-1
        cright = col+1
        r = row-1
        while r >= 0 :
            if cleft >= 0:
                if board[r][cleft] == "Q":
                    return False
            if cright < n:
                if board[r][cright] == "Q":
                    return False
            cleft -= 1
            cright += 1
            r -= 1

        return True

