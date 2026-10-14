class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans = []
        for n in set1:
            if n in set2:
                ans.append(n)
        return ans
        