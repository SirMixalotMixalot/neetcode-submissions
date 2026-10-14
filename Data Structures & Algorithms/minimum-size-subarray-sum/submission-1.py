class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0,1
        # windowSum = nums[start:end]
        windowSum = nums[0]
        minLength = math.inf
        while start < end <= len(nums):
            if windowSum < target and end < len(nums):
                windowSum += nums[end]
                end += 1
            elif windowSum >= target:
                minLength = min(end - start, minLength)
                windowSum -= nums[start]
                start += 1
            else:
                break
        return 0 if minLength == math.inf else minLength

