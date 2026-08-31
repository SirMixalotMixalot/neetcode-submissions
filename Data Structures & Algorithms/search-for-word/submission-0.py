class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def neighbours(r,c):
            return [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            ]
 
        def explore(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            for nr, nc in neighbours(r, c):
                if explore(nr, nc, i + 1):
                    return True
            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if explore(r, c, 0):
                    return True
        return False