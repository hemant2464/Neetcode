class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def can_reach(t):
            if grid[0][0] > t:
                return False

            visited = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] <= t:
                        if nx == ny == n - 1:
                            return True
                        stack.append((nx, ny))
                        visited.add((nx, ny))

            return False

        left, right = 0, n * n - 1
        while left < right:
            mid = (left + right) // 2
            if can_reach(mid):
                right = mid
            else:
                left = mid + 1

        return left