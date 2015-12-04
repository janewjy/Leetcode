board = ["..9748...", "7........", ".2.1.9...", "..7...24.",
         ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."]
board = [list(i) for i in board]

keeptrack = 0


# # def avilableNumber(board,p,q):
#     numberList = [str(x) for x in range(1,10)]
#     for i in xrange(9):
#         if board[i][q] in numberList:
#             numberList.remove(board[i][q])
#     for j in xrange(9):
#         if board[p][j] in numberList:
#             numberList.remove(board[p][j])
#     si, sj = p//3, q//3

#     for i in range(si*3, si*3+3):
#         for j in range(sj*3, sj*3+3):
#             if board[i][j] in numberList:
#                 numberList.remove(board[i][j])
#     return numberList

def numberSafe(num, row, col):
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




def back_Track(row, col):
    if col == 9:
        col = 0
        row += 1
    while board[row][col] != '.':
        if col == 8 and row == 8:
            print board
            break
        col += 1
        if col == 9:
            col = 0
            row += 1


    print board
    for num in range(1, 10):
        if numberSafe(num, row, col):
            board[row][col] = str(num)
            if row == 8 and col == 8:
                print board
            else:
                print row,col
                back_Track(row, col+1)


back_Track(0, 0)
