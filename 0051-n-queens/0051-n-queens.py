from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col):
            return not (cols[col] or diagonals[row - col] or anti_diagonals[row + col])

        def place_queen(row, col):
            queens.append(col)
            cols[col] = True
            diagonals[row - col] = True
            anti_diagonals[row + col] = True

        def remove_queen(row, col):
            queens.pop()
            cols[col] = False
            diagonals[row - col] = False
            anti_diagonals[row + col] = False

        def solve(row):
            if row == n:
                ans.append(["".join("Q" if col == c else "." for c in range(n)) for col in queens])
                return
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    solve(row + 1)
                    remove_queen(row, col)

        cols = [False] * n
        diagonals = [False] * (2 * n - 1)
        anti_diagonals = [False] * (2 * n - 1)
        queens = []
        ans = []
        solve(0)
        return ans