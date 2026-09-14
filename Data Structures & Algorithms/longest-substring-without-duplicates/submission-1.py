class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        current = set(s[0])
        start = 0
        end = 0
        best = 1
        while end < len(s) - 1:
            end += 1
            while s[end] in current:
                current.remove(s[start])
                start += 1
            current.add(s[end])

            curr = end - start + 1
            if curr > best:
                best = curr
            
        return best


        