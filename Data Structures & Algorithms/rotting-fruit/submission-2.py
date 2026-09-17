from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten = deque()
        seen = set()
        clean = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    rotten.append((r, c))
                if val == 1:
                    clean += 1
        newrotten = deque()
        minutes = 0
        while rotten:
            curr = rotten.popleft()
            if curr in seen:
                continue
            (cury, curx) = curr
            dirs = ((1, 0), (0, 1),(-1, 0), (0, -1))
            for (dy, dx) in dirs:
                newx, newy = curx + dx, cury + dy
                if not ((0 <= newx < n) and (0 <= newy < m)):
                    # invalid cords
                    continue
                if (newy, newx) in seen:
                    # already seen banana
                    continue
                if grid[newy][newx] == 1:
                    grid[newy][newx] = 2
                    newrotten.append((newy, newx))
                    clean -= 1
            seen.add(curr)
            if len(rotten) == 0:
                # swap rotten and newrotten
                # increase minutes
                rotten = newrotten
                newrotten = deque()
                if rotten:
                    minutes += 1
        
        return minutes  if clean == 0  else -1


        
        

        