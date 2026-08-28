class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # permutation
        # [_,_,_,_, ...]
        answer = []

        def dfs(curr, picked):
            if len(curr) == len(nums):
                answer.append(curr[:])
                return
            for i, n in enumerate(nums):
                if not picked[i]:
                    picked[i] = True
                    curr.append(n)
                    dfs(curr, picked)
                    picked[i] = False
                    curr.pop()
        dfs([], [False]*len(nums))

        return answer




        