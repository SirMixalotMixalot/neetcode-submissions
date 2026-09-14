class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        bestArea = 0
        while left < right:
            h = min(heights[left], heights[right])
            bestArea = max(bestArea, h * (right - left))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return bestArea
        