class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        mid = 0
        while left < right:
            mid = (left + right) // 2
            if self.canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left
    def canFinish(self, piles, k, h):
        if k == 0:
            return False
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/k)
        return hours <= h

        