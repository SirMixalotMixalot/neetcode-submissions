class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumToIndex = {}
        for i, v in enumerate(nums):
            rest = target - v
            if rest in sumToIndex:
                return [sumToIndex[rest], i]
            sumToIndex[v] = i
        return [-1,-1]
        
        