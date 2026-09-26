class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(r, c):
            if grid[r][c] == "0":
                return
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            grid[r][c] = "0"
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if not (0 <= newR < len(grid) and 0 <= newC < len(grid[0])):
                    continue # invalid cords
                dfs(newR, newC)
            # grid[r][c] = "1"
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1
        print(grid)
                
        return ans

        