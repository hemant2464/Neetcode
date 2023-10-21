class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j):
            # Check if the current cell is out of bounds or not 'O'
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            
            # Mark the current cell as visited by changing 'O' to '#'
            board[i][j] = '#'
            
            # Visit the neighboring cells
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        # Visit the cells on the borders of the board and mark them as unflippable
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)
        
        # Flip the unflippable cells back to 'O' and the flippable cells to 'X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'