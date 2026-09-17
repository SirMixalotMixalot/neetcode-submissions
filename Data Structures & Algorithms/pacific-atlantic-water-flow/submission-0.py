class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])

        def dfs(r, c, reachable):
            if (r, c) in reachable:
                return # already seen
            
            reachable.add((r,c))
            h = heights[r][c]
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newr, newc = r + dr, c + dc
                if not ((0 <= newr < m) and (0 <= newc < n)):
                    continue
                if heights[newr][newc] >= h:
                    dfs(newr, newc, reachable)
        
        for row in range(m):
            dfs(row, 0, pacific)
            dfs(row, n - 1, atlantic)
        for col in range(n):
            dfs(0, col, pacific)
            dfs(m - 1, col, atlantic)
        
        res = pacific & atlantic
        return [[r,c] for (r,c) in res]

            

        