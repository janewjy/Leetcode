[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for s in board:
            if findDuplicants(s):
                return False
        
        for i in xrange(9):
            unit = [s[i] for s in board]
            if findDuplicants(''.join(unit)):
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                unit = [s[i:i+3] for s in board[j:j+3]]
                if findDuplicants(''.join(''.join(l) for l in unit)):
                    return False
        return True


def findDuplicants(s):
    dic = {}
    for i in s:
        if i == '.':
            continue
        if i in dic:
            return True
        dic[i] = 1
    
    return False

# 1-25
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)
        for i in board:
            save = []
            for j in i:
                if board[i][j]!='.':
                    if board[i][j] not in save:
                        save.append(board[i][j])
                    else:
                        return False
        for j in xrange(m):
            save = []
            for i in xrange(m):
                if board[i][j]!='.':
                    if board[i][j] not in save:
                        save.append(board[i][j])
                    else:
                        return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                save = []
                unit = [s[i:i+3] for s in board[j:j+3]]
                for k in unit:
                    if k!='.':
                        if board[i][j] not in save:
                            save.append(board[i][j])
                        else:
                            return False
        return True

