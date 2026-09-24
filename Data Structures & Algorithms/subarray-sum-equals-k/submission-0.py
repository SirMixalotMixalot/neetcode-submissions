class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        res = 0
        for i, n in enumerate(nums):
            s += n
            if s - k in prefix:
                res += prefix[s - k]
            prefix[s] += 1
        return res

        