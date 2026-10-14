class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxRight, maxLeft = height[right], height[left]
        trapped = 0
        while left < right:
            if maxLeft <= maxRight:
                # left is limiting
                left += 1
                maxLeft = max(maxLeft, height[left])
                trapped += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                trapped += maxRight - height[right]
        return trapped

        