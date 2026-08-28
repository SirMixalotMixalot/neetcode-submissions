class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCosts = []
        minCosts.append(0)
        minCosts.append(0)
        for step in range(2, len(cost) + 1):
            costStepBefore = minCosts[step - 1] + cost[step - 1]
            costStep2Before = minCosts[step - 2] + cost[step - 2]
            minCosts.append(min(costStepBefore, costStep2Before))
        return minCosts[len(cost)]
        