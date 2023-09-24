class Solution(object):
    def isValidSudoku(self, board):
        seen = set()

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    # Check for duplicates in the same row, column, or subgrid
                    if (element, i) in seen or (j, element) in seen or (i // 3, j // 3, element) in seen:
                        return False
                    seen.add((element, i))
                    seen.add((j, element))
                    seen.add((i // 3, j // 3, element))

        return True