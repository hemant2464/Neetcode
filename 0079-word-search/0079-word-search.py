from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited or board[i][j] != word[idx]:
                return False

            visited.add((i, j))

            # Explore neighbors
            if (
                backtrack(i + 1, j, idx + 1) or
                backtrack(i - 1, j, idx + 1) or
                backtrack(i, j + 1, idx + 1) or
                backtrack(i, j - 1, idx + 1)
            ):
                return True

            visited.remove((i, j))  # Backtrack
            return False

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        # Start exploration from each cell in the board
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True

        return False