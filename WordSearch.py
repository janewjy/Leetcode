def exist(board, word):
    if not board and not word:
        return True
    n = len(word)
    row = len(board)
    col = len(board[0])
    i, j, k = 0, 0, 0
    while k < n:
        for i in range(row):
            for j in range(col):
                while board[i][j] == word[k]:
                     pass :
                    k += 1

