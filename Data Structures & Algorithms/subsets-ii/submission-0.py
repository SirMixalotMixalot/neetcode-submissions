class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        # [1, 1, 2, 3, 3]
        # include 1, skip 1
        # include 1 <- good
        # skip 1, only bad after we skipped 1
        # include 1, dfs, exclude 1 (in this branch,)
        def dfs(curr, i):
            nonlocal ans
            
            if i >= len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[i])
            dfs(curr, i +1)
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(curr, i + 1)

        dfs([], 0)
        return ans