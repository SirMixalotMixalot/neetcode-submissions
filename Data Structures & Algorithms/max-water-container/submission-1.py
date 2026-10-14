class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 # maximusing width initially
        maxWater = 0
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            maxWater = max(water, maxWater)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
        