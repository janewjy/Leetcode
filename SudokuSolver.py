board = ["..9748...", "7........", ".2.1.9...", "..7...24.",
         ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."]

board2 = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
board = [list(i) for i in board]

keeptrack = 0

["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        back_track(board, 0, 0)



def back_track(board, row, col,flag = 0):
    if col == 9:
        col = 0
        row += 1
    while board[row][col] != '.':
        if col == 8 and row == 8:
            break
        col += 1
        if col == 9:
            col = 0
            row += 1
    if board[row][col] != '.' and row == 8 and col == 8:
        return 1
    for num in range(1, 10):
        if numberSafe(board, num, row, col):
            board[row][col] = str(num)
            if row == 8 and col == 8:
                return 1
            else:
                flag = back_track(board, row, col+1,flag)
                if flag == 1:
                    return 1
                else:
                    board[row][col] = '.'
 


def numberSafe(board,num, row, col):
    num = str(num)
    for i in range(9):
        if num == board[i][col]:
            return False
    for j in range(9):
        if num == board[row][j]:
            return False
    si, sj = row//3, col//3

    for i in range(si*3, si*3+3):
        for j in range(sj*3, sj*3+3):
            if board[i][j] == num:
                return False
    return True

