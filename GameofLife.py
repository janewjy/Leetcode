class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        board2 = [[0]*n for _ in xrange(m)]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j]:
                    if live_cell(i,j,m,n,board)<2:
                        board2[i][j] = 0
                    elif 2<=live_cell(i,j,m,n,board)<=3:
                        board2[i][j] = 1

                    elif live_cell(i,j,m,n,board)>3:
                        board2[i][j] = 0

                elif board[i][j] == 0 and live_cell(i,j,m,n,board)==3:
                    board2[i][j] = 1
        board[::] = board2[::]

def live_cell(i,j,m,n,board): 
    res = 0
    count = 0
    if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]    
    if i-1 >= 0:                count += board[i-1][j]  
    if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]    
    if j-1 >= 0:                count += board[i][j-1]  
    if j+1 < n:                 count += board[i][j+1]  
    if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]    
    if i+1 < m:                 count += board[i+1][j]  
    if i+1 < m and j+1 < n:     count += board[i+1][j+1]    
    return count    

[[1,0,1],[1,1,1],[0,0,1]]