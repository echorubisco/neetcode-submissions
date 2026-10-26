class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, column = len(board)-1, len(board[0])-1
        def backtrack(r,c,i):
            if i == len(word):
                return True
            if r<0 or r>row or c<0 or c>column or board[r][c] != word[i] or board[r][c] == '#':
                return
            char = board[r][c]
            board[r][c] = '#'
            found = backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1)
            board[r][c] = char
            return found
        for i in range(row+1):
            for j in range(column+1):
                if backtrack(i,j,0):
                    return True
        return False
        