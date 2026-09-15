class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # probably need a dict to keep track of count of letters in window
        # then window is valid if sum of non majority letters <= k
        # keep track of majority letters? hard to do
        # if i keep track of all the letters, XYYX
        # i will know on [XYY], X = 1, Y = 2, do i now search for lowest value?
        # [XYYX] i know X = 2, Y = 2, non majority <= k

        longest = 0
        left = 0
        maxfreq = 0
        counts = defaultdict(int)
        for right, ch in enumerate(s):
            counts[ch] += 1
            maxfreq = max(maxfreq, counts[ch])
            window_len = right - left + 1
            while window_len - maxfreq > k and left < len(s):
                counts[s[left]] -= 1
                left += 1
                window_len = right - left + 1
            longest = max(window_len, longest)
        
        return longest
            

        