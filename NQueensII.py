class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [['.']*n for _ in xrange(n)]
        res = [0] 
        bk(board,0,res)
        return res[0]

def bk(board,i,res):
    for j in xrange(len(board)):
        if safe(board,i,j):
            board[i][j] = 'Q'
            if i == len(board)-1:
                res[0] += 1
                board[i][j] = '.'
                return
            else:
                bk(board,i+1,res)
                board[i][j] = '.'




def safe(board,row,col):
    for i in xrange(len(board)):
        if board[i][col] == 'Q' or  board[row][i] == 'Q':
            return False
    r = row-1
    cleft = col-1
    cright = col+1
    while r>=0:
        if cleft >= 0 and board[r][cleft] == 'Q':
            return False
        if cright < len(board) and board[r][cright] == "Q":
            return False
        r -= 1
        cleft -=1
        cright += 1
    return True



print Solution().totalNQueens(4)       

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [['.']*n for _ in xrange(n)]
        res = bk(board,0,0)
        return res

def bk(board,i,res):
    for j in xrange(len(board)):
        if safe(board,i,j):
            board[i][j] = 'Q'
            if i == len(board)-1:
                board[i][j] = '.'
                return res+1
            else:
                res = bk(board,i+1,res)
                board[i][j] = '.'
    return res


def safe(board,row,col):
    for i in xrange(len(board)):
        if board[i][col] == 'Q' or  board[row][i] == 'Q':
            return False
    r = row-1
    cleft = col-1
    cright = col+1
    while r>=0:
        if cleft >= 0 and board[r][cleft] == 'Q':
            return False
        if cright < len(board) and board[r][cright] == "Q":
            return False
        r -= 1
        cleft -=1
        cright += 1
    return True
 