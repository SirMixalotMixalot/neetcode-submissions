class Solution:
    def trap(self, height: List[int]) -> int:
        """
height = [3, 0, 2, 0, 4]
maxOnLeft = [0, 3, 3, 3, 3]
maxOnRight = [4, 4, 4, 4, 0]
maxOnLeft = maxOnLeft[i]
maxOnRight = maxOnRight[len(height) - 1 - i]
# nothing to the left and nothing to the right
0 + 3 + 1 + 3 + 0
output = 7

        """
        # scan from left to right, get tallest on left
        # scan from right to left get tallest seen on right
        # what happens at boundaries?
        # at 0, nothing can be on my left?
        # general case -> maxHeight = min(maxOnLeft, maxOnRight)
        #              -> trapped += max(0, maxHeight - height)
        # based on general case, maybe make array have 0 on left of index 0
        # and 0 on right of index len(height) - 1
        trapped = 0
        maxOnLeft = [0] * len(height)
        maxOnRight = [0] * len(height)
        for i, h in enumerate(height):
            if i == 0:
                continue
            maxOnLeft[i] = max(height[i - 1], maxOnLeft[i - 1])
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                continue
            maxOnRight[i] = max(height[i + 1], maxOnRight[i + 1])
        
        for i, h in enumerate(height):
            mOnLeft = maxOnLeft[i]
            mOnRight = maxOnRight[i]
            maxHeight = min(mOnLeft, mOnRight)
            trapped += max(0, maxHeight - height[i])
        return trapped

        