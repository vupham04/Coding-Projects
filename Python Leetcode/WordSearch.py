# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, curCol, curRow, word, curPos):
            if 0<=curRow<len(board) and 0<=curCol<len(board[0]) and curPos<len(word):
                if board[curRow][curCol] == word[curPos]:
                    cha = board[curRow][curCol]
                    board[curRow][curCol] = '_'
                    curPos = curPos+1
                    if curPos==len(word):
                        return True
                    if dfs(board,curCol+1,curRow,word,curPos) or dfs(board,curCol,curRow+1,word,curPos) or dfs(board,curCol-1,curRow,word,curPos) or dfs(board,curCol,curRow-1,word,curPos):
                        return True
                    board[curRow][curCol] = cha
            return False
        #return dfs(board, 1, 3, word, 0)
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for ch in range(m):
                if board[i][ch] == word[0]:
                    if dfs(board, ch, i, word, 0):
                        return True
                
        return False
        
        