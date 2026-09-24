class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer = []

        def dfs(curr, i):
            if i >= len(nums):
                answer.append(curr[:])
                return
            dfs(curr + [nums[i]], i + 1)
            dfs(curr, i + 1)
        dfs([], 0)        
        return answer