class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def dfs(curr, total, i):

            if total == target:
                answer.append(curr[:])
                return
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(curr, total + candidates[i], i + 1)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(curr, total, i + 1)
        dfs([], 0, 0)
        return answer