class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        answer = False
        visited = [[0]*len(board[0]) for i in xrange(len(board))]
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):

                if board[row][col] == word[0]:
                    if len(word) == 1:
                        return True
                    visited[row][col] = 1
                    answer = helper(board,visited,row,col,word[1:])
                    print answer

                if answer == True:
                    return True
                visited[row][col] = 0
        return False

def helper(board,visited,row,col,word):
    for i,j in canVisit(row,col,visited):
        if board[i][j] == word[0] :
            visited[i][j] = 1
            if len(word) == 1:
                return True
            else:
                answer = helper(board,visited,i,j,word[1:])
                if answer == True:
                    return True
                else:
                    visited[i][j] = 0
def canVisit(row,col,visited):
    res = []
    if row>0 and visited[row-1][col] == 0:
        res.append((row-1,col))
    if col>0 and visited[row][col-1] == 0:
        res.append((row,col-1))
    if row<len(visited)-1 and visited[row+1][col] == 0:
        res.append((row+1,col))
    if col<len(visited[0])-1 and visited[row][col+1] == 0:
        res.append((row,col+1))
    return res

    
["CAA","AAA","BCD"]
"AAB"

t = ["ABCE","SFCS","ADEE"]
s = "ABCCED"
t = ["CAA","AAA","BCD"]
s = "AAB"

a = Solution()
print a.exist(t,s)



        