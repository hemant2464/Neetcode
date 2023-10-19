from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        def dfs(r, c, ocean, visited):
            if (r, c) in ocean or (r, c) in visited:
                return
            ocean.add((r, c))
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean, visited)
        
        n, m = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for i in range(n):
            dfs(i, 0, pacific, set())
            dfs(i, m - 1, atlantic, set())
        for j in range(m):
            dfs(0, j, pacific, set())
            dfs(n - 1, j, atlantic, set())
        
        return list(pacific.intersection(atlantic))