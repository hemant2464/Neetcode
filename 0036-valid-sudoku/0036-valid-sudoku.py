class Solution(object):
    def isValidSudoku(self, board):
        seen = set()
        
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    if (element, i) in seen or (element, ~j) in seen or (element, i // 3, j // 3) in seen:
                        return False
                    seen.add((element, i))
                    seen.add((element, ~j))
                    seen.add((element, i // 3, j // 3))
        
        return True