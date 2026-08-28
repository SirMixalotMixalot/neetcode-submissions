class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0 for _ in range(n + 1)]
        steps[0] = 1
        steps[1] = 1 # first step?
        for stair in range(2, n + 1):
            steps[stair] = steps[stair - 1] + steps[stair - 2]
        return steps[n]    