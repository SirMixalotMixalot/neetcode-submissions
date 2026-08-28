class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # keep track of sum and current array of numbers
        # possibilities: add num to target
        # skip num

        # [2, ], []
        # # [2, 2,] [2,]
        #   
        # [2,2,2], [2,2]
        # [2,2,2,2], [2,2,2]
        # [2,2,2,2,2] x [2,2,2,2]

        answer = []
        total = 0

        def dfs(curr, total, i):
            nonlocal answer
            # basecase
            if total > target:
                return
            if total == target:
                answer.append(curr)
                return

            if i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(curr[:], total + nums[i], i)
            curr.pop()
            dfs(curr[:], total, i + 1)
        dfs([], 0, 0)
        return answer
        